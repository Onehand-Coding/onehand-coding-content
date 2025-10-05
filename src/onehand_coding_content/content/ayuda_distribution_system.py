import time
import random
from datetime import datetime
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause

class AyudaDistributionSystem:
    """
    National Ayuda Distribution System (NADS)
    Budget: ₱100B (subject to 'adjustments') | Coverage: Nationwide*
    "Mabilis, Epektibo, at Sapat!" (according to the press release)
    """

    def __init__(self):
        self.total_budget = 100_000_000_000  # 100 Billion
        self.remaining_budget = self.total_budget
        self.event_type = self._get_calamity_event()
        print()
        typing_with_pauses(f"🚨 {self.event_type} AYUDA DISTRIBUTION SYSTEM v2.0 🚨", delay=0.03)
        print("="*60)
        dramatic_pause(1)

    def _get_calamity_event(self):
        """Randomly select a reason for 'ayuda'"""
        events = [
            "Super Typhoon",
            "Earthquake",
            "Volcanic Eruption",
            "Pandemic Wave 12",
            "Economic 'Crisis'",
            "Holiday Season"
        ]
        return random.choice(events)

    def check_budget_status(self):
        """Check where the money went"""
        typewriter_effect("\n💰 Checking budget status...")
        dramatic_pause(2)

        # Simulate budget 'adjustments'
        self.remaining_budget *= 0.60  # 40% 'administrative costs'
        typing_with_pauses(f"   - Initial Budget: ₱{self.total_budget:,.2f}")
        typing_with_pauses(f"   - Less 'Administrative Costs' (40%): ₱{self.total_budget * 0.4:,.2f}")
        
        self.remaining_budget *= 0.75  # 25% 'logistical fees'
        typing_with_pauses(f"   - Less 'Logistical Fees' (25%): ₱{self.total_budget * 0.6 * 0.25:,.2f}")
        
        self.remaining_budget *= 0.90  # 10% 'miscellaneous expenses'
        typing_with_pauses(f"   - Less 'Miscellaneous Expenses' (10%): ₱{self.total_budget * 0.6 * 0.75 * 0.1:,.2f}")
        
        dramatic_pause(1)
        typewriter_effect(f"\n   ✅ Net Budget for Distribution: ₱{self.remaining_budget:,.2f}")
        typing_with_pauses("   📝 Note: 'Budget is fully accounted for.'")

    def list_requirements(self):
        """List the ever-changing list of requirements"""
        typewriter_effect("\n📋 Present the following requirements for validation:")
        dramatic_pause(1)
        
        requirements = [
            "   - Birth Certificate (original and 3 photocopies)",
            "   - Barangay Clearance (with dry seal)",
            "   - Proof of Residency (at least 10 years)",
            "   - Voter's ID (must have voted for the winning candidate)",
            "   - 2x2 ID Picture (with white background and no smile)",
            "   - Latest Utility Bill (under your name)",
            "   - NBI, Police, and UFO Clearance",
            "   - Certificate of Indigency (but must own a smartphone)",
            "   - Social Media Account (for photo ops)"
        ]
        
        for req in requirements:
            typing_with_pauses(req, delay=0.02)
        
        dramatic_pause(1)
        typing_with_pauses("\n   *Additional requirements may be announced on-site.*")

    def simulate_distribution(self, num_beneficiaries):
        """Simulate the chaotic distribution process"""
        typewriter_effect(f"\n\n🚀 Initiating 'ayuda' distribution for {num_beneficiaries} beneficiaries...")
        dramatic_pause(2)

        ayuda_per_person = self.remaining_budget / num_beneficiaries
        typewriter_effect(f"   - Calculated Ayuda per Person: ₱{ayuda_per_person:,.2f}")
        typing_with_pauses("   - Announcing to media: 'Up to ₱10,000 per family!'")
        dramatic_pause(2)

        typewriter_effect("\n   - Distribution Day Simulation:")
        dramatic_pause(1)
        
        events = [
            "   - 8:00 AM: Line starts forming.",
            "   - 10:00 AM: VIPs and media arrive for photo ops.",
            "   - 12:00 PM: Lunch break (2 hours).",
            "   - 2:00 PM: Forms are distributed (wrong forms).",
            "   - 3:00 PM: Ran out of ballpens.",
            "   - 4:00 PM: Cut-off time announced.",
            "   - 5:00 PM: Ayuda distribution officially 'completed'."
        ]
        
        for event in events:
            typing_with_pauses(event)
            time.sleep(0.5)

        final_ayuda = ayuda_per_person * 0.25 # 'Processing fees'
        dramatic_pause(1)
        typewriter_effect(f"\n\n   💸 Actual Ayuda Received per Person: ₱{final_ayuda:,.2f} (in a damaged envelope)")
        typing_with_pauses("   - Plus one (1) can of sardines and two (2) packs of noodles.")

    def generate_report(self):
        """Generate the official accomplishment report"""
        print("\n\n" + "="*60)
        typing_with_pauses("📈 ACCOMPLISHMENT REPORT", delay=0.03)
        print("="*60)
        dramatic_pause(1)

        typewriter_effect(f"🎯 Target Beneficiaries: 1,000,000")
        typewriter_effect(f"✅ Actual Beneficiaries Served: 1,000,000 (in the report)")
        typewriter_effect(f"💰 Budget Utilized: 100%")
        typewriter_effect(f"⭐ Satisfaction Rating: 110% (based on official surveys)")
        dramatic_pause(1)
        typing_with_pauses("\n🏆 Status: MISSION ACCOMPLISHED")
        typing_with_pauses("🎖️  Team to receive commendation and bonuses!")


def main():
    """Main entry point"""
    system = AyudaDistributionSystem()

    # Check budget
    system.check_budget_status()

    # List requirements
    system.list_requirements()

    # Simulate distribution
    # Target beneficiaries: 1M, but let's use a smaller number for simulation
    system.simulate_distribution(num_beneficiaries=1_000_000)

    # Generate report
    system.generate_report()

    print("\n\n" + "="*60)
    typing_with_pauses("💬 Official Statement:")
    typing_with_pauses("   'The distribution was a resounding success.'")
    dramatic_pause(1)
    typing_with_pauses("\n🤔 Citizens: 'Success po sa ano?'")
    print("="*60)


# Run the simulation
if __name__ == "__main__":
    main()
