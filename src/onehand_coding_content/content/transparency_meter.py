import time
import random

import pygame

from ..sounds import play_sound, NEVER_BACKDOWN
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause

class TransparencyMeter:
    """
    Official Government Transparency Index™
    "Measuring our commitment to openness!"
    (Spoiler: Sira yung measuring device)
    """

    def __init__(self):
        self.transparency_level = 0  # Hardcoded for accuracy
        self.excuses_list = [
            "Executive privilege",
            "National security concerns",
            "Ongoing investigation",
            "Confidential by nature",
            "Not yet the proper time",
            "Under review by legal team",
            "Protecting sources",
            "Sub judice",
            "Privacy concerns"
        ]

        print()
        print("="*60)
        typing_with_pauses("📊 PHILIPPINE GOVERNMENT TRANSPARENCY METER", delay=0.03)
        print("="*60)
        dramatic_pause(1)

    def initialize_system(self):
        """Boot up the transparency monitoring system"""
        typewriter_effect("\n🔧 Initializing Transparency Monitoring System...")
        dramatic_pause(2)

        steps = [
            "Loading transparency protocols...",
            "Connecting to public database...",
            "Retrieving accountability records...",
            "Calculating openness index...",
        ]

        for step in steps:
            typewriter_effect(f"   ⏳ {step}")
            time.sleep(1.5)

        typewriter_effect("\n✅ System initialized!")
        dramatic_pause(1)
        typing_with_pauses("⚠️  Warning: Display may be stuck. Have tried turning it off and on again.")

    def check_transparency(self, category):
        """Check transparency level for different categories"""
        typewriter_effect(f"\n\n📋 Checking transparency for: {category}")
        print("-"*60)
        dramatic_pause(1)

        # Simulate "checking"
        typewriter_effect("🔍 Analyzing data...")
        dramatic_pause(2)
        typewriter_effect("🧮 Calculating metrics...")
        dramatic_pause(2)
        typewriter_effect("📊 Generating report...")
        dramatic_pause(2)

        # Result is always the same
        typewriter_effect(f"\n📈 Transparency Level: {self.transparency_level}%")

        # Progress bar stuck at 0
        print("\nProgress: [", end="")
        for i in range(20):
            print("░", end="", flush=True)
            time.sleep(0.1)
        print("] 0%")

        dramatic_pause(1)
        excuse = random.choice(self.excuses_list)
        typing_with_pauses(f"\n❌ Reason: '{excuse}'")
        dramatic_pause(1)
        typing_with_pauses("📝 Official statement: 'We value transparency and will release information soon™'")
        dramatic_pause(1)

    def test_all_categories(self):
        """Test transparency across all government categories"""
        categories = [
            ("Budget Allocation", "Where did the ₱billions go?"),
            ("Project Contracts", "Who got the deal and why?"),
            ("Official Expenses", "SALN? What SALN?"),
            ("Meeting Minutes", "Who decided what?"),
            ("Audit Reports", "COA findings? Never heard of her"),
            ("Performance Metrics", "How are we actually doing?")
        ]

        print("\n\n" + "="*60)
        typewriter_effect("\n\n🔍 COMPREHENSIVE TRANSPARENCY AUDIT")
        print("="*60)
        dramatic_pause(2)

        for category, question in categories:
            typewriter_effect(f"\n\n📂 Category: {category}")
            typing_with_pauses(f"❓ Question: {question}")
            dramatic_pause(1)

            typewriter_effect("🔄 Processing request...")
            dramatic_pause(2)

            typewriter_effect(f"📊 Transparency Score: {self.transparency_level}%")
            typewriter_effect(f"🚫 Status: Information not available")
            excuse = random.choice(self.excuses_list)
            typing_with_pauses(f"📌 Reason: {excuse}")
            time.sleep(1.5)

        print("\n\n" + "="*60)
        typing_with_pauses("📉 OVERALL TRANSPARENCY INDEX: 0%", delay=0.04)
        print("="*60)
        dramatic_pause(1)
        typing_with_pauses("\n🏆 Achievement Unlocked: 'Consistent Performance!'")

    def attempt_to_fix(self):
        """Try to fix the stuck meter (spoiler: it won't work)"""
        print("\n\n" + "="*60)
        typewriter_effect("\n\n🔧 ATTEMPTING TO REPAIR TRANSPARENCY METER...")
        print("="*60)
        dramatic_pause(2)

        attempts = [
            ("Recalibrating sensors", False),
            ("Updating algorithms", False),
            ("Clearing cache", False),
            ("Restarting system", False),
            ("Calling IT support", False),
            ("Performing factory reset", False),
            ("Consulting manual", False),
            ("Praying to tech gods", False),
        ]

        for attempt, success in attempts:
            typewriter_effect(f"\n🔄 {attempt}...")
            dramatic_pause(2)

            # Fake progress
            print("   [", end="", flush=True)
            for i in range(10):
                print("▓", end="", flush=True)
                time.sleep(0.2)
            print("] Done")

            if success:
                typewriter_effect("   ✅ Success!")
            else:
                typing_with_pauses("   ❌ Failed. Meter still at 0%")

            time.sleep(0.8)

        typewriter_effect("\n\n🤷 DIAGNOSIS:")
        dramatic_pause(1)
        typing_with_pauses("   Technical Issue: Meter is not broken.")
        dramatic_pause(1)
        typing_with_pauses("   Root Cause: It's working perfectly.")
        dramatic_pause(1)
        typing_with_pauses("   Transparency level is actually 0%.")
        dramatic_pause(2)
        typing_with_pauses("\n   💡 'It's not a bug, it's a feature!' - System Engineer")

    def citizen_requests(self):
        """Simulate citizen FOI requests"""
        print("\n\n" + "="*60)
        typewriter_effect("\n\n📬 PROCESSING FREEDOM OF INFORMATION REQUESTS")
        print("="*60)
        dramatic_pause(1)

        requests = [
            "Request #0521: List of project contractors",
            "Request #0847: Detailed budget breakdown",
            "Request #1293: Travel expenses of officials",
            "Request #1888: Meeting transcripts",
            "Request #2456: Performance evaluations"
        ]

        for request in requests:
            typewriter_effect(f"\n📥 {request}")
            time.sleep(0.8)
            typewriter_effect("   Status: Pending")
            time.sleep(0.8)
            typewriter_effect("   Days waiting: 547 days")
            time.sleep(0.8)
            typing_with_pauses("   Expected response: '15-30 working days' (narrator: it's been years)")
            time.sleep(1.5)

        typewriter_effect("\n\n💬 Auto-reply:")
        typing_with_pauses("   'Your request has been received and is being processed.'")
        dramatic_pause(1)
        typing_with_pauses("   'Please expect a response within 15-30 working days.'")
        dramatic_pause(1)
        typing_with_pauses("   'Thank you for your patience.'")
        dramatic_pause(2)
        typing_with_pauses("\n🤦 *Citizens still waiting ...*")


