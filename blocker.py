import tkinter as tk
import tkinter.ttk as ttk

# Function to filter blue light based on intensity
def filter_blue_light(intensity):
    # Convert intensity to a float
    intensity = float(intensity)
    # Convert intensity to a value between 0 and 255
    blue_intensity = int(255 * (1 - intensity))
    # Set the screen color based on blue intensity
    screen_color = "#{:02x}{:02x}{:02x}".format(255, 255, blue_intensity)
    root.config(bg=screen_color)

# Create tkinter application window
root = tk.Tk()
root.title("Blue Light Filter")

# Create a frame to contain widgets
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, padx=10, pady=10)

# Create a label for the slider
label = ttk.Label(frame, text="Adjust Blue Light Intensity")
label.grid(row=0, column=0, columnspan=2, pady=5)

# Create a scale widget for adjusting blue light intensity
scale = ttk.Scale(frame, from_=0, to=1, orient="horizontal", command=filter_blue_light)
scale.grid(row=1, column=0, columnspan=2, pady=5)

# Set initial value for the scale
scale.set(0.5)

# Run the tkinter event loop
root.mainloop()
