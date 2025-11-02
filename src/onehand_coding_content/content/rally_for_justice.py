import time
import random

from ..config import LINE_LENGTH
from ..sounds import play_with_wait, REVOLUTION
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause


class PinoyRally:
    def __init__(self):
        self.demands = [
            "Transparency sa lahat ng transactions",
            "Accountability hindi excuses",
            "Justice walang kapit",
            "Services hindi lip service",
            "Action hindi lang salita"
        ]

        self.politicians = ["Politician A", "Politician B", "Politician C", "All of them tbh"]

        # Hindi tayo sumusuporta sa kahit sino mang pontio pilato
        self.supported_politicians = []

    def check_politician_support(self):
        """Check kung may sinusuportahan tayong politician"""
        if len(self.supported_politicians) == 0:
            return "NEUTRAL MODE: Activated ✅"
        else:
            return "ERROR: Bias detected! 🚨"

    def rally_for_justice(self):
        print("\n" + "=" * LINE_LENGTH)
        typewriter_effect("🇵🇭 RALLY FOR JUSTICE INITIATED 🇵🇭")
        print("=" * LINE_LENGTH)

        # Verify na neutral tayo
        typing_with_pauses(f"Status: {self.check_politician_support()}")
        time.sleep(1)

        typing_with_pauses("\n📢 OUR DEMANDS (hindi request, DEMANDS!):")
        for i, demand in enumerate(self.demands, 1):
            typing_with_pauses(f"{i}. {demand}")
            time.sleep(0.8)

        typing_with_pauses("\n🎯 TARGET: Lahat ng may kapangyarihan")
        time.sleep(1)

        # Random check kung sino man nakaupo
        current_official = random.choice(self.politicians)
        typing_with_pauses(f"\n⚖️ Whoever you are '{current_official}', deliver or resign!")
        time.sleep(1.5)

        # The punchline
        typing_with_pauses("\n💡 REMINDER:")
        typing_with_pauses("   Our loyalty is to the COUNTRY,")
        typing_with_pauses("   not to any politician's bank account! 💸")
        time.sleep(2)

        return "Rally successful! Now back to work... 💪"

# Democratic participation functions
def voice_out():
    """Boses ng bayan function"""
    voices = [
        "Tama na ang korapsyon!",
        "Saan napunta ang pera namin?",
        "Trabaho hindi drama!",
        "Ginhawa hindi pahirap!"
    ]

    typing_with_pauses("\n🔊 VOICES FROM THE PEOPLE:")
    for voice in voices:
        typing_with_pauses(f"   👥 {voice}")
        time.sleep(1)

def calculate_tax_efficiency():
    """Calculate kung saan napupunta ang tax ng mga manggagawa."""
    tax_collected = 100  # 100% ng tax

    # Realistic breakdown (atleast?)
    actual_services = 30
    ghost_projects = 25
    legitimate_expenses = 20
    unknown_allocation = 25

    typing_with_pauses(f"\n💰 TAX BREAKDOWN CALCULATOR:")
    typing_with_pauses(f"   Actual Public Services: {actual_services}%")
    time.sleep(1)
    typing_with_pauses(f"   Ghost Projects: {ghost_projects}%")
    time.sleep(1)
    typing_with_pauses(f"   'Legitimate Expenses': {legitimate_expenses}%")
    time.sleep(1)
    typing_with_pauses(f"   Nasa kung saan: {unknown_allocation}%")
    time.sleep(2)

    if unknown_allocation > actual_services:
        typing_with_pauses("   ❌ EFFICIENCY: FAILED!")
        typing_with_pauses("   💡 SOLUTION: Rally na tayo! 📢")


def main():
    """Pinoy Rally Main Entry Point."""
    typing_with_pauses("\n🐍 Python Rally Script v1.0")
    typing_with_pauses("Developed by: Onehand-Coding")
    typing_with_pauses("Bug reports: Sa mga rally mismo!")
    print()

    # Initialize rally
    rally = PinoyRally()

    try:
        # Execute rally
        result = rally.rally_for_justice()

        # Add people's voices
        voice_out()

        # Show tax reality check
        calculate_tax_efficiency()

        typing_with_pauses(f"\n✅ {result}")
        typing_with_pauses("\n🇵🇭 Remember: Democracy is not a spectator sport!")
        typing_with_pauses("   Code responsibly, rally peacefully! 💻✊")

    except Exception as e:
        typing_with_pauses(f"Error: {e}")
        typing_with_pauses("But we continue fighting anyway! 💪")

    finally:
        typing_with_pauses("\n# I support")
        typing_with_pauses("# OnehandCoding PinoyProgrammer 🌟")

    play_with_wait(REVOLUTION)


if __name__ == "__main__":
    main()
