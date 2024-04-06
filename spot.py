import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tkinter as tk

# Spotify Developer Credentials
client_id = '5c34ad62d3af42d395e93f6f3bc70839'
client_secret = 'dfe3f7f0e77e455baed7456af9d701dc'
redirect_uri = 'google.com'

# Spotify scopes for authorization
scope = "user-read-playback-state,user-modify-playback-state"

# Create Spotify object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

# Create Tkinter window
root = tk.Tk()
root.title("Spotify Player")

# Function to play music
def play_music():
    sp.start_playback()

# Function to pause music
def pause_music():
    sp.pause_playback()

# Play button
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Pause button
pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack()

# Run the Tkinter event loop
root.mainloop()
