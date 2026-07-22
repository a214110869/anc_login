app_name = "anc_login"
app_title = "ANC Login"
app_publisher = "Reflection"
app_description = "Custom Login Page for ANC (Arif Al-Nahdi Co Ltd)"
app_email = "dev@reflection.net.sa"
app_license = "MIT"
app_version = "1.0.0"

# Override login page
website_route_rules = [
    {"from_route": "/login", "to_route": "login"},
]

# Hooks
on_session_creation = "anc_login.api.on_session_creation"
after_install = "anc_login.install.after_install"
