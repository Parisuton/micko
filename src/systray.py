import os
import sys
import subprocess
import threading
import pystray
from PIL import Image
from pystray import MenuItem as item

# Function to open configuration.py
def open_configuration(icon, item):
    global microphone_listening

    if microphone_listening:
        stop_mic_listener(icon)

    subprocess.run(["python", os.path.join("config", "configuration.py")])

# Function to exit the application
def exit_application(icon, item):
    if microphone_listening:
        stop_mic_listener(icon)
    icon.stop()
    os._exit(0)

# Function to toggle microphone and change the icon
def toggle_microphone(icon, item):
    global microphone_listening
    microphone_listening = not microphone_listening

    # Change the icon based on microphone state
    if microphone_listening:
        start_mic_listener(icon)
    else:
        stop_mic_listener(icon)

# Function to start mic_listener.py
def start_mic_listener(icon):
    global mic_listener_process
    # If the process is not started or has terminated, start a new one
    if not mic_listener_process or mic_listener_process.poll() is not None:
        mic_listener_path = os.path.join(script_directory, "mic_listener.py")
        mic_listener_process = subprocess.Popen(["python", mic_listener_path])
        icon.icon = Image.open(os.path.join(script_directory, "icons/micko_recording.ico"))

# Function to stop mic_listener.py
def stop_mic_listener(icon):
    global mic_listener_process

    # If the process is started, terminate it forcefully
    if mic_listener_process and mic_listener_process.poll() is None:
        mic_listener_process.terminate()

    mic_listener_process = None
    icon.icon = Image.open(os.path.join(script_directory, "icons/micko.ico"))

# Function to create the system tray icon
def create_systray():
    icon_path = os.path.join(script_directory, "icons/micko.ico")
    image = Image.open(icon_path)

    # Create menu items
    menu = (item('Toggle Microphone Listening', toggle_microphone, default=True),
            item('Open Configuration', open_configuration),
            item('Exit Application', exit_application))

    # Set up the system tray icon
    icon = pystray.Icon("micko", image, menu=menu)

    # Run the system tray icon in a separate thread
    threading.Thread(target=icon.run).start()

if __name__ == "__main__":
    # Variable to track microphone state
    microphone_listening = False
    # Process to track mic_listener subprocess
    mic_listener_process = None

    # Get the script directory using sys.argv[0]
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

    create_systray()
