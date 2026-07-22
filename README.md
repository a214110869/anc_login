# ANC Login — Custom Frappe App

صفحة دخول مخصصة لشركة عارف النهدي المحدودة على ERPNext 15.

## التثبيت

```bash
cd /home/frappe/frappe-bench
bench get-app anc_login https://github.com/YOUR_ORG/anc_login
bench --site anc.flexsofts.cloud install-app anc_login
bench --site anc.flexsofts.cloud migrate
bench restart
```

## الإعدادات

بعد التثبيت:
1. افتح ERPNext → ابحث عن **ANC Login Settings**
2. ارفع شعارك وغيّر الخط واللون
3. احفظ — التغييرات تظهر فوراً على صفحة الدخول

## رفع الشعار

ضع ملفات الشعار في:
```
anc_login/public/images/logo.png
anc_login/public/images/logo-white.png
```
ثم شغّل: `bench build --app anc_login`
