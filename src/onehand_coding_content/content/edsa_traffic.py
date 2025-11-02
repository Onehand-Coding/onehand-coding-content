import time
import random

from ..config import LINE_LENGTH
from ..sounds import play_with_wait, EVIL_GIGGLE
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause

def travel_edsa(destination, distance_km, traffic_reasons, contemplations):
    """
    Simulates the EDSA experience, with a random excuse generator
    and a wide range of existential crises.
    """

    print("\n" + "="*LINE_LENGTH)
    typewriter_effect("EDSA TRAFFIC SIMULTOR 🚦")
    print("="*LINE_LENGTH)
    dramatic_pause(2)

    typing_with_pauses(f"🚗 Starting journey to {destination} ({distance_km}km). Brace yourself.")
    typing_with_pauses("Current Road: EDSA (Endless Despair and Suffering Avenue)")

    distance_traveled = 0
    patience_level = 100
    start_time = time.time()

    while distance_traveled < distance_km:
        move = random.uniform(0.001, 0.05)
        distance_traveled += move
        patience_level -= 1

        # A wild traffic event appears!
        if random.randint(1, 10) == 5:
            # Randomly select a reason from the list
            reason = random.choice(traffic_reasons)
            typing_with_pauses(f"- Sudden stop! Reason: {reason}")
            dramatic_pause(2)
            patience_level -= 5

        # Time for some deep thoughts
        if patience_level < 50 and random.randint(1, 5) == 1:
            # Randomly select a thought from the list
            thought = random.choice(contemplations)
            typing_with_pauses(f"- Traveled {distance_traveled:.3f}km. Contemplation: {thought}")

        if patience_level <= 0:
            typing_with_pauses("\n--- PATIENCE DEPLETED ---")
            typing_with_pauses("You've abandoned the car. The city has won this round.")
            return

        dramatic_pause(1)

    end_time = time.time()
    total_time_seconds = end_time - start_time
    total_time_hours = total_time_seconds / 3600

    typing_with_pauses(f"\n🎉 SURVIVED! Arrived at {destination}! 🎉")
    typing_with_pauses(f"Total time in purgatory: {total_time_hours:.2f} hours (simulated).")

# --- Lists of Misery and Wonder ---

# List of classic Manila traffic excuses
classic_traffic_reasons = [
    "Bus loading/unloading in the middle of the road.",
    "VIP convoy passing. Of course.",
    "Motorcycle swerving like it's a video game.",
    "A minor fender-bender blocking two lanes.",
    "Mysterious collective slowdown for no reason at all.",
    "Someone changing a flat tire on the fast lane.",
    "A group of people crossing where there's an overpass 10 meters away."
]

# Deep thoughts while barely moving
commuter_contemplations = [
    "Sana nag-bike na lang ako.",
    "Sana nag MRT na lang ako..Puyat kasi.",
    "I wonder how many hours of my life I've spent on this exact spot.",
    "What if I quit my job and became a farmer in the province?",
    "Did I remember to turn off the aircon before leaving?",
    "Maybe this is a sign I should learn to work from home permanently.",
    "Is this what purgatory feels like?"
]


def main():
    """Edsa Traffic Simulator Entry point."""
    travel_edsa("Megamall", 8, classic_traffic_reasons, commuter_contemplations)
    play_with_wait(EVIL_GIGGLE)


if __name__ == '__main__':
    main()
