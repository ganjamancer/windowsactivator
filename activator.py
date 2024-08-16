import os
import time

# Licenses
licenses = {
  "1": "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"
  "2": "3KHY7-WNT83-DGQKR-F7HPR-844BM"
  "3": "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH"
  "4": "PVMJN-6DFY6–9CCP6–7BKTT-D3WVR"
  "5": "W269N-WFGWX-YVC9B-4J6C9-T83GX"
  "6": "MH37W-N47XK-V7XM9-C7227-GCQG9"
  "7": "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2"
  "8": "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ"
  "9": "NPPR9-FWDCX-D2C8J-H872K-2YT43"
  "10": "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4"
}

def check_python_version():
    print("Checking Python version...")
    time.sleep(1)
    os.system("python --version")
    return input("Is this correct? (y/n): ").strip().lower() == "y"

def select_version():
    print("\nPlease select your version:")
    print("""
    (1) Home
    (2) Home N
    (3) Home Single Language
    (4) Home Country Specific
    (5) Pro
    (6) Pro N
    (7) Educational
    (8) Educational N
    (9) Enterprise
    (10) Enterprise N
    """)
    return input("Pick your version (1-10): ").strip()

def apply_license(version):
    if version in licenses:
        os.system(f"slmgr /ipk {licenses[version]}")
        time.sleep(1)
        print("Verifying the license...")
        os.system("slmgr /skms kms8.msguides.com")
        time.sleep(1)
        print("Applying license...")
        os.system("slmgr /ato")
        print("If a small window showed saying 'Product activated successfully', you're done!")
    else:
        print("Invalid selection. Please try again.")

def main():
    print("Please share this repo!")
    print("https://github.com/ganjamancer/windowsactivator/\n")
    
    if check_python_version():
        version = select_version()
        apply_license(version)
    else:
        print("Please reinstall Python or reboot after ensuring Python is installed.")
        os.system("exit")

if __name__ == "__main__":
    main()
