import time
import random

from ..config import LINE_LENGTH
from ..sounds import play_with_wait, DELAY
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause


class OmbudsmanOffice:
    def __init__(self):
        self.confidential_funds = 50_000_000  # 50M pesos
        self.corruption_cases_filed = 0
        self.corruption_cases_resolved = 0
        self.investigation_speed = "tortoise_mode"
        self.vip_protection_level = "maximum"

    def investigate_corruption(self, case_name):
        typing_with_pauses(f"🔍 Investigating: {case_name}")
        typing_with_pauses(f"💰 Using confidential funds: ₱{self.confidential_funds:,}")

        # Special handling for DPWH + Senator cases
        if "senator" in case_name.lower() or "dpwh" in case_name.lower():
            typing_with_pauses("⚠️  WARNING: VIP detected! Switching to delicate mode...")
            time.sleep(3)  # Extra time for "careful" handling

            vip_outcomes = [
                "Transferred to regular court (downgraded)",
                "Witness suddenly unavailable",
                "Documents mysteriously missing",
                "Investigation scope narrowed significantly"
            ]
            result = random.choice(vip_outcomes)
        else:
            # Simulate "thorough" investigation
            time.sleep(2)  # Emphasis on how slow it is

            investigation_outcomes = [
                "Case forwarded to Sandiganbayan",
                "Insufficient evidence (somehow)",
                "Official transferred to another position",
                "Under further review (indefinitely)"
            ]
            result = random.choice(investigation_outcomes)

        typing_with_pauses(f"📋 Result: {result}")

        # Reduce funds but corruption remains
        self.confidential_funds -= 1_000_000
        if "forwarded to Sandiganbayan" in result:
            self.corruption_cases_filed += 1

        return result


class PhilippineJudiciary:
    def __init__(self):
        self.pending_cases = 999999
        self.average_case_duration = "10-15 years"
        self.justice_delivery_status = "pending"

    def process_case(self, case_name):
        typing_with_pauses(f"\n⚖️ Sandiganbayan processing: {case_name}")

        # Simulate judicial process
        processes = [
            "Filing motion to dismiss",
            "Counter motion filed",
            "Motion to quash",
            "Preliminary investigation",
            "More preliminary investigation",
            "Postponement due to absent witness",
            "Another postponement",
            "Senator claims parliamentary immunity",
            "Case archived temporarily"
        ]

        for i, process in enumerate(processes):
            typing_with_pauses(f"📅 Year {i+1}: {process}")
            time.sleep(1)  # Each year passes slowly

        typing_with_pauses(f"⏰ Expected resolution: {self.average_case_duration}")
        typing_with_pauses("🎭 Plot twist: Key witness suddenly has amnesia")
        typing_with_pauses("📺 Breaking: Senator holds press conference about 'political persecution'")

        self.pending_cases += 1  # Ironic increment
        return "Justice delayed is justice denied"

# The Philippine Reality Check
def main():
    """Main Entry Point for Judicial process Simulation code."""
    print("\n" + "="*LINE_LENGTH)
    typewriter_effect("🇵🇭 PHILIPPINE ANTI-CORRUPTION SYSTEM v2025")
    print("="*LINE_LENGTH)
    dramatic_pause(2)

    ombudsman = OmbudsmanOffice()
    judiciary = PhilippineJudiciary()

    major_cases = [
        "Billion-peso infrastructure scam",
        "Ghost employees payroll",
        "Overpriced medical supplies",
        "Missing disaster relief funds"
    ]

    print("\n" + "="*LINE_LENGTH)
    typing_with_pauses("OMBUDSMAN INVESTIGATION PHASE")
    print("="*LINE_LENGTH)
    dramatic_pause(1)

    for case in major_cases:
        result = ombudsman.investigate_corruption(case)
        typing_with_pauses(f"Remaining confidential funds: ₱{ombudsman.confidential_funds:,}\n")
        time.sleep(1)

    print("\n" + "="*LINE_LENGTH)
    typing_with_pauses("JUDICIARY PROCESS PHASE")
    print("="*LINE_LENGTH)

    # Only process cases that were filed
    if ombudsman.corruption_cases_filed > 0:
        judiciary.process_case("The One Case That Made It")
    else:
        typing_with_pauses("📝 No cases to process. All were 'insufficient evidence'")

    print("\n" + "="*LINE_LENGTH)
    typing_with_pauses("SYSTEM PERFORMANCE REPORT")
    print("="*LINE_LENGTH)
    dramatic_pause(1)

    typing_with_pauses(f"💸 Confidential funds used: ₱{50_000_000 - ombudsman.confidential_funds:,}")
    typing_with_pauses(f"📊 Cases resolved: {ombudsman.corruption_cases_resolved}")
    typing_with_pauses(f"⏱️  Average justice delivery time: Still counting...")
    typing_with_pauses(f"🏆 Corruption level: Unchanged")

    time.sleep(2)  # Let the irony sink in

    typing_with_pauses("\n💡 SYSTEM ERROR: Justice.exe has stopped working")
    typing_with_pauses("🔄 Please restart democracy and try again")
    typing_with_pauses("\n#JusticeDelayed #JusticeDenied #TaxPayersMoney #WakeUpPilipinas")

    print()
    play_with_wait(DELAY)

if __name__ == "__main__":
    main()
