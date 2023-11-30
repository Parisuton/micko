import subprocess
import sys
import time

def install_dependencies():
    subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.run([sys.executable, 'setup.py', 'install'])

def start_micko():
    subprocess.run([sys.executable, 'src/micko.py'])

if __name__ == "__main__":
    install_dependencies()
    start_micko()
    time.sleep(4)