import time
import multiprocessing
from tkinter import Tk
from PIL import Image, ImageTk
from over import OverlayApp  # assuming your class is defined in overlay_app.py

def change_background(app, new_image_path):
    # Open the new image
    new_image = Image.open(new_image_path)

    # Convert the image to PhotoImage format
    new_photo_image = ImageTk.PhotoImage(new_image)

    # Update the background label with the new image
    app.background_label.config(image=new_photo_image)

    # Keep a reference to the new image to prevent it from being garbage collected
    app.background_label.image = new_photo_image

def timer_function(app):
    time.sleep(2)  # wait for 10 seconds
    change_background(app, "panda.jpg")  # change the background

if __name__ == "__main__":
    root = Tk()
    app = OverlayApp(root)
    p = multiprocessing.Process(target=timer_function, args=(app,))
    p.start()
    timer_function(app)
    root.mainloop()
