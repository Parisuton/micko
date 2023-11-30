import os
import subprocess

def check_config():
    # Check if config.json exists in the configuration folder
    config_path = os.path.join("configuration", "config.json")

    if not os.path.exists(config_path):
        print("Configuration file not found. Launching configuration.py...")
        
        # Launch configuration.py
        subprocess.run(["python", os.path.join("configuration", "configuration.py")])

        # Wait for configuration.py to be saved
        while not os.path.exists(config_path):
            pass

    print("Configurations are loaded. Continue with the rest of the application.")

def main():
    check_config()
    

main()