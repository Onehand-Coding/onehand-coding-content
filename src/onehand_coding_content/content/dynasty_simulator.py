"""
Philippine Political Dynasty Simulator
A stark look at inherited power in Philippine politics
"""

import time
import sys
import signal
import random
import itertools

from ..sounds import play_with_wait, CORRUPTION_3
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause


def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    raise KeyboardInterrupt


def run_dynasty_loop():
    """Simulate the never ending political dynasty loop in the Philippines."""
    year = 2028  # Next presidential election
    election_count = 0

    try:
        while True:  # The loop that defines Philippine politics
            election_count += 1

            typewriter_effect(f"\n>>> ELECTION YEAR {year}")
            dramatic_pause(1)

            typewriter_effect("  Ballots being cast...")
            time.sleep(1)
            typewriter_effect("  Votes being counted...")
            time.sleep(1)

            # Election Results - Same Surnames Win
            typing_with_pauses(f"\n  📊 RESULTS: Same families win again!")
            time.sleep(0.5)

            typewriter_effect(f"    • Marcos family: Still in power")
            typewriter_effect(f"    • Duterte family: Still in power")
            typewriter_effect(f"    • Senator siblings: Still in Senate")
            typewriter_effect(f"    • Provincial dynasties: Still controlling their territories")

            time.sleep(1)

            # The Waiting Period
            typewriter_effect(f"\n  ⏳ Simulating {year}-{year+6} term...")
            time.sleep(2.5)  # Representing 6-year term

            typewriter_effect(f"  ✓ Term completed. Same surnames still in power.")

            # Meta Commentary
            if election_count == 1:
                time.sleep(1)
                typing_with_pauses("\n  # Hmmm, coincidence lang siguro...")
            elif election_count == 2:
                time.sleep(1)
                typing_with_pauses("\n  # Wait, same families pa rin?")
            elif election_count == 3:
                time.sleep(1)
                typing_with_pauses("\n  # Ito na yata yung pattern eh...")
            elif election_count == 4:
                time.sleep(1)
                typing_with_pauses("\n  # Decades na... still the same surnames.")
            elif election_count >= 5:
                time.sleep(1)
                typing_with_pauses("\n  # This is not a bug. It's a FEATURE.")

            year += 6  # Next election cycle

            # The Break Statement That Never Executes
            # break  # Anti-Dynasty Law? Pending since Article II, Section 26, 1987 Constitution
            # break  # "The State shall guarantee equal access to opportunities for public service"
            # break  # Still waiting for Congress to pass the enabling law...
            # break  # Pero puro dynasty members naman ang Congress, so... 🤷

            time.sleep(2)

    except KeyboardInterrupt:
        # User tries to escape the loop
        print("\n\n")
        dramatic_pause(2)

        print("=" * 60)
        typing_with_pauses("⚠️  SIMULATION INTERRUPTED BY USER")
        print("=" * 60)

        time.sleep(1)

        typing_with_pauses(f"\n  You pressed Ctrl+C after {election_count} election cycles.")
        typing_with_pauses(f"  That's {election_count * 6} years of the same families in power.")

        dramatic_pause(2)

        typing_with_pauses("\n  You can stop the simulation...")
        dramatic_pause(2)
        typing_with_pauses("  ...pero yung reality? Tuloy pa rin bukas.")

        dramatic_pause(2)

        typing_with_pauses("\n  At least sa code, may Ctrl+C button.")
        time.sleep(1)
        typing_with_pauses("  Sa totoo? Wala tayong ganyang option.")
        time.sleep(1)
        typing_with_pauses("  The loop just... continues. Forever.")

        dramatic_pause(2)

        print("\n" + "=" * 60)
        typewriter_effect("SYSTEM NOTES:")
        print("=" * 60)
        typing_with_pauses("\n  • Anti-Dynasty Law: Pending since 1987 (37+ years)")
        typing_with_pauses("  • Article II, Section 26: 'State shall guarantee equal access'")
        typing_with_pauses("  • Enabling Law: Still not passed by Congress")
        typing_with_pauses("  • Congress composition: Mostly dynasty members")
        typing_with_pauses("  • Prognosis: while True loop continues...")

        dramatic_pause(2)

        print()
        typing_with_pauses("💭 This is not a bug. This is by design.")
        print()

        time.sleep(1)

        play_with_wait(CORRUPTION_3)


