import pygame
import schedule
import time
# Initialize the mixer
pygame.mixer.init()

# Load the song into the mixer
song = pygame.mixer.Sound("Baapu.mp3")

# Set the volume of the song
song.set_volume(0.5)

# Play the song
# song.play()


def getdate():
    import datetime
    return datetime.datetime.now()


a = getdate()

def drink_water():
    return song.play(5)

drink_water()