# Run the simulation
if __name__ == "__main__":
    meter = TransparencyMeter()

    # Initialize
    meter.initialize_system()

    # Check specific category
    meter.check_transparency("Government Project Expenses")

    # Test all categories
    meter.test_all_categories()

    # Try to fix
    meter.attempt_to_fix()

    # Show citizen requests
    meter.citizen_requests()

    # Final message
    print("\n\n" + "="*60)
    typing_with_pauses("🎭 SYSTEM SUMMARY", delay=0.03)
    print("="*60)
    typewriter_effect("📊 Transparency Meter: 0% (functioning normally)")
    typewriter_effect("📝 Excuses Generated: Unlimited")
    typewriter_effect("⏰ Avg Response Time: ∞")
    typewriter_effect("🤷 Accountability Level: 404 Not Found")
    print("="*60)

    dramatic_pause(2)
    typing_with_pauses("\n💭 'Sunshine is the best disinfectant' - Louis Brandeis")
    dramatic_pause(1)
    typing_with_pauses("🌑 'Good thing we're allergic to sunshine' - PH Gov't, probably")

    typewriter_effect("\n\n# while transparency == 0:")
    typewriter_effect("#     promises += 1")
    typewriter_effect("#     accountability -= 1")

    play_sound(NEVER_BACKDOWN)

    # Lets wait for the final sound to finish playing.
    import pygame.mixer
    while pygame.mixer.get_busy():
            pygame.time.wait(100)