def main():
    # The Dynasty Database - Patterns observed in Philippine politics as of 2025.
    national_positions = {
        "Executive Branch": {
            "President": "Marcos Family",
            "Senator": "Marcos Family"
        },
        "Vice President": {
            "VP": "Duterte Family (Former President's Daughter)"
        },
        "Senate": {
            "Slot 1-2": "Villar Siblings",
            "Slot 3-4": "Ejercito-Estrada Clan",
            "Slot 5-6": "Cayetano Siblings",
            "Slot 7-9": "Tulfo Brothers"
        }
    }

    provincial_dynasties = {
        "Isabela": ["Dy Family", "Albano Family"],
        "Ilocos Norte": ["Marcos Family"],
        "Davao": ["Duterte Family"],
        "Maguindanao": ["Mangudadatu Family"],
        "Cavite": ["Remulla Family", "Revilla Family"],
        "Pampanga": ["Lapid Family"],
        "Zamboanga Sibugay": ["Hofer Family"],
        "Cebu": ["Garcia Family"],
        "Camarines Sur": ["Villafuerte Family"]
    }

    # System Initialization
    print()
    print("=" * 60)
    typewriter_effect("PHILIPPINE POLITICAL DYNASTY SIMULATOR v1987.0")
    print("=" * 60)
    time.sleep(1)

    typewriter_effect("\n# Initializing democracy.exe...")
    dramatic_pause(2)

    typewriter_effect("\n# Loading political families into power...")
    time.sleep(1)

    # Show current power structure
    typing_with_pauses("\n>>> NATIONAL LEVEL DETECTED:")
    time.sleep(0.5)

    for branch, positions in national_positions.items():
        print(f"\n  {branch}:")
        for position, family in positions.items():
            typing_with_pauses(f"    • {position}: {family}")
            time.sleep(0.3)

    dramatic_pause(2)

    typing_with_pauses("\n>>> PROVINCIAL DYNASTIES DETECTED:")
    time.sleep(0.5)

    for province, families in list(provincial_dynasties.items())[:5]:  # Show first 5
        typing_with_pauses(f"\n  {province}:")
        for family in families:
            typing_with_pauses(f"    • {family} (Controlling local government for decades)")
            time.sleep(0.3)

    typing_with_pauses(f"\n  ... and more provinces with similar patterns")

    dramatic_pause(3)

    # === NEW SECTION: BRUTE FORCE SOLUTION ATTEMPT ===
    print("\n" + "=" * 60)
    typing_with_pauses("💡 ATTEMPTING SOLUTION: Brute Force Configuration Search")
    print("=" * 60)

    time.sleep(1)

    typing_with_pauses("\n# Maybe we can find a dynasty-free government configuration?")
    typewriter_effect("# Let's try different permutations of available candidates...")

    dramatic_pause(2)

    # Define candidate pool for NATIONAL positions only
    national_candidates = [
        ("Marcos_A", "Marcos Family"),
        ("Marcos_B", "Marcos Family"),
        ("Duterte_A", "Duterte Family"),
        ("Duterte_B", "Duterte Family"),
        ("Villar_A", "Villar Family"),
        ("Villar_B", "Villar Family"),
        ("Cayetano_A", "Cayetano Family"),
        ("Cayetano_B", "Cayetano Family"),
        ("Ejercito_A", "Ejercito-Estrada Family"),
        ("Tulfo_A", "Tulfo Family"),
        ("Tulfo_B", "Tulfo Family"),
        ("Independent_A", "No Dynasty"),
        ("Independent_B", "No Dynasty"),
        ("Independent_C", "No Dynasty"),
    ]

    # Provincial positions are LOCKED to their territories (reality check)
    provincial_locks = {
        "Governor (Isabela)": [
            ("Dy_A", "Dy Family"),
            ("Albano_A", "Albano Family"),
            ("Independent_Local_1", "No Dynasty")
        ],
        "Governor (Ilocos Norte)": [
            ("Marcos_Provincial", "Marcos Family"),
            ("Independent_Local_2", "No Dynasty")
        ],
        "Governor (Davao)": [
            ("Duterte_Provincial", "Duterte Family"),
            ("Independent_Local_3", "No Dynasty")
        ]
    }

    national_positions = [
        "President",
        "Vice President",
        "Senator 1",
        "Senator 2",
        "Senator 3"
    ]

    typing_with_pauses(f"\n📊 Candidate Pool Analysis:")
    typing_with_pauses(f"   National candidates: {len(national_candidates)} available")
    typing_with_pauses(f"     • Dynasty-affiliated: {len([c for c in national_candidates if c[1] != 'No Dynasty'])}")
    typing_with_pauses(f"     • Independent: {len([c for c in national_candidates if c[1] == 'No Dynasty'])}")

    dramatic_pause(2)

    typing_with_pauses("\n   ⚠️  Provincial positions: PRE-DETERMINED by territory")
    for province, pool in provincial_locks.items():
        dynasty_count = len([c for c in pool if c[1] != "No Dynasty"])
        typing_with_pauses(f"     • {province}: {dynasty_count}/{len(pool)} candidates are dynasty members")
        time.sleep(0.3)

    typing_with_pauses(f"\n🎯 Positions to randomize: {len(national_positions)} (national level only)")
    typing_with_pauses(f"🔒 Positions locked by territory: {len(provincial_locks)} (provincial level)")

    dramatic_pause(2)

    typing_with_pauses("\n# Generating random government configurations...")
    time.sleep(1)

    # Try 3 random permutations
    for attempt in range(1, 4):
        print(f"\n{'─' * 60}")
        typing_with_pauses(f"🔍 ATTEMPT #{attempt}: Testing random configuration")
        print(f"{'─' * 60}")

        dramatic_pause(1)

        # Get random sample for NATIONAL positions
        national_config = random.sample(national_candidates, len(national_positions))

        # Get random picks from PROVINCIAL locks (constrained by territory)
        provincial_config = {}
        for province, pool in provincial_locks.items():
            provincial_config[province] = random.choice(pool)

        typewriter_effect("\n  Proposed Government Configuration:")
        time.sleep(0.5)

        # Display NATIONAL configuration
        typing_with_pauses("\n  National Level (randomized):")
        for i, position in enumerate(national_positions):
            candidate_name, family = national_config[i]
            typing_with_pauses(f"    • {position}: {candidate_name} ({family})")
            time.sleep(0.3)

        # Display PROVINCIAL configuration (territory-locked)
        dramatic_pause(1)
        typing_with_pauses("\n  Provincial Level (locked by territory):")
        for province, (candidate_name, family) in provincial_config.items():
            typing_with_pauses(f"    • {province}: {candidate_name} ({family})")
            time.sleep(0.3)

        dramatic_pause(2)

        # Analyze for dynasties
        typewriter_effect("\n  🔬 Analyzing for dynasty members...")
        time.sleep(1)

        # Combine both configs for analysis
        all_config = national_config + list(provincial_config.values())
        total_positions = len(national_positions) + len(provincial_locks)

        # Count dynasty members
        dynasty_count = len([c for c in all_config if c[1] != "No Dynasty"])
        dynasty_percentage = (dynasty_count / total_positions) * 100

        # Check for family duplicates
        families = [c[1] for c in all_config if c[1] != "No Dynasty"]
        family_counts = {}
        for family in families:
            family_counts[family] = family_counts.get(family, 0) + 1
        duplicate_families = sum(1 for count in family_counts.values() if count > 1)

        typing_with_pauses(f"\n  📈 Results:")
        time.sleep(0.3)
        typing_with_pauses(f"    • Total positions: {total_positions}")
        time.sleep(0.3)
        typing_with_pauses(f"    • Dynasty members: {dynasty_count}/{total_positions} ({dynasty_percentage:.1f}%)")
        time.sleep(0.3)

        if duplicate_families > 0:
            typing_with_pauses(f"    • Families with multiple members: {duplicate_families}")
            time.sleep(0.3)

        independent_count = total_positions - dynasty_count
        typing_with_pauses(f"    • Independent officials: {independent_count}/{total_positions} ({100-dynasty_percentage:.1f}%)")

        dramatic_pause(2)

        # Verdict
        if dynasty_count == 0:
            typing_with_pauses("\n  ✅ SUCCESS: Dynasty-free government found!")
        else:
            typing_with_pauses(f"\n  ❌ FAILED: Still {dynasty_percentage:.1f}% dynasty-controlled")
            time.sleep(0.5)
            typing_with_pauses(f"  (Even with provinces locked to their territories)")

        time.sleep(1)

        if attempt < 3:
            typewriter_effect("\n  Trying another combination...")
            time.sleep(1)

    # Final analysis
    dramatic_pause(3)

    print("\n" + "=" * 60)
    typing_with_pauses("📊 BRUTE FORCE ATTEMPT: CONCLUSION")
    print("=" * 60)

    time.sleep(1)

    typing_with_pauses("\n  After 3 random configuration attempts:")
    time.sleep(0.5)
    typing_with_pauses("  ❌ No dynasty-free government configuration found")

    dramatic_pause(2)

    typing_with_pauses("\n  Root Cause Analysis:")
    time.sleep(0.5)
    typewriter_effect("    • Problem is not the algorithm")
    time.sleep(0.5)
    typewriter_effect("    • Problem is the dataset (candidate pool)")
    time.sleep(0.5)
    typewriter_effect(f"    • National level: {len([c for c in national_candidates if c[1] != 'No Dynasty'])}/{len(national_candidates)} candidates are dynasty-affiliated")
    time.sleep(0.5)
    typewriter_effect("    • Provincial level: Already locked to territorial dynasties")
    time.sleep(0.5)
    typewriter_effect("    • Even randomizing national positions can't overcome provincial locks")

    dramatic_pause(2)

    typing_with_pauses("\n  💭 Conclusion:")
    time.sleep(0.5)
    typing_with_pauses("  You can't brute force your way out of a system")
    time.sleep(0.5)
    typing_with_pauses("  where the input itself is already compromised.")

    dramatic_pause(3)

    typing_with_pauses("You want to see why?...")

    time.sleep(2)

    run_dynasty_loop()  # The Infinite Loop - The Heart of the Problem


if __name__ == "__main__":
    # Register signal handler for graceful Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    print("\n")
    main()
    print("\n")
