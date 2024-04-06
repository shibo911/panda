import tkinter as tk
from PIL import Image, ImageTk

class Overlay(tk.Tk):
    def __init__(self, *a, **kw):
        tk.Tk.__init__(self, *a, **kw)
        self._set_window_attrs()
        self.set_transparency()

    def _set_window_attrs(self):
        self.title("Overlay")
        self.geometry("200x200+100+100")
        self.focus_force()
        self.wm_attributes("-topmost", True)
        self.overrideredirect(True)
        self.offset_x, self.offset_y = None, None
        self.bind("<Button-1>", self.on_mouse_click)
        self.bind("<B1-Motion>", self.on_mouse_drag)
        self.bind("<ButtonRelease-1>", self.on_mouse_rel)

    def set_transparency(self):
        self.canvas = tk.Canvas(self, bg="black")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.config(highlightthickness=0)

        # Load the image
        image = Image.open("panda.jpg")
        self.photo = ImageTk.PhotoImage(image)

        # Add the image to the canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor='nw')

        self.wm_attributes("-transparentcolor", "black")

    def on_mouse_click(self, event):
        self.offset_x = self.winfo_pointerx() - self.winfo_rootx()
        self.offset_y = self.winfo_pointery() - self.winfo_rooty()

    def on_mouse_drag(self, event):
        if None not in (self.offset_x, self.offset_y):
            new_window_x = self.winfo_pointerx() - self.offset_x
            new_window_y = self.winfo_pointery() - self.offset_y
            self.geometry("+%d+%d" % (new_window_x, new_window_y))

    def on_mouse_rel(self, event):
        self.offset_x, self.offset_y = None, None

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    Overlay().run()
