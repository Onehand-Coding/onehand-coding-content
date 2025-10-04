import time
import random

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

        print("\n" + "="*70)
        typing_with_pauses("🏛️  2025 NATIONAL BUDGET REALLOCATION SYSTEM", delay=0.03)
        print("="*70)
        print()
        typing_with_pauses("'Optimizing for maximum... efficiency? 🤔'")
        dramatic_pause(2)

    def show_original_budget(self):
        """Display original proposed budget"""
        typewriter_effect("\n📊 ORIGINAL BUDGET PROPOSAL (2024):")
        print("-"*70)
        dramatic_pause(1)

        for program, amount in self.original_allocations.items():
            typewriter_effect(f"   • {program}: ₱{amount:,.2f}")
            time.sleep(0.8)

        dramatic_pause(2)
        typing_with_pauses("\n✅ 'Looks good for the people!' - Citizens")
        dramatic_pause(1)

    def bicam_magic(self):
        """The mysterious bicameral conference committee process"""
        print("\n\n" + "="*70)
        typing_with_pauses("🎩 BICAMERAL CONFERENCE COMMITTEE IN SESSION...", delay=0.03)
        print("="*70)
        dramatic_pause(2)

        typewriter_effect("\n📋 Processing realignments...")
        dramatic_pause(2)

        typewriter_effect("🔄 Analyzing 'priorities'...")
        dramatic_pause(2)

        typewriter_effect("🧮 Calculating 'optimal' distribution...")
        dramatic_pause(2)

        typewriter_effect("\n⚡ APPLYING REALIGNMENT ALGORITHM...")
        dramatic_pause(1)

        # The infamous realignment
        print("\n🎯 Realignment Summary:")
        typewriter_effect("   • Regular Realignments: ₱487.5 Billion")
        time.sleep(1)
        typewriter_effect("   • Unprogrammed Funds Added: ₱373 Billion")
        time.sleep(1)

        total_realigned = 487_500_000_000 + 373_000_000_000
        typing_with_pauses(f"   • TOTAL REALIGNED: ₱{total_realigned:,.2f}")
        dramatic_pause(2)

        typewriter_effect("\n🤔 Wait... ₱860.5 BILLION realigned?")
        dramatic_pause(2)
        typing_with_pauses("📝 Note: 'Standard procedure daw. Nothing to see here.'")

    def show_cuts(self):
        """Show what got cut"""
        print("\n\n" + "="*70)
        typing_with_pauses("✂️  BUDGET CUTS (For optimization purposes)", delay=0.03)
        print("="*70)
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

            typewriter_effect(f"\n📉 {program}:")
            typewriter_effect(f"   Original: ₱{original:,.2f}")
            typewriter_effect(f"   New Amount: ₱{new:,.2f}")
            typing_with_pauses(f"   CUT: -₱{cut_amount:,.2f} ({cut_percent:.1f}%)")
            time.sleep(1)
            typing_with_pauses(f"   💬 {comment}")
            dramatic_pause(2)

    def show_increases(self):
        """Show what got INCREASED"""
        print("\n\n" + "="*70)
        typing_with_pauses("📈 BUDGET INCREASES (For 'priority' projects)", delay=0.03)
        print("="*70)
        dramatic_pause(2)

        typewriter_effect("\n💡 Where did the money go?")
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

            typewriter_effect(f"\n📊 {program}:")
            typewriter_effect(f"   Before: ₱{original:,.2f}")
            typewriter_effect(f"   After: ₱{new:,.2f}")
            typing_with_pauses(f"   INCREASE: +₱{increase_amount:,.2f} (+{increase_percent:.0f}%)")
            time.sleep(1)
            typing_with_pauses(f"   💬 {comment}")
            dramatic_pause(2)

        typewriter_effect("\n\n🗓️  Timeline Check:")
        typing_with_pauses("   2025 Budget: Approved December 2024")
        typing_with_pauses("   2025 Midterm Elections: May 2025")
        dramatic_pause(2)
        typing_with_pauses("   🤔 Coincidence? 'Absolutely!' - Politicians")

    def public_reaction(self):
        """Show public and expert reactions"""
        print("\n\n" + "="*70)
        typing_with_pauses("📱 PUBLIC REACTION", delay=0.03)
        print("="*70)
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

        typewriter_effect("\n\n📢 OFFICIAL GOVERNMENT RESPONSE:")
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
        print("\n\n" + "="*70)
        typing_with_pauses("🧮 FINAL SUMMARY: THE MATH", delay=0.03)
        print("="*70)
        dramatic_pause(2)

        typewriter_effect(f"\n💰 Total 2025 Budget: ₱{self.total_budget:,.2f}")
        typewriter_effect(f"🔄 Amount Realigned: ₱860,500,000,000")
        dramatic_pause(1)

        percentage = (860_500_000_000 / self.total_budget) * 100
        typing_with_pauses(f"\n📊 That's {percentage:.1f}% of the entire national budget!")
        dramatic_pause(2)

        typewriter_effect("\n📉 Priorities DECREASED:")
        typewriter_effect("   ❌ Healthcare")
        typewriter_effect("   ❌ Education")
        typewriter_effect("   ❌ Poverty Programs")
        typewriter_effect("   ❌ Disaster Response")
        dramatic_pause(1)

        typewriter_effect("\n📈 Priorities INCREASED:")
        typewriter_effect("   ✅ Local Infrastructure (controllable)")
        typewriter_effect("   ✅ Ayuda Programs (with faces on tarpaulins)")
        typewriter_effect("   ✅ Congressional Insertions (mysterious)")
        typewriter_effect("   ✅ 'Various' DPWH Projects (vague)")
        dramatic_pause(2)

        typewriter_effect("\n🗳️  Pattern Recognition:")
        typing_with_pauses("   Election Year → Budget goes to visible projects")
        typing_with_pauses("   Non-Election Year → Budget goes to... also visible projects")
        dramatic_pause(1)
        typing_with_pauses("   Conclusion: 'It's always election season!' 🎪")
        dramatic_pause(2)

        typewriter_effect("\n💡 Key Learnings:")
        typing_with_pauses("   1. Healthcare < Campaign Materials")
        typing_with_pauses("   2. Education < Photo Ops")
        typing_with_pauses("   3. Poverty Programs < Politician Brands")
        typing_with_pauses("   4. People's Welfare < Political Survival")


# Demo usage
if __name__ == "__main__":
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
    print("\n\n" + "="*70)
    typing_with_pauses("💭 CLOSING THOUGHTS", delay=0.03)
    print("="*70)
    dramatic_pause(1)

    typing_with_pauses("'Budget for the people... just not THOSE people.' 🎭")
    dramatic_pause(1)
    typing_with_pauses("'Transparency: You can see the process, but can't do anything about it.' 🔍")
    dramatic_pause(2)

    typewriter_effect("\n\n# Python Representation:")
    typewriter_effect("# if election_year:")
    typewriter_effect("#     budget.reallocate_to(visible_projects)")
    typewriter_effect("#     budget.cut_from(essential_services)")
    typewriter_effect("#     politicians.print('Para sa bayan!')")
    typewriter_effect("# ")
    typewriter_effect("# # Output: Bayan gutom, politician busog 🍽️")

    play_with_wait(CORRUPTION_2)
