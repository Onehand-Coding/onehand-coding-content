"""
Philippine Justice System Simulator
October 24, 2025: A Day of Reckoning... or Recycling?

Napoles Pork Barrel (2013) vs Flood Control Scam (2025)
Same script. Different actors. Same ending?

₱10 BILLION stolen (Pork Barrel)
₱118+ BILLION stolen (Flood Control)

This is not a bug. This is a FEATURE.
"""

import time
from datetime import datetime

from ..sounds import play_with_wait, CORRUPTION_3, CORRUPTION_2
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause


class JusticeSystemSimulator:
    """
    Philippine Justice System: Pattern Recognition Edition
    Analyzing: Napoles (2013) vs Flood Control (2025)
    """

    def __init__(self):
        self.current_date = datetime(2025, 10, 24)

        # Napoles Pork Barrel Scam
        self.napoles_scandal = {
            "year_exposed": 2013,
            "amount_stolen": 10_000_000_000,  # ₱10 Billion
            "years_elapsed": 12,
            "convictions_today": 0,  # Acquitted today
            "big_fish_jailed": 0,
            "mastermind_convicted": True,  # Napoles convicted in OTHER cases
            "masterminds_acquitted_today": ["JPE Enrile", "Gigi Reyes", "Napoles"]
        }

        # Current Flood Control Scam
        self.flood_scandal = {
            "year_exposed": 2025,
            "amount_stolen": 118_500_000_000,  # ₱118.5 Billion (so far)
            "ghost_projects": 421,  # Out of 8,000 inspected
            "years_elapsed": 0,
            "investigation_status": "Ongoing",
            "hearings": "Closed door",  # KEY ISSUE
            "protected_witnesses": 5,
            "senators_implicated": 6,
            "big_fish_jailed": 0,
            "probable_outcome": "TBD (but we know)"
        }

    def display_header(self):
        """Display shocking header"""
        print("\n" + "="*70)
        typewriter_effect("⚖️  PHILIPPINE JUSTICE SYSTEM: PATTERN ANALYSIS")
        print("="*70)
        print()
        typing_with_pauses(f"📅 Date: {self.current_date.strftime('%B %d, %Y')}")
        typing_with_pauses("🔔 Breaking News: Enrile, Napoles, Reyes ACQUITTED in Pork Barrel Case")
        dramatic_pause(2)
        print()

    def compare_scandals(self):
        """Side-by-side comparison"""
        print("\n" + "="*70)
        typewriter_effect("📊 TALE OF TWO CORRUPTION SCANDALS")
        print("="*70)
        dramatic_pause(1)

        typing_with_pauses("\n🏛️  PORK BARREL SCAM (2013)")
        print("-"*70)
        time.sleep(0.5)
        typing_with_pauses(f"   💰 Amount Stolen: ₱{self.napoles_scandal['amount_stolen']:,.2f}")
        time.sleep(0.5)
        typing_with_pauses(f"   📅 Years Since Exposed: {self.napoles_scandal['years_elapsed']} years")
        time.sleep(0.5)
        typing_with_pauses(f"   👨‍⚖️ Big Fish Convicted: {self.napoles_scandal['big_fish_jailed']}")
        time.sleep(0.5)
        typing_with_pauses("   ✅ Napoles Convicted: Yes (in OTHER cases)")
        time.sleep(0.5)
        typing_with_pauses(f"   ❌ Acquitted TODAY: {', '.join(self.napoles_scandal['masterminds_acquitted_today'])}")
        dramatic_pause(2)

        typing_with_pauses("\n\n🌊 FLOOD CONTROL SCAM (2025)")
        print("-"*70)
        time.sleep(0.5)
        typing_with_pauses(f"   💰 Amount Stolen: ₱{self.flood_scandal['amount_stolen']:,.2f}")
        time.sleep(0.5)
        typing_with_pauses(f"   📅 Years Since Exposed: {self.flood_scandal['years_elapsed']} years")
        time.sleep(0.5)
        typing_with_pauses(f"   🚫 Ghost Projects Found: {self.flood_scandal['ghost_projects']} (so far)")
        time.sleep(0.5)
        typing_with_pauses(f"   🔒 Hearings Status: {self.flood_scandal['hearings']}")
        time.sleep(0.5)
        typing_with_pauses(f"   🎯 Senators Implicated: {self.flood_scandal['senators_implicated']}")
        time.sleep(0.5)
        typing_with_pauses(f"   👨‍⚖️ Big Fish Convicted: {self.flood_scandal['big_fish_jailed']}")
        dramatic_pause(2)

        # The shocking comparison
        typing_with_pauses("\n\n📈 MAGNITUDE COMPARISON:")
        print("-"*70)
        time.sleep(1)
        multiplier = self.flood_scandal['amount_stolen'] / self.napoles_scandal['amount_stolen']
        typing_with_pauses(f"   Flood Control Scam is {multiplier:.1f}x BIGGER than Pork Barrel")
        dramatic_pause(2)
        typing_with_pauses("   Yet... we're seeing the same pattern unfold.")
        dramatic_pause(2)

    def timeline_of_justice(self):
        """Show how long justice takes"""
        print("\n\n" + "="*70)
        typewriter_effect("⏰ PORK BARREL SCAM: TIMELINE OF 'JUSTICE'")
        print("="*70)
        dramatic_pause(1)

        timeline = [
            ("2013", "Scandal exposed by whistleblowers", "💣"),
            ("2014", "Charges filed against senators", "⚖️"),
            ("2014-2025", "11 years of legal proceedings", "⏳"),
            ("2024", "Acquitted of plunder charges", "❌"),
            ("Oct 24, 2025", "Acquitted of 15 graft charges", "❌"),
            ("Result", "12 years. ₱10B stolen. Zero big fish jailed.", "🤡")
        ]

        for year, event, emoji in timeline:
            typing_with_pauses(f"\n   {emoji} {year}: {event}")
            time.sleep(1.5)

        dramatic_pause(2)

        typing_with_pauses("\n   🔮 Reasons for acquittal:")
        time.sleep(0.8)
        typing_with_pauses("      • 'Prosecution failed to prove beyond reasonable doubt'")
        time.sleep(0.8)
        typing_with_pauses("      • 'Endorsement letters were merely recommendatory'")
        time.sleep(0.8)
        typing_with_pauses("      • 'No proof of kickbacks'")
        time.sleep(0.8)
        typing_with_pauses("      • 'Whistleblower testimony unreliable'")
        dramatic_pause(2)

        typing_with_pauses("\n   💭 Translation: 'May pera, may justice.' 💸")
        dramatic_pause(2)

    def predict_flood_scandal_future(self):
        """Predict what will happen to flood control scam"""
        print("\n\n" + "="*70)
        typewriter_effect("🔮 FLOOD CONTROL SCAM: PREDICTED TIMELINE")
        print("="*70)
        dramatic_pause(2)

        typing_with_pauses("\n⚠️  Based on historical patterns...")
        dramatic_pause(2)

        # Calculate predicted dates
        start_year = 2025
        predictions = [
            (start_year, "Scandal exposed (public outrage)", "✅", 100),
            (start_year, "Independent Commission created", "✅", 100),
            (start_year, "Hearings: CLOSED DOOR (no transparency)", "✅", 100),
            (start_year + 1, "Media coverage fades", "🔄", 95),
            (start_year + 2, "Some small fries charged", "🔄", 90),
            (start_year + 4, "First trials begin", "🔄", 85),
            (start_year + 8, "Small contractors convicted", "🔄", 70),
            (start_year + 10, "Big fish acquitted (insufficient evidence)", "🔄", 95),
            (start_year + 12, "₱118B unaccounted. Zero senators jailed.", "🔄", 99),
            (start_year + 13, "New corruption scandal emerges", "🔄", 100)
        ]

        for year, event, status, probability in predictions:
            typing_with_pauses(f"\n   {status} {year}: {event}")
            if probability < 100:
                typing_with_pauses(f"      Probability: {probability}%")
            time.sleep(1.5)

        dramatic_pause(3)

        typing_with_pauses("\n\n   🎯 Expected Outcome:")
        time.sleep(1)
        typing_with_pauses("      ₱118.5 BILLION stolen")
        time.sleep(1)
        typing_with_pauses("      421+ ghost projects")
        time.sleep(1)
        typing_with_pauses("      6 senators implicated")
        time.sleep(1)
        typing_with_pauses("      Result: ZERO big fish jailed")
        dramatic_pause(2)

        typing_with_pauses("\n   💬 'History doesn't repeat, but it rhymes.' - Mark Twain")
        time.sleep(1)
        typing_with_pauses("   🤡 'In PH, history copy-pastes.' - Citizens")
        dramatic_pause(2)

    def the_transparency_problem(self):
        """Highlight the transparency issue"""
        print("\n\n" + "="*70)
        typewriter_effect("👁️  THE TRANSPARENCY PROBLEM")
        print("="*70)
        dramatic_pause(2)

        typing_with_pauses("\n🚨 CRITICAL DIFFERENCE: CLOSED DOOR HEARINGS")
        time.sleep(1)

        typing_with_pauses("\n   ❌ Independent Commission Investigation (2025):")
        time.sleep(0.8)
        typing_with_pauses("      • Hearings: CLOSED DOOR")
        time.sleep(0.8)
        typing_with_pauses("      • Public access: DENIED")
        time.sleep(0.8)
        typing_with_pauses("      • Media coverage: Press releases only")
        time.sleep(0.8)
        typing_with_pauses("      • Livestream: NOT ALLOWED")
        dramatic_pause(2)

        typing_with_pauses("\n   💬 What people are saying:")
        time.sleep(1)
        typing_with_pauses("      Justice Carpio: 'People will lose faith in the ICI'")
        time.sleep(1)
        typing_with_pauses("      Sen. Pangilinan: 'Decision is ill-advised, open it!'")
        time.sleep(1)
        typing_with_pauses("      Agot Isidro: 'Taxpayers fund this, we should see it'")
        time.sleep(1)
        typing_with_pauses("      Netizens: 'Kung walang tinatago, bakit takot ipakita?'")
        dramatic_pause(2)

        typing_with_pauses("\n   🤔 ICI's Response: 'Ayaw namin ng trial by publicity'")
        time.sleep(1)
        typing_with_pauses("   💭 Translation: 'Ayaw namin ng accountability' 🙈")
        dramatic_pause(3)

    def existential_questions(self):
        """Address the deep questions"""
        print("\n\n" + "="*70)
        typewriter_effect("💭 THE QUESTIONS THAT HAUNT US")
        print("="*70)
        dramatic_pause(2)

        questions = [
            ("Is there still hope for the Philippines?",
             "The fact that you're asking means there's still hope.\nThe day we stop asking is the day hope truly dies."),

            ("Is this what our heroes wanted?",
             "Rizal wrote about the same greed 140 years ago.\nBonifacio fought against this same system.\nThey'd be disappointed, but not surprised."),

            ("Will this generation turn a blind eye?",
             "Some will. Some won't.\nYou're reading this. You're not blind.\nThe question is: What will YOU do?"),

            ("How do we trust the government now?",
             "Trust is earned, not given.\n₱10B (2013) → Zero accountability\n₱118B (2025) → Same pattern\nTrust? We verify. Then verify again."),

            ("What are we supposed to do?",
             "1. Remember these patterns\n2. Vote with eyes WIDE open\n3. Demand transparency (PUBLIC hearings)\n4. Support accountability measures\n5. Never. Stop. Asking. Questions.")
        ]

        for i, (question, answer) in enumerate(questions, 1):
            typing_with_pauses(f"\n   ❓ Question {i}: {question}")
            dramatic_pause(2)
            typing_with_pauses("   💡 Answer:")
            for line in answer.split('\n'):
                typing_with_pauses(f"      {line}")
                time.sleep(1)
            dramatic_pause(2)

    def the_code_speaks(self):
        """The code that represents our reality"""
        print("\n\n" + "="*70)
        typewriter_effect("💻 THE CODE THAT DEFINES US")
        print("="*70)
        dramatic_pause(1)

        code = '''
def philippine_justice_system(scandal):
    """
    The algorithm that never changes
    """
    years = 0
    public_outrage = 100

    # Initial response
    print("Creating independent commission...")

    # Make it look like action
    while years < 12:
        public_outrage -= 8  # Fades over time
        years += 1

        if public_outrage < 20:
            print("Public forgot. Time to acquit.")
            break

    # The inevitable outcome
    big_fish_jailed = 0
    money_recovered = 0

    return {
        "justice": False,
        "accountability": None,
        "big_fish_jailed": big_fish_jailed,
        "pattern": "Will repeat"
    }


# Real-world execution
pork_barrel_result = philippine_justice_system("Napoles")
# Output: {'justice': False, 'big_fish_jailed': 0, 'pattern': 'Will repeat'}

flood_control_result = philippine_justice_system("Flood Control")
# Output: {'justice': False, 'big_fish_jailed': 0, 'pattern': 'Will repeat'}

# while corruption_exists:
#     taxpayers.suffer()
#     politicians.profit()
#     system.continues()
#     hope -= 1  # But never reaches zero. That's our superpower.
'''

        for line in code.split('\n'):
            typing_with_pauses(line)
            time.sleep(0.3)

        dramatic_pause(3)

    def final_message(self):
        """The message of resolve"""
        print("\n\n" + "="*70)
        typewriter_effect("🔥 TO THE CURRENT GENERATION", delay=0.04)
        print("="*70)
        dramatic_pause(2)

        typing_with_pauses("\nOctober 24, 2025.")
        time.sleep(1)
        typing_with_pauses("12 years after the Pork Barrel Scam was exposed.")
        time.sleep(1)
        typing_with_pauses("Enrile, Napoles, Reyes: ACQUITTED.")
        dramatic_pause(2)

        typing_with_pauses("\nMeanwhile, ₱118.5 BILLION is missing.")
        time.sleep(1)
        typing_with_pauses("421 ghost flood control projects.")
        time.sleep(1)
        typing_with_pauses("And the hearings? CLOSED DOOR.")
        dramatic_pause(3)

        typing_with_pauses("\n\n   🔥 THIS IS NOT ACCEPTABLE.")
        dramatic_pause(2)

        typing_with_pauses("\n   ✊ What we demand:")
        time.sleep(1)
        typing_with_pauses("      1. PUBLIC hearings (livestreamed)")
        time.sleep(0.8)
        typing_with_pauses("      2. REAL accountability (jail time for big fish)")
        time.sleep(0.8)
        typing_with_pauses("      3. TRANSPARENT investigations")
        time.sleep(0.8)
        typing_with_pauses("      4. RECOVERED funds (return people's money)")
        time.sleep(0.8)
        typing_with_pauses("      5. SYSTEMIC change (break the pattern)")
        dramatic_pause(3)

        typing_with_pauses("\n\n   💪 Our heroes fought for freedom.")
        time.sleep(1.5)
        typing_with_pauses("   We fight for accountability.")
        dramatic_pause(2)

        typing_with_pauses("\n   🇵🇭 The pattern stops when WE stop accepting it.")
        dramatic_pause(2)

        print("\n" + "="*70)
        typing_with_pauses("'Ang hindi marunong lumingon sa pinanggalingan", delay=0.04)
        typing_with_pauses("ay hindi makararating sa paroroonan.'", delay=0.04)
        dramatic_pause(1)
        typing_with_pauses("\nWe've looked back. We see the pattern.", delay=0.04)
        time.sleep(1)
        typing_with_pauses("Now we change the destination.", delay=0.04)
        print("="*70)
        dramatic_pause(2)


def main():
    """Run the justice system simulator"""
    simulator = JusticeSystemSimulator()

    # Display header with today's news
    simulator.display_header()

    # Compare the two scandals
    simulator.compare_scandals()

    # Show the pork barrel timeline
    simulator.timeline_of_justice()

    # Predict flood control future
    simulator.predict_flood_scandal_future()

    # Highlight transparency problem
    simulator.the_transparency_problem()

    # Answer existential questions
    simulator.existential_questions()

    # Show the code
    simulator.the_code_speaks()

    # Final rallying message
    simulator.final_message()

    print()

    play_with_wait(CORRUPTION_2)

    play_with_wait(CORRUPTION_3)


if __name__ == "__main__":
    main()
