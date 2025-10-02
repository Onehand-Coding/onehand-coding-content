import time
import random
from datetime import datetime
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause

class FloodDetectionSystem:
    """
    State-of-the-art Flood Monitoring System
    Cost: ₱500M | Efficacy: TBD
    "Tested and proven effective!" (during inauguration only)
    """

    def __init__(self):
        self.is_rainy_season = self._check_season()
        self.system_status = "OPERATIONAL*"
        typing_with_pauses("🌊 PHILIPPINE FLOOD EARLY WARNING SYSTEM v1.0", delay=0.03)
        print("="*55)
        dramatic_pause(1)

    def _check_season(self):
        """Check if it's actually rainy season"""
        month = datetime.now().month
        # June to November = rainy season
        return 6 <= month <= 11

    def check_system_health(self):
        """System diagnostics (spoiler: meron issue)"""
        typewriter_effect("\n🔧 Running system diagnostics...")
        dramatic_pause(2)

        if self.is_rainy_season:
            issues = [
                "⚠️  Sensor #1-12: OFFLINE (baha daw yung sensor)",
                "⚠️  Network Connection: UNSTABLE (natanggal yung cable ng baha)",
                "⚠️  Backup Power: DEPLETED (ginamit sa Christmas party)",
                "⚠️  Database Server: ERROR 404 (404: Funds not found)"
            ]

            for issue in issues:
                typing_with_pauses(issue)
                time.sleep(0.5)

            typewriter_effect("\n❌ System Status: CRITICAL FAILURE")
            typing_with_pauses("📝 Recommendation: 'Under maintenance. Check back next year.'")

        else:
            typewriter_effect("✅ All systems operational!")
            typewriter_effect("✅ All sensors responding perfectly!")
            typewriter_effect("✅ Network: 100% uptime!")
            typewriter_effect("✅ Data accuracy: 99.9%!")
            dramatic_pause(1)
            typewriter_effect("\n🎉 System Status: EXCELLENT")
            typing_with_pauses("📸 *Perfect time for media coverage*")

    def detect_flood(self, water_level_cm):
        """Flood detection algorithm (very sophisticated)"""
        typewriter_effect(f"\n\n📡 Detecting flood conditions...")
        typewriter_effect(f"💧 Current water level: {water_level_cm} cm")
        dramatic_pause(2)

        if self.is_rainy_season:
            typewriter_effect("\n🤖 System response:")
            dramatic_pause(1)
            typing_with_pauses("   'ERROR: Cannot process request'")
            dramatic_pause(1)
            typing_with_pauses("   'Sensor malfunction detected'")
            dramatic_pause(1)
            typing_with_pauses("   'Please try again later (next year)'")
            dramatic_pause(2)

            typewriter_effect("\n📱 Meanwhile, citizens:")
            typewriter_effect("   🏊 Already swimming on EDSA")
            typewriter_effect("   📸 Posting #WalangPasok selfies")
            typing_with_pauses("   😤 Trending: #SaanAngBudget")

        else:
            # Works perfectly when there's no flood
            if water_level_cm < 10:
                level = "SAFE ✅"
                action = "Enjoy the weather!"
            elif water_level_cm < 30:
                level = "MONITOR 🟡"
                action = "Stay alert!"
            else:
                level = "DANGER 🔴"
                action = "Evacuate immediately!"

            dramatic_pause(1)
            typing_with_pauses(f"\n🚨 Alert Level: {level}")
            typing_with_pauses(f"📢 Recommended Action: {action}")
            typewriter_effect("\n✨ System working flawlessly!")
            typing_with_pauses("👨‍💼 *Officials taking photos for press release*")

    def generate_report(self):
        """Monthly performance report for COA"""
        print("\n\n" + "="*55)
        typing_with_pauses("📊 MONTHLY PERFORMANCE REPORT", delay=0.03)
        print("="*55)
        dramatic_pause(1)

        if self.is_rainy_season:
            uptime = random.uniform(5, 15)
            typewriter_effect(f"⏱️  System Uptime: {uptime:.1f}%")
            typewriter_effect(f"✅ Successful Detections: 0")
            typing_with_pauses(f"❌ Failed Detections: Lost count (database baha)")
            typewriter_effect(f"💸 Budget Utilized: 98% (remaining 2% = 'savings')")
            dramatic_pause(1)
            typing_with_pauses("\n📝 Notes: 'Equipment needs upgrade (additional ₱300M)'")

        else:
            uptime = random.uniform(95, 99.9)
            typewriter_effect(f"⏱️  System Uptime: {uptime:.1f}%")
            typewriter_effect(f"✅ Successful Detections: 1,247")
            typewriter_effect(f"❌ Failed Detections: 0")
            typewriter_effect(f"💸 Budget Utilized: 100%")
            dramatic_pause(1)
            typewriter_effect("\n🏆 Status: EXCEEDS EXPECTATIONS")
            typing_with_pauses("🎖️  Team to receive Performance Bonus!")


# Run the simulation
if __name__ == "__main__":
    system = FloodDetectionSystem()

    typewriter_effect(f"\n📅 Current season: {'🌧️  RAINY' if system.is_rainy_season else '☀️  DRY'}")
    dramatic_pause(1)

    # Check system health
    system.check_system_health()

    # Try to detect flood
    water_level = 85 if system.is_rainy_season else 5
    system.detect_flood(water_level)

    # Generate report
    system.generate_report()

    print("\n\n" + "="*55)
    typing_with_pauses("💬 Official Statement:")
    typing_with_pauses("   'The system is working as intended.'")
    dramatic_pause(1)
    typing_with_pauses("\n🤔 Citizens: 'Intended for what exactly?'")
    print("="*55)
