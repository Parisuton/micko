import tkinter as tk
from tkinter import ttk
from beeply.notes import *
import json
import os
import pyaudio
from pathlib import Path

class ConfigurationWindow:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("micko")
        self.parent.geometry("415x190")
        self.parent.resizable(False, False)
        self.set_dark_theme()
        self.create_widgets()
        self.load_settings()

    def set_dark_theme(self):
        # Background color for the entire window
        self.parent.configure(bg="#2E2E2E")

        # Appearance
        self.parent.option_add('*TFrame*Background', '#2E2E2E')
        self.parent.option_add('*TFrame*Foreground', 'white')
        self.parent.option_add('*TLabel*Background', '#2E2E2E')
        self.parent.option_add('*TLabel*Foreground', 'white')
        self.parent.option_add('*TButton*Background', '#404040')
        self.parent.option_add('*TButton*Foreground', 'white')
        self.parent.option_add('*TButton*activeBackground', '#606060')
        self.parent.option_add('*TCombobox*Background', '#404040')
        self.parent.option_add('*TCombobox*Foreground', 'white')
        self.parent.option_add('*TCombobox*fieldBackground', '#404040')
        self.parent.option_add('*TEntry*Background', '#404040')
        self.parent.option_add('*TEntry*Foreground', 'white')

    def create_widgets(self):
        frame = ttk.Frame(self.parent, padding="10", style="TFrame")  # Use the dark style for the frame
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Threshold Volume
        ttk.Label(frame, text="Threshold Volume", style="TLabel").grid(row=0, column=0, pady=10)
        self.threshold_var = tk.DoubleVar()
        self.threshold_var.set(40.0)
        ttk.Scale(frame, from_=0, to=100, variable=self.threshold_var, length=200, orient=tk.HORIZONTAL, command=self.update_threshold_entry).grid(row=0, column=1, pady=10)
        self.threshold_entry = ttk.Entry(frame, textvariable=self.threshold_var, width=5)
        self.threshold_entry.grid(row=0, column=2, padx=5)


        ttk.Entry(frame, textvariable=self.threshold_var, width=5).grid(row=0, column=2, padx=5)

        # Beep Sound
        ttk.Label(frame, text="Beep Sound").grid(row=1, column=0, pady=10)
        self.note_var = tk.StringVar()
        self.note_var.set("A_")
        ttk.Combobox(frame, textvariable=self.note_var, values=["_B", "C", "D", "E", "F", "G", "A", "B", "C_", "D_", "E_", "F_", "G_", "A_", "B_", "C__"], state="readonly").grid(row=1, column=1, pady=10)
        ttk.Button(frame, text="Listen", command=self.preview_sound).grid(row=1, column=2, padx=5)

        # Sound Recording Devices
        ttk.Label(frame, text="Microphone Device").grid(row=2, column=0, pady=10)
        self.device_var = tk.StringVar()
        combobox = ttk.Combobox(frame, textvariable=self.device_var, values=[device[1] for device in self.get_available_devices()], width=30, state="readonly")
        combobox.grid(row=2, column=1, pady=10)


        # Save Button
        ttk.Button(frame, text="Save", command=self.save_settings).grid(row=3, column=0, columnspan=2, pady=10)
        
    def preview_sound(self):
        beep_note = self.note_var.get()
        beeps().hear(beep_note)

    def get_available_devices(self):
        p = pyaudio.PyAudio()
        devices = []

        for i in range(p.get_device_count()):
            device_info = p.get_device_info_by_index(i)
            if device_info["maxInputChannels"] > 0 and device_info["hostApi"] == 0:
                devices.append((i, device_info["name"]))

        p.terminate()
        return devices

    def update_threshold_entry(self, value):
        # Adjust the value to increments of 0.5
        rounded_value = round(float(value) * 2) / 2
        self.threshold_var.set(rounded_value)

        # Update the entry
        self.threshold_entry.delete(0, tk.END)
        self.threshold_entry.insert(0, f"{rounded_value:.1f}")


    def update_combobox_width(self):
        # Dynamically update the dropdown width based on the length of the longest item
        longest_item = max(self.get_available_devices(), key=lambda x: len(x[1]))
        width = len(longest_item[1]) + 2 
        self.device_combobox.config(width=width)
        self.threshold_scale.config(length=width * 10)  # Adjusts the length based on the width
        self.threshold_entry.config(width=int(width / 2))  # Adjusts the width of the entry based on the width


    def load_settings(self):
        # Load configuration from the JSON file
        script_directory = os.path.dirname(os.path.realpath(__file__))
        json_file_path = os.path.join(script_directory, "config.json")

        try:
            with open(json_file_path, "r") as file:
                settings = json.load(file)
                self.threshold_var.set(settings.get("threshold_volume", 40.0))
                self.note_var.set(settings.get("beep_sound", "A_"))

                # Use the saved device index to set the selected device in the ComboBox
                saved_device_index = settings.get("recording_device_index", None)
                if saved_device_index is not None:
                    available_devices = self.get_available_devices()
                    saved_device_name = next((device[1] for device in available_devices if device[0] == int(saved_device_index)), "")
                    self.device_var.set(saved_device_name)
        except FileNotFoundError:
            pass  # If the file is not found due to error, the other file knows some default values

    def save_settings(self):
        settings = {
            "threshold_volume": self.threshold_var.get(),
            "beep_sound": self.note_var.get(),
        }

        # Save the device index along with the name
        selected_device = next((device for device in self.get_available_devices() if device[1] == self.device_var.get()), None)
        if selected_device:
            settings["recording_device_index"] = selected_device[0]

        # Save configuration to the JSON file in the script's directory
        script_directory = Path(__file__).resolve().parent
        json_file_path = script_directory / "config.json"

        with open(json_file_path, "w") as file:
            json.dump(settings, file)

        self.parent.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ConfigurationWindow(root)
    root.mainloop()