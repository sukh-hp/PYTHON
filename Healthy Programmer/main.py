import os
from tkinter import Tk, Frame, Label, Listbox, Button, filedialog, Scale, HORIZONTAL
import pygame
import threading
from PIL import ImageTk, Image
from mutagen import File

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x600")

        # Create a label to display the currently playing song
        self.current_song_label = Label(self.root, text="No song selected", font=("Helvetica", 12))
        self.current_song_label.pack(pady=10)

        # Create a listbox to display the songs
        self.listbox = Listbox(self.root, font=("Helvetica", 12), selectbackground="#a6a6a6")
        self.listbox.pack(pady=10, fill="both", expand=True)

        # Create buttons for playback controls
        self.play_button = Button(self.root, text="Play", font=("Helvetica", 12), command=self.play_song)
        self.pause_button = Button(self.root, text="Pause", font=("Helvetica", 12), command=self.pause_song)
        self.stop_button = Button(self.root, text="Stop", font=("Helvetica", 12), command=self.stop_song)
        self.seek_slider = Scale(self.root, from_=0, to=100, orient=HORIZONTAL, command=self.seek_song)

        self.play_button.pack(side="left", padx=10)
        self.pause_button.pack(side="left", padx=10)
        self.stop_button.pack(side="left", padx=10)
        self.seek_slider.pack(pady=10)

        # Create a thread for continuous playback monitoring
        self.playback_thread = threading.Thread(target=self.check_playback)

        # Create a mixer object
        pygame.mixer.init()

    def add_songs_from_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            songs = []
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".mp3"):
                    songs.append(os.path.join(folder_path, file_name))
            self.update_song_list(songs)

    def update_song_list(self, songs):
        self.listbox.delete(0, "end")
        for song in songs:
            self.listbox.insert("end", song)

    def play_song(self):
        selected_song = self.listbox.get("active")
        if selected_song:
            pygame.mixer.music.load(selected_song)
            pygame.mixer.music.play()
            self.current_song_label.config(text=f"Now playing: {selected_song}")
            self.playback_thread.start()
            self.display_album_artwork(selected_song)

    def pause_song(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def stop_song(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

    def seek_song(self, event):
        if pygame.mixer.music.get_busy():
            seek_pos = int(self.seek_slider.get())
            song_length = pygame.mixer.music.get_length()
            seek_time = (seek_pos / 100) * song_length
            pygame.mixer.music.set_pos(seek_time)

    def check_playback(self):
        while pygame.mixer.music.get_busy():
            pass
        self.current_song_label.config(text="No song selected")

    def display_album_artwork(self, song_path):
        audio_file = File(song_path)
        if "APIC:" in audio_file.tags.keys():
            artwork_data = audio_file.tags["APIC:"].data
            artwork_image = Image.open(BytesIO(artwork_data))
            artwork_image = artwork_image.resize((200, 200), Image.ANTIALIAS)
            self.album_art_label.config(image=ImageTk.PhotoImage(artwork_image))
        else:
            self.album_art_label.config(image="")

# Create the Tkinter window
root = Tk()

# Create the music player
music_player = MusicPlayer(root)

# Create a button to add songs from a folder
add_folder_button = Button(root, text="Add Folder", font=("Helvetica", 12), command=music_player.add_songs_from_folder)
add_folder_button.pack(pady=10)

# Create a label to display album artwork
music_player.album_art_label = Label(root)
music_player.album_art_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()