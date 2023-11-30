import os
import subprocess
import sys

def check_config():
    # Check if config.json exists in the configuration folder
    config_path = os.path.join("config", "config.json")

    if not os.path.exists(config_path):
        print("Configuration file not found. Launching configuration.py...")
        
        # Launch configuration.py
        subprocess.run([sys.executable, 'micko.py'], creationflags=subprocess.CREATE_NO_WINDOW)

        # Wait for configuration.py to be saved
        while not os.path.exists(config_path):
            pass

    print("Configurations are loaded. Continue with the rest of the application.\n ##############\n\n\n")

def main():
    check_config()
    # Get the full path to systray.py
    systray_path = os.path.join(os.path.dirname(__file__), "systray.py")

    # Launch systray.py
    subprocess.run(["python", systray_path],creationflags=subprocess.CREATE_NO_WINDOW)

main()