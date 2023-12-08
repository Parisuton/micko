import os
import sys
import subprocess
import threading
import pystray
from PIL import Image
from pystray import MenuItem as item
from pathlib import Path

# Function to open configuration.py
def open_configuration(icon, item):
    global microphone_listening

    if microphone_listening:
        stop_mic_listener(icon)

    subprocess.run(["python", os.path.join("config", "configuration.py")], creationflags=subprocess.CREATE_NO_WINDOW)

# Function to exit the application
def exit_application(icon, item):
    if microphone_listening:
        stop_mic_listener(icon)
    icon.stop()
    os._exit(0)

def open_info(icon):
    subprocess.run(["python", os.path.join("src", "infowindow.py")], creationflags=subprocess.CREATE_NO_WINDOW)

# Function to toggle microphone
def toggle_microphone(icon, item):
    global microphone_listening
    microphone_listening = not microphone_listening

    if microphone_listening:
        start_mic_listener(icon)
    else:
        stop_mic_listener(icon)

# Function to start mic_listener.py and change icon
def start_mic_listener(icon):
    global mic_listener_process
    # If the process is not started or has terminated, start a new one
    if not mic_listener_process or mic_listener_process.poll() is not None:
        mic_listener_path = Path(script_directory) / "src" / "mic_listener.py"  # Updated path using pathlib
        mic_listener_process = subprocess.Popen(["python", str(mic_listener_path)], creationflags=subprocess.CREATE_NO_WINDOW)
        
        # Change the icon based on microphone state
        icon.icon = Image.open(Path(script_directory) / "assets" / "micko_recording.ico")  # Updated path using pathlib

# Function to stop mic_listener.py and revert icon change
def stop_mic_listener(icon):
    global mic_listener_process

    # If the process is started, terminate it forcefully
    if mic_listener_process and mic_listener_process.poll() is None:
        mic_listener_process.terminate()

    mic_listener_process = None
    
    # Change the icon based on microphone state
    icon.icon = Image.open(Path(script_directory) / "assets" / "micko.ico")  # Updated path using pathlib

# Function to create the system tray icon
def create_systray():
    icon_path = Path(script_directory) / "assets" / "micko.ico"  # Updated path using pathlib
    image = Image.open(icon_path)

    # Create menu items
    menu = (item('micko:', toggle_microphone, default=True),
            item('Toggle Monitoring', toggle_microphone),
            item('Settings', open_configuration),
            item('About', open_info),
            item('Exit', exit_application))

    # Sets the default icon
    icon = pystray.Icon("micko", image, menu=menu)

    # Run the system tray icon in a separate thread
    threading.Thread(target=icon.run).start()

if __name__ == "__main__":
    # Variable to track microphone state
    microphone_listening = False
    # Process to track mic_listener subprocess
    mic_listener_process = None

    # Get the script directory using sys.argv[0]
    script_directory = Path(sys.argv[0]).resolve().parent.parent  # Updated to use pathlib

    create_systray()
