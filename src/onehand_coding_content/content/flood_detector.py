import time
import random
from datetime import datetime

from ..sounds import play_with_wait, CORRUPTION_3
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause

class FloodControlRealityCheck:
    """
    Philippine Flood Control System Status Monitor
    ₱500B+ spent (2022-2025) | Still Flooding: Yes
    "Infrastructure-based solution daw!"
    """

    def __init__(self):
        self.budget_spent = 500_000_000_000  # ₱500B+ on flood control
        self.recent_casualties = 30  # July 2025 monsoon floods
        self.affected_people = 8_000_000  # 8M affected in recent floods
        self.projects_built = "thousands"
        self.bulacan_still_flooded = True  # Most projects built here, still floods

        print("\n" + "="*70)
        typing_with_pauses("🌊 PHILIPPINE FLOOD CONTROL REALITY CHECK SYSTEM", delay=0.03)
        print("="*70)
        print()
        typing_with_pauses("'₱500B+ invested. Still baha. Curious.' 🤔")
        dramatic_pause(2)

    def check_investment_vs_reality(self):
        """Compare what we spent vs what we got"""
        print("\n📊 INVESTMENT ANALYSIS (2022-2025):")
        print("-"*70)
        dramatic_pause(1)

        typewriter_effect(f"💰 Total Spent on Flood Control: ₱{self.budget_spent:,.2f}")
        time.sleep(1)
        typewriter_effect(f"🏗️  Projects Claimed Built: {self.projects_built}")
        time.sleep(1)
        typewriter_effect(f"📍 Priority Area: Bulacan (most projects)")
        dramatic_pause(2)

        typewriter_effect("\n📈 Expected Outcome:")
        typewriter_effect("   ✅ Reduced flooding")
        typewriter_effect("   ✅ Fewer casualties")
        typewriter_effect("   ✅ Better warnings")
        typewriter_effect("   ✅ Protected communities")
        dramatic_pause(2)

        typewriter_effect("\n📉 Actual Outcome (2025):")
        dramatic_pause(1)
        typing_with_pauses(f"   ❌ July 2025 Floods: {self.recent_casualties} deaths")
        time.sleep(1)
        typing_with_pauses(f"   ❌ People Affected: {self.affected_people:,}+")
        time.sleep(1)
        typing_with_pauses(f"   ❌ Bulacan Status: STILL FLOODING (despite most projects)")
        time.sleep(1)
        typing_with_pauses("   ❌ Projects Status: Overpriced, unfinished, mismatched")
        dramatic_pause(2)

        typewriter_effect("\n🧮 Quick Math:")
        dramatic_pause(1)
        cost_per_person = self.budget_spent / self.affected_people
        typing_with_pauses(f"   ₱500B ÷ 8M affected = ₱{cost_per_person:,.2f} per person")
        dramatic_pause(1)
        typing_with_pauses("   Question: Did each person get ₱62,500 worth of flood protection?")
        dramatic_pause(2)
        typing_with_pauses("   Answer: *Awkward silence* 🦗")

    def simulate_flood_event(self, location="Bulacan"):
        """Simulate a flood event with 'working' infrastructure"""
        print("\n\n" + "="*70)
        typing_with_pauses(f"⚠️  SIMULATING FLOOD EVENT: {location.upper()}", delay=0.03)
        print("="*70)
        dramatic_pause(2)

        typewriter_effect("\n🌧️  Heavy rainfall detected...")
        dramatic_pause(1)
        typewriter_effect("📊 Rainfall: 200mm in 6 hours")
        typewriter_effect("💧 Water level: RISING RAPIDLY")
        dramatic_pause(2)

        typewriter_effect("\n🏗️  Checking flood control infrastructure...")
        dramatic_pause(2)

        # Check the "infrastructure"
        issues = [
            ("River wall project", "❌ INCOMPLETE (budget disbursed though)"),
            ("Drainage system", "❌ CLOGGED (no maintenance budget?)"),
            ("Flood gates", "❌ STUCK (rusted, di gumagana)"),
            ("Warning system", "❌ OFFLINE (walang load ang SIM)"),
            ("Pumping stations", "❌ NO POWER (brownout, naturally)")
        ]

        typewriter_effect("\n📋 Infrastructure Status Check:")
        for infrastructure, status in issues:
            time.sleep(1)
            typewriter_effect(f"   • {infrastructure}: ", end_with_newline=False)
            time.sleep(0.5)
            typing_with_pauses(status)

        dramatic_pause(2)

        typewriter_effect("\n⚠️  SYSTEM STATUS: CRITICAL")
        dramatic_pause(1)
        typewriter_effect("🚨 Flood Alert Level: RED")
        dramatic_pause(1)
        typing_with_pauses("📢 Official Warning: 'Prepare to evacuate!'")
        dramatic_pause(2)

        typewriter_effect("\n📱 Meanwhile in reality:")
        time.sleep(1)
        typing_with_pauses("   🏊 EDSA: Closed. Swimming pool na.")
        time.sleep(1)
        typing_with_pauses("   🚗 NLEX: Parking lot ng baha")
        time.sleep(1)
        typing_with_pauses("   🏠 Bulacan: Residents on rooftops (again)")
        time.sleep(1)
        typing_with_pauses("   📸 Social Media: #WalangPasok trending")
        time.sleep(1)
        typing_with_pauses("   😤 Citizens: 'San yung ₱500B?!'")
        dramatic_pause(2)

    def project_quality_check(self):
        """Check the quality of completed projects"""
        print("\n\n" + "="*70)
        typing_with_pauses("🔍 PROJECT QUALITY ASSESSMENT", delay=0.03)
        print("="*70)
        dramatic_pause(2)

        typewriter_effect("\n🏗️  Inspecting completed flood control projects...")
        dramatic_pause(2)

        findings = [
            {
                "issue": "OVERPRICED CONTRACTS",
                "details": "₱55M for 300m river wall. International price: ₱15M",
                "response": "'Market rates daw' - Contractor"
            },
            {
                "issue": "UNFINISHED STRUCTURES",
                "details": "50% complete pero 100% bayad na",
                "response": "'On-going pa daw' - Since 2022"
            },
            {
                "issue": "MISMATCHED TO FLOOD RISKS",
                "details": "Built protection sa areas na hindi naman binabaha",
                "response": "'Engineering decision daw' - DPWH"
            },
            {
                "issue": "SUBSTANDARD MATERIALS",
                "details": "Designed for 50 years, damaged after 6 months",
                "response": "'Act of God daw' - Contractor"
            },
            {
                "issue": "GHOST PROJECTS",
                "details": "Exists in spreadsheet, not on ground",
                "response": "'Under investigation' - COA (since 2025)"
            }
        ]

        for finding in findings:
            typewriter_effect(f"\n⚠️  {finding['issue']}")
            time.sleep(0.8)
            typing_with_pauses(f"   📌 Finding: {finding['details']}")
            time.sleep(0.8)
            typing_with_pauses(f"   💬 Official Response: {finding['response']}")
            dramatic_pause(1.5)

        dramatic_pause(2)
        typewriter_effect("\n🏆 Overall Rating: FAILS TO PROTECT THE POOR")
        dramatic_pause(1)
        typing_with_pauses("📝 Conclusion: 'Money spent. People still flooding.' - Advocacy Groups")

    def economic_impact(self):
        """Show the broader economic damage"""
        print("\n\n" + "="*70)
        typing_with_pauses("💸 ECONOMIC IMPACT ANALYSIS", delay=0.03)
        print("="*70)
        dramatic_pause(2)

        typewriter_effect("\n📊 DIRECT COSTS:")
        typewriter_effect("   • Flood control budget (2022-2025): ₱500B+")
        time.sleep(1)
        typewriter_effect("   • Estimated ghost projects: ₱118B")
        time.sleep(1)
        typewriter_effect("   • Cost overruns & corruption: ₱200B+ (estimated)")
        dramatic_pause(2)

        typewriter_effect("\n📉 CONSEQUENCE COSTS:")
        typewriter_effect("   • Stock market: -1.5% (7-day drop, 5-month low)")
        time.sleep(1)
        typewriter_effect("   • Philippine peso: Weakened significantly")
        time.sleep(1)
        typewriter_effect("   • South Korea loan: $503M SUSPENDED")
        time.sleep(1)
        typewriter_effect("   • Predicted losses (2022-2050): $124B from floods")
        dramatic_pause(2)

        typewriter_effect("\n😔 HUMAN COSTS (July 2025 alone):")
        typewriter_effect(f"   • Deaths: {self.recent_casualties}")
        time.sleep(1)
        typewriter_effect("   • Affected: 8M+ people")
        time.sleep(1)
        typewriter_effect("   • Displaced: Thousands")
        time.sleep(1)
        typewriter_effect("   • Homes damaged: Thousands")
        dramatic_pause(2)

        typing_with_pauses("\n💭 Reality Check:")
        typing_with_pauses("   'We spent ₱500B+ to PREVENT this.'")
        dramatic_pause(1)
        typing_with_pauses("   'Instead, we got scandals and still-flooded streets.'")
        dramatic_pause(2)

    def solutions_vs_reality(self):
        """Compare proposed solutions vs what actually helps"""
        print("\n\n" + "="*70)
        typing_with_pauses("🎯 SOLUTIONS: PROPOSED VS REALITY", delay=0.03)
        print("="*70)
        dramatic_pause(2)

        typewriter_effect("\n🏛️  GOVERNMENT APPROACH: Infrastructure Only")
        typewriter_effect("   Strategy: Build concrete structures")
        typewriter_effect("   Budget: ₱500B+ (and counting)")
        typewriter_effect("   Result: Still flooding + corruption scandals")
        dramatic_pause(2)

        typewriter_effect("\n🌍 WHAT EXPERTS RECOMMEND: Holistic Approach")
        expert_solutions = [
            "Nature-based solutions (mangroves, wetlands)",
            "Community-based early warning systems",
            "Better urban planning and zoning",
            "Climate change adaptation strategies",
            "Transparent and accountable spending",
            "Maintenance budget for existing structures"
        ]

        for solution in expert_solutions:
            typing_with_pauses(f"   • {solution}")
            time.sleep(1)

        dramatic_pause(2)
        typewriter_effect("\n🤷 Government Response to Expert Recommendations:")
        dramatic_pause(1)
        typing_with_pauses("   'Noted. Anyway, here's another concrete project...'")
        dramatic_pause(2)

        typewriter_effect("\n💡 WHAT ACTUALLY HELPED (July 2025 floods):")
        typewriter_effect("   ✅ Bayanihan spirit (neighbors helping neighbors)")
        typewriter_effect("   ✅ Social media warnings (faster than official)")
        typewriter_effect("   ✅ NGO & volunteer rescue operations")
        typewriter_effect("   ✅ Community-organized evacuations")
        dramatic_pause(2)

        typing_with_pauses("\n📌 Pattern: 'Government builds. Nature destroys. People survive.'")

    def generate_final_report(self):
        """Devastating final summary"""
        print("\n\n" + "="*70)
        typing_with_pauses("📋 FINAL VERDICT: THE NUMBERS DON'T LIE", delay=0.03)
        print("="*70)
        dramatic_pause(2)

        typewriter_effect("\n✅ CLAIMED ACCOMPLISHMENTS:")
        typewriter_effect("   • Thousands of projects built")
        typewriter_effect("   • ₱500B+ invested in flood control")
        typewriter_effect("   • 'Best infrastructure in SEA' - Officials")
        dramatic_pause(2)

        typewriter_effect("\n❌ ACTUAL SITUATION:")
        typewriter_effect("   • Bulacan (most projects): STILL FLOODING")
        typewriter_effect("   • Metro Manila: Business as usual (baha)")
        typewriter_effect("   • July 2025: 30 dead, 8M affected")
        typewriter_effect("   • ₱118B+ in ghost projects exposed")
        typewriter_effect("   • International loans suspended")
        typewriter_effect("   • Stock market tanking")
        typewriter_effect("   • Poor communities: Still unprotected")
        dramatic_pause(2)

        typewriter_effect("\n🎭 THE PATTERN:")
        time.sleep(1)
        typing_with_pauses("   1. Announce mega flood control project")
        time.sleep(1)
        typing_with_pauses("   2. Award to 'preferred' contractors")
        time.sleep(1)
        typing_with_pauses("   3. Overpriced, substandard, or ghost")
        time.sleep(1)
        typing_with_pauses("   4. Floods happen anyway")
        time.sleep(1)
        typing_with_pauses("   5. Announce NEW mega project")
        time.sleep(1)
        typing_with_pauses("   6. Repeat cycle")
        dramatic_pause(3)

        typewriter_effect("\n💬 VOICES:")
        dramatic_pause(1)
        typing_with_pauses("   Advocates: 'Flood control projects fail the poor'")
        time.sleep(1)
        typing_with_pauses("   Economists: 'Systemic corruption in infrastructure'")
        time.sleep(1)
        typing_with_pauses("   Citizens: 'San napunta yung pera?!'")
        time.sleep(1)
        typing_with_pauses("   Officials: 'We are investigating...' (always)")
        dramatic_pause(3)

        print("\n" + "="*70)
        typing_with_pauses("🌊 BOTTOM LINE:", delay=0.04)
        print("="*70)
        dramatic_pause(1)
        typing_with_pauses("₱500 BILLION spent.", delay=0.04)
        dramatic_pause(1)
        typing_with_pauses("People STILL drowning.", delay=0.04)
        dramatic_pause(1)
        typing_with_pauses("Politicians STILL profiting.", delay=0.04)
        dramatic_pause(2)
        typing_with_pauses("\n'It's not a bug. It's the system.' 🎭", delay=0.03)


# Demo usage
if __name__ == "__main__":
    system = FloodControlRealityCheck()

    # Show investment vs reality
    system.check_investment_vs_reality()

    # Simulate actual flood event
    system.simulate_flood_event("Bulacan")

    # Quality check of projects
    system.project_quality_check()

    # Economic impact
    system.economic_impact()

    # Solutions comparison
    system.solutions_vs_reality()

    # Final devastating report
    system.generate_final_report()

    print("\n\n" + "="*70)
    typing_with_pauses("💭 FINAL THOUGHT", delay=0.03)
    print("="*70)
    dramatic_pause(2)

    typing_with_pauses("'We don't have a flood problem.'")
    dramatic_pause(1)
    typing_with_pauses("'We have a corruption problem that causes floods.'")
    dramatic_pause(2)

    typewriter_effect("\n\n# while True:")
    typewriter_effect("#     government.announce_project()")
    typewriter_effect("#     contractors.overcharge()")
    typewriter_effect("#     floods.continue()")
    typewriter_effect("#     people.suffer()")
    typewriter_effect("#     accountability = None")

    play_with_wait(CORRUPTION_3)
