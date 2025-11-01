import time

from ..config import LINE_LENGTH
from ..sounds import play_with_wait, CORRUPTION_2
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause

class Budget2025Reallocator:
    """
    Philippine 2025 National Budget Optimizer™
    "Realigning priorities for the people!" (some people 👀)
    Total: ₱6.352 Trillion
    """

    def __init__(self):
        self.total_budget = 6_352_000_000_000  # ₱6.352 Trillion
        self.original_allocations = {
            "PhilHealth Subsidy": 74_000_000_000,
            "Education (DepEd)": 852_000_000_000,
            "4Ps Anti-Poverty": 113_000_000_000,
            "Calamity Response": 45_000_000_000,
        }
        self.reallocated = {}

        print("\n" + "="*LINE_LENGTH)
        typewriter_effect("🏛️  2025 NATIONAL BUDGET REALLOCATION SYSTEM")
        print("="*LINE_LENGTH)
        print()
        typing_with_pauses("'Optimizing for maximum... efficiency? 🤔'")
        dramatic_pause(2)

    def show_original_budget(self):
        """Display original proposed budget"""
        typewriter_effect("\n📊 ORIGINAL BUDGET PROPOSAL (2024):")
        print("-"*LINE_LENGTH)
        dramatic_pause(1)

        for program, amount in self.original_allocations.items():
            typing_with_pauses(f"   • {program}: ₱{amount:,.2f}")
            time.sleep(0.8)

        dramatic_pause(2)
        typing_with_pauses("\n✅ 'Looks good for the people!' - Citizens")
        dramatic_pause(1)

    def bicam_magic(self):
        """The mysterious bicameral conference committee process"""
        print("\n\n" + "="*LINE_LENGTH)
        typewriter_effect("🎩 BICAMERAL CONFERENCE COMMITTEE IN SESSION...")
        print("="*LINE_LENGTH)
        dramatic_pause(2)

        typing_with_pauses("\n📋 Processing realignments...")
        dramatic_pause(2)

        typing_with_pauses("🔄 Analyzing 'priorities'...")
        dramatic_pause(2)

        typing_with_pauses("🧮 Calculating 'optimal' distribution...")
        dramatic_pause(2)

        typing_with_pauses("\n⚡ APPLYING REALIGNMENT ALGORITHM...")
        dramatic_pause(1)

        # The infamous realignment
        print("\n🎯 Realignment Summary:")
        typing_with_pauses("   • Regular Realignments: ₱487.5 Billion")
        time.sleep(1)
        typing_with_pauses("   • Unprogrammed Funds Added: ₱373 Billion")
        time.sleep(1)

        total_realigned = 487_500_000_000 + 373_000_000_000
        typing_with_pauses(f"   • TOTAL REALIGNED: ₱{total_realigned:,.2f}")
        dramatic_pause(2)

        typing_with_pauses("\n🤔 Wait... ₱860.5 BILLION realigned?")
        dramatic_pause(2)
        typing_with_pauses("📝 Note: 'Standard procedure daw. Nothing to see here.'")

    def show_cuts(self):
        """Show what got cut"""
        print("\n\n" + "="*LINE_LENGTH)
        typewriter_effect("✂️  BUDGET CUTS (For optimization purposes)")
        print("="*LINE_LENGTH)
        dramatic_pause(2)

        cuts = [
            ("PhilHealth Subsidy", 74_000_000_000, 29_900_000_000,
             "60% cut. 'Mag-PERA na lang kayo sa politicians!' 🎟️"),

            ("4Ps Anti-Poverty Program", 113_000_000_000, 88_000_000_000,
             "22% cut. 'Resilience training via hunger!' 💪"),

            ("Calamity Response Fund", 45_000_000_000, 35_000_000_000,
             "22% cut. 'Pray harder during typhoons!' 🙏"),

            ("Education Programs", 852_000_000_000, 750_000_000_000,
             "12% cut. 'Ignorance is bliss naman daw!' 📚")
        ]

        for program, original, new, comment in cuts:
            cut_amount = original - new
            cut_percent = (cut_amount / original) * 100

            typing_with_pauses(f"\n📉 {program}:")
            typing_with_pauses(f"   Original: ₱{original:,.2f}")
            typing_with_pauses(f"   New Amount: ₱{new:,.2f}")
            typing_with_pauses(f"   CUT: -₱{cut_amount:,.2f} ({cut_percent:.1f}%)")
            time.sleep(1)
            typing_with_pauses(f"   💬 {comment}")
            dramatic_pause(2)

    def show_increases(self):
        """Show what got INCREASED"""
        print("\n\n" + "="*LINE_LENGTH)
        typewriter_effect("📈 BUDGET INCREASES (For 'priority' projects)")
        print("="*LINE_LENGTH)
        dramatic_pause(2)

        typing_with_pauses("\n💡 Where did the money go?")
        dramatic_pause(1.5)

        increases = [
            ("Local Infrastructure Projects", 120_000_000_000, 520_000_000_000,
             "333% increase! 'Roads before education!' 🛣️"),

            ("Ayuda/Aid Programs", 45_000_000_000, 280_000_000_000,
             "522% increase! 'Perfect timing before 2025 midterms!' 🗳️"),

            ("Congressional Priority Projects", 35_000_000_000, 165_000_000_000,
             "371% increase! 'Purely for the people's benefit!' 👀"),

            ("DPWH 'Various' Projects", 200_000_000_000, 450_000_000_000,
             "125% increase! 'Detailed breakdown? Next question pls.' 🤐")
        ]

        for program, original, new, comment in increases:
            increase_amount = new - original
            increase_percent = ((new - original) / original) * 100

            typing_with_pauses(f"\n📊 {program}:")
            typing_with_pauses(f"   Before: ₱{original:,.2f}")
            typing_with_pauses(f"   After: ₱{new:,.2f}")
            typing_with_pauses(f"   INCREASE: +₱{increase_amount:,.2f} (+{increase_percent:.0f}%)")
            time.sleep(1)
            typing_with_pauses(f"   💬 {comment}")
            dramatic_pause(2)

        typing_with_pauses("\n\n🗓️  Timeline Check:")
        typing_with_pauses("   2025 Budget: Approved December 2024")
        typing_with_pauses("   2025 Midterm Elections: May 2025")
        dramatic_pause(2)
        typing_with_pauses("   🤔 Coincidence? 'Absolutely!' - Politicians")

    def public_reaction(self):
        """Show public and expert reactions"""
        print("\n\n" + "="*LINE_LENGTH)
        typewriter_effect("📱 PUBLIC REACTION")
        print("="*LINE_LENGTH)
        dramatic_pause(1)

        reactions = [
            ("Health Workers", "😤 'Gastos ng medical assistance lalaki kasi walang PhilHealth!'"),
            ("Teachers", "🤦 'Kulang na nga facilities, binawasan pa budget'"),
            ("Economists", "📊 'This is textbook patronage politics'"),
            ("Poor Families", "😔 '4Ps nabawasan pero bilihin tumaas. Paano na?'"),
            ("IBON Foundation", "📢 '2025 BBM: Budget Badly Made'"),
            ("CCGG (Good Gov't Group)", "⚖️ 'This budget betrays the Filipino people'"),
            ("Regular Citizens", "🥲 'Ayuda before elections, ghost after elections'")
        ]

        for source, reaction in reactions:
            typing_with_pauses(f"\n   {source}: {reaction}")
            time.sleep(1.5)

        dramatic_pause(2)

        typing_with_pauses("\n\n📢 OFFICIAL GOVERNMENT RESPONSE:")
        dramatic_pause(1)
        typing_with_pauses("   'The budget reflects our commitment to the people.'")
        dramatic_pause(1)
        typing_with_pauses("   'All allocations were done transparently.'")
        dramatic_pause(1)
        typing_with_pauses("   'Opposition is politically motivated.'")
        dramatic_pause(1)
        typing_with_pauses("   'Critics are part of destabilization plot.' 🙄")
        dramatic_pause(2)

    def generate_summary(self):
        """Final summary with the math"""
        print("\n\n" + "="*LINE_LENGTH)
        typewriter_effect("🧮 FINAL SUMMARY: THE MATH")
        print("="*LINE_LENGTH)
        dramatic_pause(2)

        typing_with_pauses(f"\n💰 Total 2025 Budget: ₱{self.total_budget:,.2f}")
        typing_with_pauses("🔄 Amount Realigned: ₱860,500,000,000")
        dramatic_pause(1)

        percentage = (860_500_000_000 / self.total_budget) * 100
        typing_with_pauses(f"\n📊 That's {percentage:.1f}% of the entire national budget!")
        dramatic_pause(2)

        typing_with_pauses("\n📉 Priorities DECREASED:")
        typing_with_pauses("   ❌ Healthcare")
        typing_with_pauses("   ❌ Education")
        typing_with_pauses("   ❌ Poverty Programs")
        typing_with_pauses("   ❌ Disaster Response")
        dramatic_pause(1)

        typing_with_pauses("\n📈 Priorities INCREASED:")
        typing_with_pauses("   ✅ Local Infrastructure (controllable)")
        typing_with_pauses("   ✅ Ayuda Programs (with faces on tarpaulins)")
        typing_with_pauses("   ✅ Congressional Insertions (mysterious)")
        typing_with_pauses("   ✅ 'Various' DPWH Projects (vague)")
        dramatic_pause(2)

        typing_with_pauses("\n🗳️  Pattern Recognition:")
        typing_with_pauses("   Election Year → Budget goes to visible projects")
        typing_with_pauses("   Non-Election Year → Budget goes to... also visible projects")
        dramatic_pause(1)
        typing_with_pauses("   Conclusion: 'It's always election season!' 🎪")
        dramatic_pause(2)

        typing_with_pauses("\n💡 Key Learnings:")
        typing_with_pauses("   1. Healthcare < Campaign Materials")
        typing_with_pauses("   2. Education < Photo Ops")
        typing_with_pauses("   3. Poverty Programs < Politician Brands")
        typing_with_pauses("   4. People's Welfare < Political Survival")


