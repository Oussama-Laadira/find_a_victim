import json
import csv
import requests
import os
import time
import sys

GREEN = "\033[92m"
RESET = "\033[0m"

os.system("cls" if os.name == "nt" else "clear")

banner = r"""
___________.__            .___          ____   ____.__        __  .__         
\_   _____/|__| ____    __| _/ _____    \   \ /   /|__| _____/  |_|__| _____  
 |    __)  |  |/    \  / __ |  \__  \    \   Y   / |  |/ ___\   __\  |/     \ 
 |     \   |  |   |  \/ /_/ |   / __ \_   \     /  |  \  \___|  | |  |  Y Y  \
 \___  /   |__|___|  /\____ |  (____  /    \___/   |__|\___  >__| |__|__|_|  /
     \/            \/      \/       \/                     \/              \/ 
"""

def animated_print(text, delay=0.0005):
    for char in text:
        sys.stdout.write(GREEN + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)

animated_print(banner)
animated_print("\nDeveloped by Mr.Ghost\n\n")
# ----------------------------------
# 1. قراءة ملف JSON
# ----------------------------------
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

sites = data["sites"]   # ← هنا المواقع تكون بصيغة { "facebook": "https://...", ... }

# ----------------------------------
# 2. أخذ اسم المستخدم
# ----------------------------------
username = input("enter User Name : ")
username_clean = username.replace(" ", "")

# ----------------------------------
# 3. تجهيز ملف CSV لحفظ النتائج
# ----------------------------------
with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Website", "URL", "Status"])  # عنوان الأعمدة

    # ----------------------------------
    # 4. فحص كل موقع
    # ----------------------------------
    for site_name, url_pattern in sites.items():

        # بناء الرابط
        url = url_pattern.format(username_clean)

        try:
            r = requests.get(url, timeout=5)

            if r.status_code == 200:
                status = "FOUND"
                print(f"✔ yes {site_name}: {url}")
            else:
                status = "NOT FOUND"
                print(f"✖ no {site_name}")

        except Exception:
            status = "ERROR"
            print(f"⚠ error connecting to {site_name}")

        # حفظ النتيجة في CSV
        writer.writerow([site_name, url, status])
print("\n Save results.csv ✓")