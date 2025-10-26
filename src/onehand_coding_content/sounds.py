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
SABOG_SOUND = SOUND_DIR / "akoy-sabog-na.wav"
CORRUPTION_1 = SOUND_DIR / "corruption-1.wav"
CORRUPTION_2 = SOUND_DIR / "corruption-2.wav"
CORRUPTION_3 = SOUND_DIR / "corruption-3.wav"
DELAY = SOUND_DIR / "delay.wav"
NO_PROMISES = SOUND_DIR / "no-promises.wav"
HERO = SOUND_DIR / "hero.wav"


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


def play_with_wait(sound_file, wait_time=100, volume=0.3):
    """Play sound and wait for it to finish."""
    if sound_file.exists() and PYGAME_AVAILABLE:
        sound_obj = mixer.Sound(str(sound_file))
        try:
            sound_obj.set_volume(volume)
            sound_obj.play()
        except Exception:
            # If there's an error playing the sound, continue without sound
            pass

    # Lets wait for the sound to finish playing.
    while mixer.get_busy():
            pygame.time.wait(wait_time)
