import time
import random

class ContractorSelectionSystem:
    """
    Fair and Transparent Bidding System™
    "Random selection guaranteed!" (wink wink)
    """

    def __init__(self):
        self.the_chosen_one = "Kamag-anak Construction Corp."
        print("🏗️  GOVERNMENT PROJECT BIDDING SYSTEM")
        print("="*60)
        print("📜 'Ensuring fair and transparent selection since... today!'")
        print("="*60)
        time.sleep(2)

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

        print("\n📋 REGISTERED BIDDERS:\n")
        for i, bidder in enumerate(bidders, 1):
            print(f"{i}. {bidder['name']}")
            print(f"   Experience: {bidder['experience']}")
            print(f"   Bid Amount: {bidder['bid']}")
            print(f"   Credentials: {bidder['credentials']}")
            print(f"   Past Projects: {bidder['past_projects']}")
            print()
            time.sleep(1.5)

        return bidders

    def evaluation_criteria(self):
        """Official evaluation metrics (very scientific)"""
        print("\n📊 EVALUATION CRITERIA:")
        print("="*60)
        time.sleep(1)

        criteria = [
            ("Technical Competence", "30%", "Important daw"),
            ("Financial Capability", "25%", "Dapat may pera"),
            ("Experience", "20%", "Mas matanda mas magaling?"),
            ("Bid Price", "15%", "Lower is better... usually"),
            ("Special Considerations", "10%", "👀 *The secret sauce*")
        ]

        for criterion, weight, note in criteria:
            print(f"✓ {criterion}: {weight} - {note}")
            time.sleep(0.8)

    def random_selection_process(self):
        """The most 'random' selection you'll ever see"""
        print("\n\n🎰 INITIATING RANDOM SELECTION ALGORITHM...")
        print("="*60)
        time.sleep(2)

        print("🔄 Analyzing bids...")
        time.sleep(2)

        print("🧮 Computing scores...")
        time.sleep(2)

        print("🎲 Applying randomization matrix...")
        time.sleep(2)

        # Dramatic countdown
        print("\n⏳ Selecting winner in:")
        for i in range(3, 0, -1):
            print(f"   {i}...")
            time.sleep(1)

        # Fake randomization
        print("\n🎯 Random selection in progress:")
        fake_candidates = [
            "Reliable Contractors Co.",
            "Quality Infrastructure Ltd.",
            "Experienced Builders Inc.",
            "Kamag-anak Construction Corp."
        ]

        time.sleep(1)
        for candidate in fake_candidates:
            print(f"   Checking... {candidate}")
            time.sleep(0.5)
            if candidate != self.the_chosen_one:
                print(f"   ❌ Disqualified (random reasons)")
            else:
                print(f"   ✅ *Mysteriously passes all criteria*")
            time.sleep(1)

    def announce_winner(self):
        """The grand reveal"""
        print("\n\n" + "="*60)
        print("🎊 OFFICIAL ANNOUNCEMENT")
        print("="*60)
        time.sleep(2)

        print(f"\n🏆 WINNER: {self.the_chosen_one}")
        time.sleep(1)

        print("\n📢 Justification:")
        print("   'After careful and RANDOM evaluation...'")
        time.sleep(1)
        print("   'The selection process was TRANSPARENT...'")
        time.sleep(1)
        print("   'All criteria were FAIRLY assessed...'")
        time.sleep(1)
        print("   'This company offered the BEST value...'")
        time.sleep(2)

        print("\n💰 Contract Details:")
        print("   Amount: ₱800M (highest bid)")
        print("   Timeline: '18 months' (realistically: 5 years)")
        print("   Quality guarantee: 'Trust me bro'")
        time.sleep(2)

    def public_reaction(self):
        """The aftermath"""
        print("\n\n📱 PUBLIC REACTION:")
        print("="*60)
        time.sleep(1)

        reactions = [
            "🤨 Netizen1: 'Random nga, randomly chosen before the bidding'",
            "😤 Netizen2: 'Yung company 2 months old lang pero nanalo?'",
            "🤔 Netizen3: 'Same last name sa mayor... coincidence?'",
            "😂 Netizen4: 'Transparency = pwede ninyong makita pero di kayo pwedeng kumontra'",
            "🤷 Netizen5: 'Pilipinas pa ba surprised tayo?'"
        ]

        for reaction in reactions:
            print(f"   {reaction}")
            time.sleep(1.5)

        time.sleep(2)
        print("\n📢 Official Response:")
        print("   'Any insinuations of irregularity are baseless.'")
        time.sleep(1)
        print("   'The process followed all legal procedures.'")
        time.sleep(1)
        print("   'May complaint ka? File a case! (Matagal yan, 10 years minimum)'")


# Run the simulation
if __name__ == "__main__":
    system = ContractorSelectionSystem()
    time.sleep(1)

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
    print("🎭 END OF BIDDING PROCESS")
    print("💬 'Democracy in action!' - Official Tagline")
    print("🤦 'Déjà vu in action.' - Citizens")
    print("="*60)

    print("\n\n# Random.seed(ninong_ni_mayor)")