def main():
    """Main entry point"""
    reallocator = Budget2025Reallocator()

    # Show original budget
    reallocator.show_original_budget()

    # The magical bicam process
    reallocator.bicam_magic()

    # Show the cuts
    reallocator.show_cuts()

    # Show the increases
    reallocator.show_increases()

    # Public reaction
    reallocator.public_reaction()

    # Final summary
    reallocator.generate_summary()

    # Final thoughts
    print("\n\n" + "="*LINE_LENGTH)
    typewriter_effect("💭 CLOSING THOUGHTS")
    print("="*LINE_LENGTH)
    dramatic_pause(1)

    typing_with_pauses("'Budget for the people... just not THOSE people.' 🎭")
    dramatic_pause(1)
    typing_with_pauses("'Transparency: You can see the process, but can't do anything about it.' 🔍")
    dramatic_pause(2)

    typing_with_pauses("\n\n# Python Representation:")
    typing_with_pauses("# if election_year:")
    typing_with_pauses("#     budget.reallocate_to(visible_projects)")
    typing_with_pauses("#     budget.cut_from(essential_services)")
    typing_with_pauses("#     politicians.print('Para sa bayan!')")
    typing_with_pauses("# ")
    typing_with_pauses("# # Output: Bayan gutom, politician busog 🍽️")

    play_with_wait(CORRUPTION_2)

# Demo usage
if __name__ == "__main__":
    main()
