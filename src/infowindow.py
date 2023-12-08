import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk, ImageSequence
import webbrowser 

def show_info_window():
    info_window = tk.Tk()
    info_window.title("micko") 

    current_dir = Path(__file__).resolve().parent.parent
    assets_dir = current_dir / "assets"

    icon_path = assets_dir / "micko.ico" 
    if icon_path.exists():
        info_window.iconbitmap(icon_path)

    # Load and display the first gif
    tray_image1_path = assets_dir / "systemtray.gif"
    if tray_image1_path.exists():
        tray_image1 = Image.open(tray_image1_path)
        frames1 = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(tray_image1)]
        num_frames1 = len(frames1)
        current_frame1 = 0

        def update_animation1():
            nonlocal current_frame1
            img = frames1[current_frame1]
            tray_label1.configure(image=img)
            tray_label1.image = img
            current_frame1 = (current_frame1 + 1) % num_frames1
            info_window.after(100, update_animation1)

        tray_label1 = tk.Label(info_window, image=frames1[0])
        tray_label1.pack(pady=10)

        # Start the animation loop for the first gif
        info_window.after(0, update_animation1)

        # Add text label below the first gif
        text_label1 = tk.Label(info_window, text="You will find micko waiting for you in your system tray, shown above.\nYou can pin micko on the taskbar by dragging the icon.")
        text_label1.pack(pady=5)

    else:
        print(f"Error: {tray_image1_path} not found.")

    # Load and display the second gif
    tray_image2_path = assets_dir / "systemtray2.gif"
    if tray_image2_path.exists():
        tray_image2 = Image.open(tray_image2_path)
        frames2 = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(tray_image2)]
        num_frames2 = len(frames2)
        current_frame2 = 0

        def update_animation2():
            nonlocal current_frame2
            img = frames2[current_frame2]
            tray_label2.configure(image=img)
            tray_label2.image = img
            current_frame2 = (current_frame2 + 1) % num_frames2
            info_window.after(100, update_animation2)

        tray_label2 = tk.Label(info_window, image=frames2[0])
        tray_label2.pack(pady=10)

        # 2nd animation loop
        info_window.after(0, update_animation2)

        # Text label
        text_label2 = tk.Label(info_window, text="Toggle micko monitoring by left-clicking it. Monitoring is marked by the red circle on the icon.\nFind more options by right-clicking the icon.")
        text_label2.pack(pady=5)

    else:
        print(f"Error: {tray_image2_path} not found.")

    # GitHub button to open the GitHub page
    github_button = tk.Button(info_window, text="GitHub", command=lambda: webbrowser.open("https://github.com/Parisuton/micko"))
    github_button.pack(side=tk.LEFT, padx=100)

    # Close button
    close_button = tk.Button(info_window, text="Thanks!", command=info_window.destroy)
    close_button.pack(side=tk.RIGHT, padx=100) 

    info_window.mainloop()


if __name__ == "__main__":
    show_info_window()
