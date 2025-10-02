from pathlib import Path

try:
    import pygame
    from pygame import mixer
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

from .config import PROJECT_ROOT, SOUND_DIR


# Initialize pygame mixer for sound effects
if PYGAME_AVAILABLE:
    try:
        mixer.init()
    except pygame.error:
        PYGAME_AVAILABLE = False

# Sound effect file paths, currently uses random sounds avaiable locally lets improve it in the future.
KEYPRESS_SOUND = SOUND_DIR / "keypress.wav"
BURN_SOUND = SOUND_DIR / "burn.wav"
SAVAGE_SOUND = SOUND_DIR / "savage.wav"
WIT_SOUND = SOUND_DIR / "wit.wav"
CHARM_SOUND = SOUND_DIR / "charm.wav"
POLITICS_SOUND = SOUND_DIR / "politics.wav"
PICKUP_SOUND = SOUND_DIR / "pickup.wav"
NEVER_BACKDOWN = SOUND_DIR / "never-backdown.wav"
EDUCATION_SOUND = SOUND_DIR / "education.wav"
PERSONAL_SOUND = SOUND_DIR / "personal.wav"
RELATIONSHIP_SOUND = SOUND_DIR / "relationship.wav"


def play_sound(sound_file, volume=0.3):
    """Play a sound effect if available"""
    if sound_file.exists() and PYGAME_AVAILABLE:
        sound_obj = mixer.Sound(str(sound_file))
        try:
            sound_obj.set_volume(volume)
            sound_obj.play()
        except Exception:
            # If there's an error playing the sound, continue without sound
            pass
