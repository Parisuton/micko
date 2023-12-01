# micko
Meet micko, the unapologetic microphone volume monitor designed to beep the living daylights out of loud gamers. Crafted by a husband who understands that sometimes, a little extra encouragement is needed to keep those vocal cords in check. By a gamer who knows that when the game gets intense, the shouts get loud. This design ensures that wives stay happy and gaming sessions stay epic. 

![micko](/src/icons/micko.ico)

## Overview
micko is not your average microphone volume monitor—it's the enforcer of audio discipline in the gaming realm. With a knack for turning excitement into beeps, micko keeps loud gamers in check. Shout too loud, and brace yourself for a symphony of beeps. Why? Because happy wives make for uninterrupted gaming marathons.

## Features
- __Threshold Volume Control:__ Adjust the microphone threshold volume with surgical precision using the intuitive slider. Fine-tune it to your preferred level for an optimal audio experience, ensuring that every shout is met with a strategic beep.

- __Beep Sound Selection:__ Choose your preferred beep sound from a range of beeping options. Preview the sound with a simple click and set the tone that rings in your ears.

- __Device Selection:__ micko gives you the flexibility to choose your sound recording device. Browse through available devices and select the one that perfectly captures your voice.

- __Configuration Saving:__ Save your personalized settings effortlessly. micko ensures that your preferences are stored securely, because a well-configured micko is a happy micko.

- __A Minimalist Design:__ Hold your focus on things that matter: micko features a minimalist design that makes running it extremely lightweight and uninterruptive.

## Usage

Once you have installed and ran micko, you will spot the micko icon (see above) in your system tray, nestled discreetly among your other applications. Right-click on the micko icon to unveil a menu of options. When you notice a red circle on the top right of the micko icon, it is successfully monitoring your microphone!

## Compatibility
micko is designed to enhance your audio experience on Windows. It integrates seamlessly with your existing setup, offering a hassle-free monitoring solution. micko runs in the system tray, so look out for those bottom right icons!

# Installation
Follow these steps to install micko on your Windows machine:

> [!NOTE]
>### Prerequisites: Python and Git Installations
>Skip this if you have Python and Git installed on your Windows machine already.
>1. Download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/windows/).
>   - During installation, make sure to check the box that says "Add Python to PATH."
>2. Download and install Git from the official website: [Git website](https://git-scm.com/downloads).


### Step 1: Clone the Repository
- Open the command prompt (cmd) or terminal.
- Navigate to the directory using `cd <C:\Path>` where you want to install micko.
- Run the following command to clone the repository: ```git clone https://github.com/Parisuton/micko.git```


### Step 2: Navigate to micko Directory
Change the working directory to the newly cloned micko folder:
```cd micko```


### Step 3: Install micko's Dependencies
Run the following command to install the required Python packages: ```pip install -r requirements.txt```


### Step 4: Run micko
Run micko using the following command: ```python run_micko.pyw```

You can also make a shortcut for micko by right-clicking on run_micko.pyw and selecting "Send to" --> "Desktop (create shortcut)". You can now double-click the shortcut.

When you first start micko, you will be prompted with the configuration window. After that you should find it in the system tray. Search for the micko icon!


>[!TIP]
> ### Auto-Start on Windows
> Here are ezpz steps on how to start micko with your Windows:
> - __Create Shortcut:__ Right-click on `run_micko.pyw` and create a shortcut.
> - __Open Startup Folder:__ Press `Windows+R`, type `shell::startup`, and press Enter.
> - __Add Shortcut:__ Drag the shortcut into the opened Startup folder.
> Now, micko will run on Windows startup.