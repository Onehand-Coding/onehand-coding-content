import time
import sys
import os
from pathlib import Path

from .sounds import play_sound, KEYPRESS_SOUND


def typewriter_effect(text, delay=0.05, end_with_newline=True):
    """Simulate typewriter effect - each character appears one by one with sound"""
    for char in text:
        print(char, end="", flush=True)
        play_sound(KEYPRESS_SOUND)
        time.sleep(delay)

    if end_with_newline:
        print()


def typing_with_pauses(text, delay=0.05, pause_chars=",.?!;:'"):
    """Typewriter effect with dramatic pauses on punctuation with sound"""
    for char in text:
        print(char, end="", flush=True)
        play_sound(KEYPRESS_SOUND)

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
