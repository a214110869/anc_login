import subprocess
import sys
import os

def after_install():
    """تثبيت الـ app في بيئة Frappe بعد التثبيت مباشرة"""
    try:
        bench_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
        pip_path   = os.path.join(bench_path, 'env', 'bin', 'pip')
        app_path   = os.path.join(bench_path, 'apps', 'anc_login')

        if os.path.exists(pip_path) and os.path.exists(app_path):
            subprocess.run([pip_path, 'install', '-e', app_path, '-q'], check=True)
            print("✅ anc_login installed in Frappe env")
        else:
            print("⚠️ Could not find pip or app path")
    except Exception as e:
        print(f"⚠️ after_install error: {e}")
