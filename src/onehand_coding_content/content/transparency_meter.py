import time
import random

from ..config import LINE_LENGTH
from ..sounds import play_sound, play_with_wait, NEVER_BACKDOWN, KEYPRESS_SOUND
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
        print("="*LINE_LENGTH)
        typewriter_effect("📊 PHILIPPINE GOVERNMENT TRANSPARENCY METER")
        print("="*LINE_LENGTH)
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
            typing_with_pauses(f"   ⏳ {step}")
            time.sleep(1.5)

        typing_with_pauses("\n✅ System initialized!")
        dramatic_pause(1)
        typing_with_pauses("⚠️  Warning: Display may be stuck. Have tried turning it off and on again.")

    def check_transparency(self, category):
        """Check transparency level for different categories"""
        typewriter_effect(f"\n📋 Checking transparency for: {category}")
        print("-"*LINE_LENGTH)
        dramatic_pause(1)

        # Simulate "checking"
        typing_with_pauses("🔍 Analyzing data...")
        dramatic_pause(1.5)
        typing_with_pauses("🧮 Calculating metrics...")
        dramatic_pause(1.5)
        typing_with_pauses("📊 Generating report...")
        dramatic_pause(1.5)

        # Result is always the same
        typing_with_pauses(f"\n📈 Transparency Level: {self.transparency_level}%")

        # Progress bar stuck at 0
        print("\nProgress: [", end="")
        for i in range(20):
            print("░", end="", flush=True)
            time.sleep(0.1)
        print("] 0%")
        play_sound(KEYPRESS_SOUND)

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
            ("Performance Metrics", "How are we actually doing?"),
            ("ICI Investigation Transparency", "ICI Investigation: Public live feed, or another state secret?")
        ]

        print("\n" + "="*LINE_LENGTH)
        typewriter_effect("🔍 COMPREHENSIVE TRANSPARENCY AUDIT")
        print("="*LINE_LENGTH)
        dramatic_pause(2)

        for category, question in categories:
            typing_with_pauses(f"\n📂 Category: {category}")
            typing_with_pauses(f"❓ Question: {question}")
            dramatic_pause(1)

            typing_with_pauses("🔄 Processing request...")
            dramatic_pause(2)

            typing_with_pauses(f"📊 Transparency Score: {self.transparency_level}%")
            typing_with_pauses("🚫 Status: Information not available")
            excuse = random.choice(self.excuses_list)
            typing_with_pauses(f"📌 Reason: {excuse}")
            time.sleep(1.5)

    def attempt_to_fix(self):
        """Try to fix the stuck meter (spoiler: it won't work)"""
        print("\n" + "="*LINE_LENGTH)
        typewriter_effect("🔧 ATTEMPTING TO REPAIR TRANSPARENCY METER...")
        print("="*LINE_LENGTH)
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
            typing_with_pauses(f"\n🔄 {attempt}...")
            dramatic_pause(2)

            # Fake progress
            print("   [", end="", flush=True)
            for i in range(10):
                print("▓", end="", flush=True)
                time.sleep(0.2)
            print("] Done")

            if success:
                typing_with_pauses("   ✅ Success!")
            else:
                typing_with_pauses("   ❌ Failed. Meter still at 0%")

            time.sleep(0.8)

        typing_with_pauses("\n🤷 DIAGNOSIS:")
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
        print("\n" + "="*LINE_LENGTH)
        typewriter_effect("📬 PROCESSING FREEDOM OF INFORMATION REQUESTS")
        print("="*LINE_LENGTH)
        dramatic_pause(1)

        requests = [
            "Request #0521: List of project contractors",
            "Request #0847: Detailed budget breakdown",
            "Request #1293: Travel expenses of officials",
            "Request #1888: Meeting transcripts",
            "Request #2456: Performance evaluations",
            "Request #301: Real-time updates on the ICI investigation"
        ]

        satirical_responses = [
            "'After the next 3 elections'",
            "'Once the documents are declassified in 2099'",
            "'When pigs fly, or when traffic in EDSA is clear'",
            "'We have received your request. Please expect a reply within 3-5 business centuries.'",
            "'Currently under review by the Committee for Making Things Sound Complicated.'",
            "'Your request is being processed. In the meantime, please enjoy this complimentary picture of a smiling politician.'",
            "'File not found. Have you tried looking under the rug?'"
        ]

        satirical_waiting_days = [
            "999+ days",
            "Error: Integer overflow",
            "404 days not found",
            "Still counting...",
            "Ask again tomorrow",
            "Since the dawn of time",
            "Pending since last administration"
        ]

        for request in requests:
            typing_with_pauses(f"\n📥 {request}")
            time.sleep(0.8)
            typing_with_pauses("   Status: Pending")
            time.sleep(0.8)
            days_waiting = random.choice(satirical_waiting_days)
            typing_with_pauses(f"   Days waiting: {days_waiting}")
            time.sleep(0.8)
            response = random.choice(satirical_responses)
            typing_with_pauses(f"   Expected response: {response}")
            time.sleep(1.5)

        typing_with_pauses("\n💬 Auto-reply:")
        typing_with_pauses("   'Your request has been received and is being processed.'")
        dramatic_pause(1)
        typing_with_pauses("   'Please expect a response within 15-30 working days.'")
        dramatic_pause(1)
        typing_with_pauses("   'Thank you for your patience.'")
        dramatic_pause(2)
        typing_with_pauses("\n🤦 *Citizens still waiting ...*")


def main():
    """Main entry point."""
    meter = TransparencyMeter()

    # Initialize
    meter.initialize_system()

    # Check specific category
    meter.check_transparency("Government Project Expenses")

    # Test all categories
    meter.test_all_categories()

    # Show citizen requests
    meter.citizen_requests()

    # Try to fix
    meter.attempt_to_fix()

    print("\n" + "="*LINE_LENGTH)
    typewriter_effect("📉 OVERALL TRANSPARENCY INDEX: 0%")
    print("="*LINE_LENGTH)
    dramatic_pause(1)
    typing_with_pauses("\n🏆 Achievement Unlocked: 'Consistent Performance!'")

    # Final message
    print("\n" + "="*LINE_LENGTH)
    typing_with_pauses("🎭 SYSTEM SUMMARY")
    print("="*LINE_LENGTH)
    typing_with_pauses("📊 Transparency Meter: 0% (functioning normally)")
    typing_with_pauses("📝 Excuses Generated: Unlimited")
    typing_with_pauses("⏰ Avg Response Time: ∞")
    typing_with_pauses("🤷 Accountability Level: 404 Not Found")
    print("="*LINE_LENGTH)

    dramatic_pause(2)
    typing_with_pauses("\n💭 'Sunshine is the best disinfectant' - Louis Brandeis")
    dramatic_pause(1)
    typing_with_pauses("🌑 'Good thing we're allergic to sunshine' - PH Gov't, probably")

    typing_with_pauses("\n\n# while transparency == 0:")
    typing_with_pauses("#     promises += 1")
    typing_with_pauses("#     accountability -= 1")

    play_with_wait(NEVER_BACKDOWN)


# Run the simulation
if __name__ == "__main__":
    main()
