import subprocess
import sys
from pathlib import Path
import os

def install_dependencies():
    subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'],creationflags=subprocess.CREATE_NO_WINDOW)
    subprocess.run([sys.executable, 'src/setup.py', 'install'],creationflags=subprocess.CREATE_NO_WINDOW)

def check_config():
    config_path = Path("config") / "config.json"

    if not config_path.exists():
        print("Configuration file not found. Launching configuration.py...")

        subprocess.run([sys.executable, str(Path("config") / "configuration.py")],creationflags=subprocess.CREATE_NO_WINDOW)

        # Wait for configuration.py to be saved
        while not config_path.exists():
            pass

def start_micko():
    subprocess.run([sys.executable, str(Path("src") / "micko.py")],creationflags=subprocess.CREATE_NO_WINDOW)


def main():
    # Set the current working directory to the root of the project
    os.chdir(Path(__file__).resolve().parent)

    check_config()
    start_micko()
if __name__ == "__main__":
    install_dependencies()
    main()
