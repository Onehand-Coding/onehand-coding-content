import time
import random

from ..config import LINE_LENGTH
from ..sounds import play_with_wait, CORRUPTION_1
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause


def main():
    """Main Entry point for Corruption Simulator."""
    print("\n", "=" * LINE_LENGTH)
    typewriter_effect("🇵🇭 PHILIPPINE CORRUPTION SIMULATOR 🇵🇭")
    print("=" * LINE_LENGTH)
    dramatic_pause(2)

    # FOR LOOP with BREAK - Government Officials Checking
    typing_with_pauses("\n📊 Checking Government officials for corruption...")
    dramatic_pause(1)

    officials = ["Mayor", "Governor", "Senator", "Congressman", "Barangay Captain",
               "Department Head", "Vice President", "Supreme Court Justice"]

    for official in officials:
        typing_with_pauses(f"Investigating {official}...")
        dramatic_pause(1)

        # Simulate corruption check (spoiler: everyone's corrupt)
        corruption_level = random.randint(1, 100)

        if corruption_level > 95:  # The rare "clean" official
            typing_with_pauses(f"✅ CLEAN! (Corruption: {corruption_level}%)")
            typing_with_pauses("🚨 BREAKING: First clean official found! Investigation complete!")
            break  # Exit loop - we found the unicorn!
        else:
            typing_with_pauses(f"💸 CORRUPT! (Level: {corruption_level}%)")

    # WHILE LOOP with CONTINUE - Philippine Budget Allocation
    print("\n" + "="*LINE_LENGTH)
    typing_with_pauses("💰 PHILIPPINE BUDGET ALLOCATION SYSTEM")
    print("="*LINE_LENGTH)
    dramatic_pause(1)

    budget_remaining = 1000000000  # 1 billion pesos
    project_count = 0

    projects = ["Education", "Healthcare", "Infrastructure", "Politician's Pocket",
               "Ghost Projects", "Overpriced Buildings", "Public Toilets Worth 50M",
               "Intelligence Funds", "Confidential Funds"]

    while budget_remaining > 0 and project_count < len(projects):
        current_project = projects[project_count]
        project_count += 1

        typing_with_pauses(f"\n🏗️  Allocating budget for: {current_project}")
        dramatic_pause(0.8)

        # Check if it's a "special" project (corruption magnet)
        if "Pocket" in current_project or "Ghost" in current_project or "Confidential" in current_project:
            allocation = random.randint(500000000, 800000000)  # Big chunk for corruption
            typing_with_pauses(f"💸 Allocated: ₱{allocation:,} (Priority funding! 😉)")
            budget_remaining -= allocation
            continue  # Skip the "completed" check - these never get completed properly

        # Regular projects get smaller budget
        allocation = random.randint(10000000, 50000000)
        typing_with_pauses(f"💵 Allocated: ₱{allocation:,}")
        budget_remaining -= allocation

        # Simulate project completion chance
        completion_chance = random.randint(1, 10)
        if completion_chance <= 3:  # 30% chance of completion
            typing_with_pauses("✅ Project completed successfully!")
        else:
            typing_with_pauses("⏳ Project ongoing... (for the next 10 years)")

        typing_with_pauses(f"💰 Remaining budget: ₱{budget_remaining:,}")

    # NESTED LOOPS with BREAK and CONTINUE - Senate Hearing Simulation
    print("\n" + "="*LINE_LENGTH)
    typing_with_pauses("🎭 SENATE HEARING: 'IN AID OF LEGISLATION'")
    print("="*LINE_LENGTH)
    dramatic_pause(1)

    senators = ["Sen. Questioner", "Sen. Grandstander", "Sen. Sleeping"]
    questions = ["Where did the money go?", "Are you aware of this?",
               "Do you take full responsibility?", "Sino ang may kasalanan?"]

    for senator in senators:
        typing_with_pauses(f"\n🎤 {senator} is now asking questions...")
        dramatic_pause(1)

        if "Sleeping" in senator:
            typing_with_pauses("😴 *Senator is sleeping*")
            continue  # Skip to next senator

        for question in questions:
            typing_with_pauses(f"❓ {senator}: '{question}'")
            time.sleep(0.8)

            # Simulate witness response
            response_type = random.choice(["invoke", "deflect", "answer"])

            if response_type == "invoke":
                typing_with_pauses("🤐 Witness: 'I invoke my right against self-incrimination.'")
                if "kasalanan" in question.lower():
                    typing_with_pauses("🚨 Classic Filipino corruption defense activated!")
                    break  # End questioning - they invoked rights
            elif response_type == "deflect":
                typing_with_pauses("🎯 Witness: 'That's not under my jurisdiction, Senator.'")
                continue  # Next question
            else:
                typing_with_pauses("📝 Witness: *Gives vague, non-committal answer*")

    typing_with_pauses("\n🎬 Senate hearing ends. No one goes to jail. See you next scandal!")
    typing_with_pauses("\n💡 LESSON LEARNED:")
    typing_with_pauses("   - BREAK: Use when you find the first clean official (rare!)")
    typing_with_pauses("   - CONTINUE: Use when skipping corrupt allocations or sleeping senators")
    typing_with_pauses("   - LOOPS: Perfect for simulating endless Philippine political cycles!")

    time.sleep(2)
    typing_with_pauses("\n🤷‍♂️ Welcome to Philippine politics - where the loops never end!")
    typing_with_pauses("   and the break statements are just wishful thinking...")

    play_with_wait(CORRUPTION_1)
