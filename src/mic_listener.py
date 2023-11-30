import json
import sounddevice as sd
from beeply.notes import *
from numpy.linalg import norm
from pathlib import Path

class MicrophoneListener:
    def __init__(self):
        self.load_configuration()
        self.beep = beeps()

    def start_listening(self):
        def callback(indata, frames, time, status):
            volume_norm = norm(indata) * 10
            if volume_norm > self.threshold_volume:
                self.beep.hear(self.beep_note)

        with sd.InputStream(device=self.sound_device, callback=callback, channels=1, samplerate=44100):
            while True:
                sd.sleep(1000000)  # Sleep for a long time, as we don't intend to stop listening

    def load_configuration(self):
        config_path = Path(__file__).resolve().parent.parent / "config" / "config.json"
        # print(f"Config Path: {config_path}")  # Debug line
        try:
            with config_path.open("r") as config_file:
                config_data = json.load(config_file)
            
            print(f"Loaded Configuration: {config_data}")  # Debug line

            self.sound_device = config_data.get("recording_device_index", 0)
            self.threshold_volume = config_data.get("threshold_volume", 40.0)
            self.beep_note = config_data.get("beep_sound", "_B")

            # Debug lines
            print(f"Loaded sound_device: {self.sound_device}")
            print(f"Loaded threshold_volume: {self.threshold_volume}")
            print(f"Loaded beep_note: {self.beep_note}")

        except FileNotFoundError:
            self.sound_device = 0
            self.threshold_volume = 40.0
            self.beep_note = "_B"


if __name__ == "__main__":
    listener = MicrophoneListener()
    listener.start_listening()
