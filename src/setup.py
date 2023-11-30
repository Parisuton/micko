from setuptools import setup, find_packages

setup(
    name='micko',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'beeply',
        'numpy',
        'sounddevice',
        "Pillow",
        "pystray",
        "pyaudio"
    ],
)
