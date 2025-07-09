import subprocess

import sys

from pathlib import Path
 
def log(msg):

    print(f"[INFO] {msg}")
 
def error(msg):

    print(f"[ERROR] {msg}")

    sys.exit(1)
 
def install_requirements():

    req_path = Path("requirements.txt")

    if not req_path.exists():

        error("requirements.txt not found.")

    log("Installing requirements...")

    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req_path)])

    log("Requirements installed.")
 
def run_hello_world():

    script_path = Path("Hello_World.py")

    if not script_path.exists():

        error("Hello_World.py not found.")

    log("Running Hello_World.py...")

    subprocess.check_call([sys.executable, str(script_path)])
 
if __name__ == "__main__":

    install_requirements()

    run_hello_world()

 