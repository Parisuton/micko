import subprocess
import sys
from pathlib import Path
import os

def start_micko():
    subprocess.run([sys.executable, str(Path("src") / "micko.py")],creationflags=subprocess.CREATE_NO_WINDOW)

def main():
    # This sets the current working directory as the root of the project
    os.chdir(Path(__file__).resolve().parent)

    start_micko()

if __name__ == "__main__":
    main()