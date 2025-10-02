import time
import sys
import os
from pathlib import Path

try:
    import pygame
    from pygame import mixer
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

from .config import PROJECT_ROOT


# Initialize pygame mixer for sound effects
if PYGAME_AVAILABLE:
    try:
        mixer.init()
    except pygame.error:
        PYGAME_AVAILABLE = False

# Sound effect file paths
SOUND_DIR = PROJECT_ROOT / "data" / "sounds"
KEYPRESS_SOUND = SOUND_DIR / "keypress.wav"
BURN_SOUND = SOUND_DIR / "burn.wav"      # For high difficulty
SAVAGE_SOUND = SOUND_DIR / "savage.wav"  # For medium high difficulty
WIT_SOUND = SOUND_DIR / "wit.wav"        # For medium difficulty
CHARM_SOUND = SOUND_DIR / "charm.wav"    # For low difficulty
POLITICS_SOUND = SOUND_DIR / "politics.wav"        # For politics category
PICKUP_SOUND = SOUND_DIR / "pickup.wav"            # For pickup lines category
MARRIAGE_SOUND = SOUND_DIR / "marriage.wav"        # For marriage category
EDUCATION_SOUND = SOUND_DIR / "education.wav"      # For education category
PERSONAL_SOUND = SOUND_DIR / "personal.wav"        # For personal category
RELATIONSHIP_SOUND = SOUND_DIR / "relationship.wav" # For relationship category

# Preload sound effects if available
keypad_sound = None
burn_sound = None
savage_sound = None
wit_sound = None
charm_sound = None
politics_sound = None
pickup_sound = None
marriage_sound = None
education_sound = None
personal_sound = None
relationship_sound = None
wisdom_sound = None

if PYGAME_AVAILABLE:  # TODO: Download and set suitable sound for each category and difficulty level.
    if KEYPRESS_SOUND.exists():
        keypad_sound = mixer.Sound(str(KEYPRESS_SOUND))
    if BURN_SOUND.exists():
        burn_sound = mixer.Sound(str(BURN_SOUND))
    if SAVAGE_SOUND.exists():
        savage_sound = mixer.Sound(str(SAVAGE_SOUND))
    if WIT_SOUND.exists():
        wit_sound = mixer.Sound(str(WIT_SOUND))
    if CHARM_SOUND.exists():
        charm_sound = mixer.Sound(str(CHARM_SOUND))
    if POLITICS_SOUND.exists():
        politics_sound = mixer.Sound(str(POLITICS_SOUND))
    if PICKUP_SOUND.exists():
        pickup_sound = mixer.Sound(str(PICKUP_SOUND))
    if MARRIAGE_SOUND.exists():
        marriage_sound = mixer.Sound(str(MARRIAGE_SOUND))
    if EDUCATION_SOUND.exists():
        education_sound = mixer.Sound(str(EDUCATION_SOUND))
    if PERSONAL_SOUND.exists():
        personal_sound = mixer.Sound(str(PERSONAL_SOUND))
        wisdom_sound = mixer.Sound(str(PERSONAL_SOUND))  # Share with this sound for now, we have to set all this later.
    if RELATIONSHIP_SOUND.exists():
        relationship_sound = mixer.Sound(str(RELATIONSHIP_SOUND))


def play_sound(sound_obj, volume=0.3):
    """Play a sound effect if available"""
    if PYGAME_AVAILABLE and sound_obj:
        try:
            sound_obj.set_volume(volume)
            sound_obj.play()
        except Exception:
            # If there's an error playing the sound, continue without sound
            pass


def typewriter_effect(text, delay=0.05, end_with_newline=True, sound_enabled=True):
    """Simulate typewriter effect - each character appears one by one with optional sound"""
    for char in text:
        print(char, end="", flush=True)

        if sound_enabled and keypad_sound:
            play_sound(keypad_sound)

        time.sleep(delay)
    if end_with_newline:
        print()


def typing_with_pauses(text, delay=0.05, pause_chars=",.?!;:", sound_enabled=True):
    """Typewriter effect with dramatic pauses on punctuation with optional sound"""
    for char in text:
        print(char, end="", flush=True)

        if sound_enabled and keypad_sound:
            play_sound(keypad_sound)

        if char in pause_chars:
            time.sleep(delay * 10)  # Longer pause for drama
        else:
            time.sleep(delay)
    print()


def dramatic_pause(seconds):
    """Standard dramatic pause with dots"""
    for i in range(int(seconds)):
        print(".", end="", flush=True)
        time.sleep(1)
    print()
