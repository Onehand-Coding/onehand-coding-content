import time
import random
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause

class ContractorSelectionSystem:
    """
    Fair and Transparent Bidding System™
    "Random selection guaranteed!" (wink wink)
    """

    def __init__(self):
        self.the_chosen_one = "Kamag-anak Construction Corp."
        typing_with_pauses("🏗️  GOVERNMENT PROJECT BIDDING SYSTEM", delay=0.03)
        print("="*60)
        typing_with_pauses("📜 'Ensuring fair and transparent selection since... today!'")
        print("="*60)
        dramatic_pause(2)

    def display_bidders(self):
        """Show all participating bidders (for show)"""
        bidders = [
            {
                "name": "Kamag-anak Construction Corp.",
                "experience": "2 months",
                "bid": "₱800M",
                "credentials": "May contact number ng mayor",
                "past_projects": "Cousin's bahay (ongoing)"
            },
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
            }
        ]

        typewriter_effect("\n📋 REGISTERED BIDDERS:\n")
        for i, bidder in enumerate(bidders, 1):
            typewriter_effect(f"{i}. {bidder['name']}")
            typewriter_effect(f"   Experience: {bidder['experience']}")
            typewriter_effect(f"   Bid Amount: {bidder['bid']}")
            typewriter_effect(f"   Credentials: {bidder['credentials']}")
            typing_with_pauses(f"   Past Projects: {bidder['past_projects']}")
            print()
            time.sleep(0.8)

        return bidders

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

        typewriter_effect("🔄 Analyzing bids...")
        dramatic_pause(2)

        typewriter_effect("🧮 Computing scores...")
        dramatic_pause(2)

        typewriter_effect("🎲 Applying randomization matrix...")
        dramatic_pause(2)

        # Dramatic countdown
        typewriter_effect("\n⏳ Selecting winner in:")
        for i in range(3, 0, -1):
            typewriter_effect(f"   {i}...")
            time.sleep(1)

        # Fake randomization
        typewriter_effect("\n🎯 Random selection in progress:")
        fake_candidates = [
            "Reliable Contractors Co.",
            "Quality Infrastructure Ltd.",
            "Experienced Builders Inc.",
            "Kamag-anak Construction Corp."
        ]

        dramatic_pause(1)
        for candidate in fake_candidates:
            typewriter_effect(f"   Checking... {candidate}")
            time.sleep(0.5)
            if candidate != self.the_chosen_one:
                typing_with_pauses(f"   ❌ Disqualified (random reasons)")
            else:
                typing_with_pauses(f"   ✅ *Mysteriously passes all criteria*")
            time.sleep(0.8)

    def announce_winner(self):
        """The grand reveal"""
        print("\n\n" + "="*60)
        typing_with_pauses("🎊 OFFICIAL ANNOUNCEMENT", delay=0.03)
        print("="*60)
        dramatic_pause(2)

        typing_with_pauses(f"\n🏆 WINNER: {self.the_chosen_one}", delay=0.04)
        dramatic_pause(1)

        typewriter_effect("\n📢 Justification:")
        typing_with_pauses("   'After careful and RANDOM evaluation...'")
        dramatic_pause(1)
        typing_with_pauses("   'The selection process was TRANSPARENT...'")
        dramatic_pause(1)
        typing_with_pauses("   'All criteria were FAIRLY assessed...'")
        dramatic_pause(1)
        typing_with_pauses("   'This company offered the BEST value...'")
        dramatic_pause(2)

        typewriter_effect("\n💰 Contract Details:")
        typewriter_effect("   Amount: ₱800M (highest bid)")
        typewriter_effect("   Timeline: '18 months' (realistically: 5 years)")
        typing_with_pauses("   Quality guarantee: 'Trust me bro'")
        dramatic_pause(2)

    def public_reaction(self):
        """The aftermath"""
        typewriter_effect("\n\n📱 PUBLIC REACTION:")
        print("="*60)
        dramatic_pause(1)

        reactions = [
            "🤨 Netizen1: 'Random nga, randomly chosen before the bidding'",
            "😤 Netizen2: 'Yung company 2 months old lang pero nanalo?'",
            "🤔 Netizen3: 'Same last name sa mayor... coincidence?'",
            "😂 Netizen4: 'Transparency = pwede ninyong makita pero di kayo pwedeng kumontra'",
            "🤷 Netizen5: 'Pilipinas pa ba surprised tayo?'"
        ]

        for reaction in reactions:
            typing_with_pauses(f"   {reaction}")
            time.sleep(1)

        dramatic_pause(2)
        typewriter_effect("\n📢 Official Response:")
        typing_with_pauses("   'Any insinuations of irregularity are baseless.'")
        dramatic_pause(1)
        typing_with_pauses("   'The process followed all legal procedures.'")
        dramatic_pause(1)
        typing_with_pauses("   'May complaint ka? File a case! (Matagal yan, 10 years minimum)'")


# Run the simulation
if __name__ == "__main__":
    system = ContractorSelectionSystem()
    dramatic_pause(1)

    # Show all bidders
    bidders = system.display_bidders()

    # Show evaluation criteria
    system.evaluation_criteria()

    # Run the "random" selection
    system.random_selection_process()

    # Announce winner
    system.announce_winner()

    # Show public reaction
    system.public_reaction()

    print("\n\n" + "="*60)
    typing_with_pauses("🎭 END OF BIDDING PROCESS", delay=0.03)
    typing_with_pauses("💬 'Democracy in action!' - Official Tagline")
    typing_with_pauses("🤦 'Déjà vu in action.' - Citizens")
    print("="*60)

    typewriter_effect("\n\n# Random.seed(ninong_ni_mayor)")
