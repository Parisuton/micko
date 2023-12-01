import subprocess
from pathlib import Path
import sys

# Check if config.json exists in the configuration folder
def check_config():
    config_path = Path("config", "config.json")

    if not config_path.exists():
        print("Configuration file not found. Launching configuration.py...")
        
        # Launch configuration.py from the parent folder
        subprocess.run([sys.executable, 'config/configuration.py'], creationflags=subprocess.CREATE_NO_WINDOW)

        # Wait for configuration.py to be saved
        while not config_path.exists():
            pass

    print("Configurations are loaded. Continue with the rest of the application.\n ##############\n\n\n")

def main():
    check_config()
    # Get the full path to systray.py
    systray_path = Path(__file__).parent / "systray.py"

    # Launch systray.py
    subprocess.run([sys.executable, str(systray_path)], creationflags=subprocess.CREATE_NO_WINDOW)

if __name__ == "__main__":
    main()
