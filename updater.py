import os
import shutil
import requests
import zipfile
import io
import time

REPO_ZIP_URL = "https://github.com/Drowys22/Comfox/archive/refs/heads/main.zip"
TARGET_DIR = "."

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BLACK = "\033[90m"
ORANGE = "\033[38;5;208m"
ORANGE_1 = "\033[38;5;166m"

BG_RED = "\033[41m"
BG_BLUE = "\033[44m"
BG_WHITE = "\033[47m"

print(MAGENTA + "┌──────────────────────────────────────────┐")
time.sleep(0.3)
print(MAGENTA + "│" + RED + "        ComFox Updater - Initializing     " + MAGENTA + "│")
time.sleep(0.3)
print(MAGENTA + "└──────────────────────────────────────────┘" + RESET)
time.sleep(0.3)
print("")
time.sleep(1)
print(CYAN + "Fetching latest build from GitHub...")
time.sleep(2)
print(CYAN + "Preparing update environment...")
time.sleep(2)


def delete_old_files():
    print(CYAN + "Deleting old files...")
    time.sleep(5)

    for item in os.listdir(TARGET_DIR):
        if item == "updater.py":
            continue
        path = os.path.join(TARGET_DIR, item)

        try:
            if os.path.isfile(path) or os.path.islink(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
        except Exception as e:
            print(RED + f"Error on delete: {e}")

def download_and_extract():
    print(CYAN + "Downloading the newest version from github...")
    time.sleep(5)

    response = requests.get(REPO_ZIP_URL)
    if response.status_code != 200:
        print(RED + "Error: Failed to download the ZIP.")
        return

    print(CYAN + "Unboxing...")
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
        zip_ref.extractall(TARGET_DIR)

    extracted_folder = os.path.join(TARGET_DIR, "Comfox-main")

    for item in os.listdir(extracted_folder):
        shutil.move(os.path.join(extracted_folder, item), TARGET_DIR)

    shutil.rmtree(extracted_folder)
    print(GREEN + "\nSuccessfully downloaded! Please restart ComFox to apply the update.")
    time.sleep(0.3)
    input(GREEN + "Press Enter to exit...")

if __name__ == "__main__":
    delete_old_files()
    download_and_extract()
