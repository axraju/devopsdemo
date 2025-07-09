import subprocess
import sys
from pathlib import Path
import importlib.util
 
def log(msg):
    print(f"[INFO] {msg}")
 
def error(msg):
    print(f"[ERROR] {msg}")
    sys.exit(1)
 
def is_package_installed(pkg_name: str) -> bool:
    return importlib.util.find_spec(pkg_name) is not None
 
def parse_package_name(line: str) -> str:
    for sep in ['==', '>=', '<=', '~=', '>', '<']:
        if sep in line:
            return line.split(sep)[0].strip()
    return line.strip()
 
def install_requirements():
    req_path = Path("requirements.txt")
    if not req_path.exists():
        error("requirements.txt not found.")
 
    log("Checking for missing packages...")
    with req_path.open() as f:
        packages = [line.strip() for line in f if line.strip() and not line.startswith("#")]
 
    missing = []
    for pkg in packages:
        pkg_name = parse_package_name(pkg)
        if not is_package_installed(pkg_name):
            log(f"Package missing: {pkg_name}")
            missing.append(pkg)
 
    if missing:
        log(f"Installing missing packages: {missing}")
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing)
        log("Missing packages installed.")
    else:
        log("All packages already installed.")
 
def run_hello_world():
    script_path = Path("Hello_World.py")
    if not script_path.exists():
        error("Hello_World.py not found.")
    log("Running Hello_World.py...")
    subprocess.check_call([sys.executable, str(script_path)])
 
if __name__ == "__main__":
    install_requirements()
    run_hello_world()