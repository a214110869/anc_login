import frappe

def on_session_creation(login_manager):
    """Called after successful login"""
    pass

@frappe.whitelist(allow_guest=True)
def get_login_settings():
    """Return login page settings"""
    if not frappe.db.exists("DocType", "ANC Login Settings"):
        return {"enabled": True}

    settings = frappe.db.get_singles_dict("ANC Login Settings")
    return {
        "enabled":         bool(int(settings.get("enabled", 1))),
        "logo_url":        settings.get("logo_url", "/assets/anc_login/images/logo.png"),
        "logo_topbar_url": settings.get("logo_topbar_url", "/assets/anc_login/images/logo-white.png"),
        "logo_height":     settings.get("logo_height", "52"),
        "font_family":     settings.get("font_family", "IBM Plex Sans Arabic"),
        "primary_color":   settings.get("primary_color", "#C8102E"),
        "company_name":    settings.get("company_name", "Arif Al-Nahdi Co Ltd"),
        "website_url":     settings.get("website_url", "https://anc.sa"),
        "website_label":   settings.get("website_label", "anc.sa"),
        "powered_by":      settings.get("powered_by", "Reflection"),
        "powered_by_url":  settings.get("powered_by_url", "https://reflection.net.sa"),
    }

@frappe.whitelist()
def toggle_login_page(enable):
    """System Manager فقط يقدر يشغّل/يوقف الصفحة"""
    if "System Manager" not in frappe.get_roles():
        frappe.throw("غير مصرح", frappe.PermissionError)

    if not frappe.db.exists("DocType", "ANC Login Settings"):
        frappe.throw("ANC Login Settings DocType غير موجود")

    frappe.db.set_single_value("ANC Login Settings", "enabled", 1 if frappe.parse_json(enable) else 0)
    frappe.db.commit()
    frappe.cache().delete_key("anc_login_settings")
    frappe.clear_cache()
    return {"enabled": frappe.parse_json(enable)}
