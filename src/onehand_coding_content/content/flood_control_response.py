import time
from datetime import date

from ..sounds import play_with_wait, NO_PROMISES, DELAY
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause


class IndependentCommission:
    def __init__(self):
        self.name = "Independent Commission for Infrastructure"
        self.created_date = date(2025, 9, 11)
        self.appointed_by = "President Marcos"
        self.billions_lost = 118.5
        self.officials_jailed = 0
        self.has_contempt_power = False
        self.hearings_public = False  # KEY ISSUE
        self.days_active = (date.today() - self.created_date).days

    def check_independence(self):
        typewriter_effect("\n🔍 Checking Independence...")
        dramatic_pause(2)

        typing_with_pauses("   ⚠️  Appointed by: President Marcos")
        typing_with_pauses("   ⚠️  Investigating: Same administration")
        typing_with_pauses("   ⚠️  Marcos cousin implicated: Yes")
        time.sleep(1.5)

        typing_with_pauses("\n   ❌ Independence Score: QUESTIONABLE")
        print()
        time.sleep(1)

    def check_transparency(self):
        typewriter_effect("\n👁️  Checking Transparency...")
        dramatic_pause(2)

        # The bombshell
        print("\n" + "="*60)
        typing_with_pauses("🚨 TRANSPARENCY STATUS 🚨")
        print("="*60)
        typing_with_pauses("   ❌ HEARINGS: CLOSED DOOR")
        typing_with_pauses("   ❌ Media Access: Press releases only")
        typing_with_pauses("   ❌ Livestream: Not allowed")
        typing_with_pauses("   ❌ Public Monitoring: Blocked")
        print("="*60)
        time.sleep(2)

        # Public sentiment with typewriter
        typing_with_pauses("\n📢 Public Sentiment:")
        time.sleep(0.5)

        sentiments = [
            ("Justice Carpio", "People will lose faith in the ICI"),
            ("Sen. Pangilinan", "Decision is ill-advised, open it!"),
            ("Agot Isidro", "Taxpayers fund this, we should see it"),
            ("People's Budget Coalition", "Transparency = Trust"),
            ("Former Ombudsman Morales", "Hearings should be public"),
            ("Netizens", "Kung walang tinatago, bakit takot ipakita sa publiko?")
        ]

        for person, quote in sentiments:
            typing_with_pauses(f"   • {person}: '{quote}'")
            time.sleep(0.8)

        dramatic_pause(2)

        # The punchline with dramatic typing
        typing_with_pauses(
            "\n   🤔 ICI's Response: 'Ayaw namin ng trial by publicity'",

        )
        time.sleep(1)
        typing_with_pauses(
            "   💭 Translation: 'Ayaw namin ng accountability' 🙃\n",

        )
        time.sleep(1.5)

    def check_effectiveness(self):
        typewriter_effect("\n⚖️  Effectiveness Report:")
        dramatic_pause(1)

        metrics = [
            ("Days Active", str(self.days_active), "⏰"),
            ("Billions Lost", f"₱{self.billions_lost}B", "💸"),
            ("Officials Jailed", str(self.officials_jailed), "❌"),
            ("Contempt Power", str(self.has_contempt_power), "❌"),
            ("Public Hearings", str(self.hearings_public), "❌")
        ]

        for metric, value, status in metrics:
            typing_with_pauses(f"   • {metric}: {value} {status}")
            time.sleep(0.5)
        time.sleep(2)

        # Translation with typewriter effect
        typing_with_pauses("\n💬 Translation:")
        time.sleep(0.5)
        typing_with_pauses(
            "   'Pwede kaming magtanong pero, kung ayaw sumagot, wala kaming magagawa.'"
        )
        typing_with_pauses(
            "   'Ah, at di nyo makikita yung hearing.' 🙈\n"
        )
        time.sleep(2)

        return "WALANG NGIPIN, WALANG TRANSPARENCY 🦷❌👁️❌"

    def predict_outcome(self):
        typewriter_effect("\n🔮 Based on Philippine History...\n")
        dramatic_pause(2)

        playbook = [
            ("Step 1", "Scandal exposes corruption", "✅"),
            ("Step 2", "Public outrage", "✅"),
            ("Step 3", "Government creates commission", "✅"),
            ("Step 4", "Close doors, kill transparency", "✅ <- ANDITO TAYO surprise!"),
            ("Step 5", "Media coverage fades", "⏳"),
            ("Step 6", "Report released (years later)", "⏳"),
            ("Step 7", "'Insufficient evidence'", "⏳"),
            ("Step 8", "No one goes to jail", "⏳"),
            ("Step 9", "Repeat cycle", "🔄")
        ]

        for step, desc, status in playbook:
            typing_with_pauses(f"   {step}: {desc} {status}")
            time.sleep(0.7)

        dramatic_pause(2)

        # Final statistics
        print("\n" + "="*60)
        typing_with_pauses("📊 STATISTICAL FORECAST")
        print("="*60)
        typing_with_pauses("   📈 Probability of actual jail time: 0.01%")
        typing_with_pauses("   📈 Probability ng 'nalimutan na': 99.99%")
        typing_with_pauses("   📈 Probability na closed door pa rin: 100%")
        print("="*60)
        time.sleep(2)


def main():
    """Entry point"""
    print()
    print("="*60)
    typewriter_effect("FLOOD CONTROL CORRUPTION: GOVERNMENT RESPONSE CHECK")
    print("="*60)
    print()

    commission = IndependentCommission()

    time.sleep(1)

    # Run checks
    commission.check_independence()
    time.sleep(1)

    commission.check_transparency()  # The transparency issue
    time.sleep(1)

    verdict = commission.check_effectiveness()

    print("\n" + "="*60)
    typing_with_pauses("🎯 VERDICT")
    print("="*60)
    typing_with_pauses(f"   {verdict}")
    print("="*60)
    dramatic_pause(2)

    commission.predict_outcome()
    dramatic_pause(2)

    # Footer with typewriter effect
    print("\n" + "="*60)
    typing_with_pauses("⏰ UPDATE KO KAYO PAG MAY:")
    print("="*60)
    typing_with_pauses("   1. Public hearings (hint: wag na mag-expect)")
    typing_with_pauses("   2. Actual jail time (good luck)")
    typing_with_pauses("   3. Transparency (press X to doubt)")
    print("="*60)

    print()

    play_with_wait(DELAY)
    play_with_wait(NO_PROMISES)

if __name__ == "__main__":
    main()
