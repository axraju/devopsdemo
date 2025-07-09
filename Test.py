import subprocess

import sys

from pathlib import Path
 
def install_requirements(file_path='requirements.txt'):

    req_file = Path(file_path)

    if not req_file.is_file():

        print(f"[ERROR] requirements.txt not found at: {req_file.resolve()}")

        return False
 
    try:

        print("[INFO] Installing packages from requirements.txt...\n")

        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req_file)])

        print("\n[SUCCESS] All packages installed successfully.")

        return True

    except subprocess.CalledProcessError as e:

        print(f"\n[ERROR] pip installation failed with error:\n{e}")

        return False

    except Exception as ex:

        print(f"\n[UNEXPECTED ERROR] {ex}")

        return False
 
def run_hello_world(script_name='Hello_World.py'):

    script_file = Path(script_name)

    if not script_file.is_file():

        print(f"[ERROR] {script_name} not found at: {script_file.resolve()}")

        return
 
    try:

        print(f"[INFO] Running {script_name}...\n")

        subprocess.check_call([sys.executable, str(script_file)])

    except subprocess.CalledProcessError as e:

        print(f"[ERROR] Script execution failed:\n{e}")

    except Exception as ex:

        print(f"[UNEXPECTED ERROR] {ex}")
 
if __name__ == "__main__":

    if install_requirements():

        run_hello_world()

 
