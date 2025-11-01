import time
import random

from ..sounds import play_with_wait, SABOG_SOUND
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause

class ContractorSelectionSystem:
    """
    Fair and Transparent Bidding System™
    "Random selection guaranteed!" (wink wink)
    """

    def __init__(self):
        print()
        print("="*60)
        typewriter_effect("🏗️  GOVERNMENT PROJECT BIDDING SYSTEM")
        print("="*60)
        dramatic_pause(1)
        typing_with_pauses("📜 'Ensuring fair and transparent selection since... today!'")
        dramatic_pause(2)

        self.the_chosen_one = "Kasabwat Construction Corp."
        self.disqualification_reasons = [
            "Not known to project proponents",
            "Pasaway",
            "Doesnt want to provide SOP",
            "Not DPWH Certified, what?",
            "Not Certified to build Ghost Projects",
            "Not Certified to build Sub-standard Projects"
        ]
        self.bidders = [
            {
                "name": "Experienced Builders Inc.",
                "experience": "25 years",
                "bid": "₱450M",
                "credentials": "ISO Certified, AAA Rating",
                "past_projects": "200+ government projects, zero issues"
            },
            {
                "name": "Quality Infrastructure Ltd.",
                "experience": "18 years",
                "bid": "₱480M",
                "credentials": "PCAB Licensed, Award-winning",
                "past_projects": "150+ projects, international standards"
            },
            {
                "name": "Reliable Contractors Co.",
                "experience": "30 years",
                "bid": "₱420M",
                "credentials": "Multiple certifications",
                "past_projects": "Bridge still standing after 20 years!"
            },
            {
                "name": "Kasabwat Construction Corp.",
                "experience": "2 months",
                "bid": "₱800M",
                "credentials": "May contact number sa DPWH",
                "past_projects": "Cousin's bahay (ongoing)"
            }
        ]

    def display_bidders(self):
        """Show all participating bidders (for show)"""
        typewriter_effect("📋 REGISTERED BIDDERS:")
        print("="*60)
        dramatic_pause(2)
        for i, bidder in enumerate(self.bidders, 1):
            typing_with_pauses(f"{i}. {bidder['name']}")
            typing_with_pauses(f"   Experience: {bidder['experience']}")
            typing_with_pauses(f"   Bid Amount: {bidder['bid']}")
            typing_with_pauses(f"   Credentials: {bidder['credentials']}")
            typing_with_pauses(f"   Past Projects: {bidder['past_projects']}")
            print()
            time.sleep(0.8)

    def evaluation_criteria(self):
        """Official evaluation metrics (very scientific)"""
        typewriter_effect("\n📊 EVALUATION CRITERIA:")
        print("="*60)
        dramatic_pause(1)

        criteria = [
            ("Technical Competence", "30%", "Important daw"),
            ("Financial Capability", "25%", "Dapat may pera"),
            ("Experience", "20%", "Mas matanda mas magaling?"),
            ("Bid Price", "15%", "Lower is better... usually"),
            ("Special Considerations", "10%", "👀 *The secret sauce*")
        ]

        for criterion, weight, note in criteria:
            typing_with_pauses(f"✓ {criterion}: {weight} - {note}")
            time.sleep(0.5)

    def random_selection_process(self):
        """The most 'random' selection you'll ever see"""
        typewriter_effect("\n\n🎰 INITIATING RANDOM SELECTION ALGORITHM...")
        print("="*60)
        dramatic_pause(2)

        typing_with_pauses("🔄 Analyzing bids...")
        dramatic_pause(2)

        typing_with_pauses("🧮 Computing scores...")
        dramatic_pause(2)

        typing_with_pauses("🎲 Applying randomization matrix...")
        dramatic_pause(2)

        # Dramatic countdown
        typing_with_pauses("\n⏳ Selecting winner in:")
        for i in range(3, 0, -1):
            typing_with_pauses(f"   {i}...")
            time.sleep(1)

        # Fake randomization
        typing_with_pauses("\n🎯 Random selection in progress:")

        dramatic_pause(1)
        for bidder in self.bidders:
            bidder = bidder['name']
            typing_with_pauses(f"   Checking... {bidder}")
            time.sleep(0.5)
            if bidder != self.the_chosen_one:
                typing_with_pauses(f"   ❌ Disqualified ({random.choice(self.disqualification_reasons)})")
            else:
                typing_with_pauses("   ✅ *Mysteriously passes all criteria*")
            time.sleep(0.8)

    def announce_winner(self):
        """The grand reveal"""
        print("\n\n" + "="*60)
        typewriter_effect("🎊 OFFICIAL ANNOUNCEMENT")
        print("="*60)
        dramatic_pause(2)

        typing_with_pauses(f"\n🏆 WINNER: {self.the_chosen_one}", delay=0.04)
        dramatic_pause(1)

        typing_with_pauses("\n📢 Justification:")
        typing_with_pauses("   'After careful and RANDOM evaluation...'")
        dramatic_pause(1)
        typing_with_pauses("   'The selection process was TRANSPARENT...'")
        dramatic_pause(1)
        typing_with_pauses("   'All criteria were FAIRLY assessed...'")
        dramatic_pause(1)
        typing_with_pauses("   'This company offered the BEST value...'")
        dramatic_pause(2)

        typing_with_pauses("\n💰 Contract Details:")
        typing_with_pauses("   Amount: ₱800M (highest bid)")
        typing_with_pauses("   Timeline: '18 months' or '3 days if you want'")
        typing_with_pauses("   Quality guarantee: 'We are the DPWH'")
        dramatic_pause(2)

    def public_reaction(self):
        """The aftermath"""
        typewriter_effect("\n\n📱 PUBLIC REACTION:")
        print("="*60)
        dramatic_pause(1)

        reactions = [
            "🤨 Netizen1: 'Random nga, randomly chosen before the bidding'",
            "😤 Netizen2: 'Yung company 2 months old lang pero nanalo?'",
            "🤔 Netizen3: 'Same last name ni ano... coincidence?'",
            "😂 Netizen4: 'Transparency = pwede ninyong makita pero di kayo pwedeng kumontra'",
            "🤷 Netizen5: 'Pilipinas pa ba surprised tayo?'"
        ]

        for reaction in reactions:
            typing_with_pauses(f"   {reaction}")
            time.sleep(1)

        dramatic_pause(2)
        typing_with_pauses("\n📢 Official Response:")
        typing_with_pauses("   'Any insinuations of irregularity are baseless.'")
        dramatic_pause(1)
        typing_with_pauses("   'The process followed all legal procedures.'")
        dramatic_pause(1)
        typing_with_pauses("   'May complaint ka? File a case! (Matagal yan, 10 years minimum)'")


def main():
    """Main entry point"""
    system = ContractorSelectionSystem()
    dramatic_pause(1)

    # Show all bidders
    system.display_bidders()

    # Show evaluation criteria
    system.evaluation_criteria()

    # Run the "random" selection
    system.random_selection_process()

    # Announce winner
    system.announce_winner()

    # Show public reaction
    system.public_reaction()

    print("\n\n" + "="*60)
    typing_with_pauses("🎭 END OF BIDDING PROCESS")
    typing_with_pauses("💬 'Democracy in action!' - Official Tagline")
    typing_with_pauses("🤦 'Déjà vu in action.' - Citizens")
    print("="*60)

    typewriter_effect("\n\n# Random.seed(ninong_ni_senator)")

    play_with_wait(SABOG_SOUND)


# Run the simulation
if __name__ == "__main__":
    main()
