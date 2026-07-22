import frappe
from frappe.model.document import Document

class ANCLoginSettings(Document):

    def validate(self):
        if self.logo_height and (int(self.logo_height) < 20 or int(self.logo_height) > 200):
            frappe.throw("ارتفاع الشعار يجب أن يكون بين 20 و 200 بكسل")

    def on_update(self):
        """عند الحفظ: امسح الكاش حتى تظهر التغييرات فوراً"""
        frappe.cache().delete_key("anc_login_settings")
        frappe.clear_cache()
