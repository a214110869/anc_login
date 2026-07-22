import frappe

no_cache = 1

def get_context(context):
    """جيب إعدادات صفحة الدخول وحطها في context"""
    defaults = {
        "logo_url": "",
        "logo_top_url": "",
        "logo_h": "52",
        "font_family": "IBM Plex Sans Arabic",
        "primary_color": "#C8102E",
        "company_name": "Arif Al-Nahdi Co Ltd",
        "website_url": "https://anc.sa",
        "website_label": "anc.sa",
        "powered_by": "Reflection",
        "powered_by_url": "https://reflection.net.sa",
    }

    try:
        if frappe.db.exists("DocType", "ANC Login Settings"):
            s = frappe.db.get_singles_dict("ANC Login Settings")
            defaults.update({
                "logo_url":       s.get("logo_url", ""),
                "logo_top_url":   s.get("logo_topbar_url", ""),
                "logo_h":         s.get("logo_height", "52") or "52",
                "font_family":    s.get("font_family", "IBM Plex Sans Arabic") or "IBM Plex Sans Arabic",
                "primary_color":  s.get("primary_color", "#C8102E") or "#C8102E",
                "company_name":   s.get("company_name", "Arif Al-Nahdi Co Ltd") or "Arif Al-Nahdi Co Ltd",
                "website_url":    s.get("website_url", "https://anc.sa") or "https://anc.sa",
                "website_label":  s.get("website_label", "anc.sa") or "anc.sa",
                "powered_by":     s.get("powered_by", "Reflection") or "Reflection",
                "powered_by_url": s.get("powered_by_url", "https://reflection.net.sa") or "https://reflection.net.sa",
            })
    except Exception:
        pass

    context.update(defaults)
    return context
