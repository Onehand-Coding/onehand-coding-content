import time
import sys
import random

from ..config import LINE_LENGTH
from ..sounds import play_with_wait, SABOG_SOUND
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause


def miriam_political_wisdom():
    """
    Present Miriam's classic line with proper dramatic timing
    """
    # The question - slower for emphasis
    typing_with_pauses("\n📝 QUESTION:")
    time.sleep(0.5)
    print()
    typing_with_pauses("What is the difference between corruption in the U.S. and corruption in the Philippines?")

    dramatic_pause(3)

    # The devastating answer
    typing_with_pauses("\n💡 ANSWER:")
    time.sleep(1)
    typing_with_pauses("\nIn the U.S. they go to jail.")
    time.sleep(2)  # Let it sink in
    typing_with_pauses("In the Philippines, they go to the U.S.!")

    # Final dramatic pause
    time.sleep(2)
    typing_with_pauses("\n--- MIRIAM DEFENSOR SANTIAGO🔥\n")


def interactive_reveal():
    """
    Interactive version where user presses enter to continue
    """
    typing_with_pauses("\n📝 QUESTION:")
    time.sleep(0.5)
    print()
    typing_with_pauses("What is the difference between corruption in the U.S. and corruption in the Philippines?")

    dramatic_pause(3)

    input("\nPress Enter...")
    print()

    # The devastating answer
    typing_with_pauses("\n💡 ANSWER:")
    time.sleep(1)
    typing_with_pauses("\nIn the U.S. they go to jail.")
    time.sleep(2)  # Let it sink in
    typing_with_pauses("In the Philippines, they go to the U.S.!")

    time.sleep(2)
    typing_with_pauses("\n--- MIRIAM DEFENSOR SANTIAGO🔥\n")


def main():
    """Main Entry Point."""
    print("\n" + "=" * LINE_LENGTH)
    typewriter_effect("MIRIAM PICKUP LINE")
    print("=" * LINE_LENGTH)
    dramatic_pause(2)

    if random.randint(0, 1) == 1:
        interactive_reveal()
    else:
        miriam_political_wisdom()

    play_with_wait(SABOG_SOUND)

    print()


if __name__ == "__main__":
    main()
