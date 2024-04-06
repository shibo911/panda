# Importing Required Modules & libraries
from tkinter import *
import pygame
import os

# Defining MusicPlayer Class
class MusicPlayer:

  # Defining Constructor
  def __init__(self, root):
    self.root = root
    # Title of the window
    self.root.title("Music Player")
    # Window Geometry
    self.root.geometry("1000x200+200+200")
    # Initiating Pygame
    pygame.init()
    # Initiating Pygame Mixer
    pygame.mixer.init()
    # Declaring track Variable
    self.track = StringVar()
    # Declaring Status Variable
    self.status = StringVar()

    self.is_playing = False

    # Creating Track Frame for Song label & status label
    trackframe = LabelFrame(self.root, text="Song Track", font=("times new roman", 15, "bold"), bg="grey", fg="white",
                            bd=5, relief=GROOVE)
    trackframe.place(x=0, y=0, width=600, height=100)
    # Inserting Song Track Label
    songtrack = Label(trackframe, textvariable=self.track, width=20, font=("times new roman", 24, "bold"), bg="grey",
                      fg="gold").grid(row=0, column=0, padx=10, pady=5)
    # Inserting Status Label
    trackstatus = Label(trackframe, textvariable=self.status, font=("times new roman", 24, "bold"), bg="grey",
                        fg="gold").grid(row=0, column=1, padx=10, pady=5)

    # Creating Button Frame
    buttonframe = LabelFrame(self.root, text="Control Panel", font=("times new roman", 15, "bold"), bg="grey",
                             fg="white", bd=5, relief=GROOVE)
    buttonframe.place(x=0, y=100, width=600, height=100)
    # Inserting Play Button
    self.play_pause_button = Button(buttonframe,
                                     text="PLAY",
                                     command=self.toggle_play_pause,
                                     width=6,
                                     height=1,
                                     font=("times new roman", 16, "bold"),
                                     fg="navyblue",
                                     bg="gold"
                                     )
    self.play_pause_button.grid(row=0, column=0, padx=10, pady=5)

    # Creating Playlist Frame
    songsframe = LabelFrame(self.root, text="Song Playlist", font=("times new roman", 15, "bold"), bg="grey",
                            fg="white", bd=5, relief=GROOVE)
    songsframe.place(x=600, y=0, width=400, height=200)
    # Inserting scrollbar
    scrol_y = Scrollbar(songsframe, orient=VERTICAL)
    # Inserting Playlist listbox
    self.playlist = Listbox(songsframe, yscrollcommand=scrol_y.set, selectbackground="gold", selectmode=SINGLE,
                            font=("times new roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=GROOVE)
    # Applying Scrollbar to listbox
    scrol_y.pack(side=RIGHT, fill=Y)
    scrol_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=BOTH)
    # Changing Directory for fetching Songs
    os.chdir("LazyDays")
    # Fetching Songs
    songtracks = os.listdir()
    # Inserting Songs into Playlist
    for track in songtracks:
      self.playlist.insert(END, track)

  # Defining Play Song Function
  def playsong(self):
    # Displaying Selected Song title
    self.track.set(self.playlist.get(ACTIVE))
    # Displaying Status
    self.status.set("-Playing")
    # Loading Selected Song
    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    # Playing Selected Song
    pygame.mixer.music.play()

  def stopsong(self):
    # Displaying Status
    self.status.set("-Stopped")
    # Stopped Song
    pygame.mixer.music.stop()

  def pausesong(self):
    # Displaying Status
    self.status.set("-Paused")
    # Paused Song
    pygame.mixer.music.pause()

  def unpausesong(self):
    # Displaying Status
    self.status.set("-Playing")
    # Playing back Song
    pygame.mixer.music.unpause()

  def toggle_play_pause(self):
    if self.is_playing:
      self.pausesong()
      self.play_pause_button.config(text="PLAY")  # Update button text
    else:
      self.playsong()
      self.play_pause_button.config(text="PAUSE")  # Update button text
    self.is_playing = not self.is_playing  # Toggle the state

def start_music_player():
    # Creating TK Container
    root = Tk()
    # Passing Root to MusicPlayer Class
    MusicPlayer(root)
    # Root Window Looping
    root.mainloop()
