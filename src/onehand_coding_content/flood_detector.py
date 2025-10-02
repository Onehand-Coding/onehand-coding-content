import time
import random
from datetime import datetime

class FloodDetectionSystem:
    """
    State-of-the-art Flood Monitoring System
    Cost: ₱500M | Efficacy: TBD
    "Tested and proven effective!" (during inauguration only)
    """

    def __init__(self):
        self.is_rainy_season = self._check_season()
        self.system_status = "OPERATIONAL*"
        print("🌊 PHILIPPINE FLOOD EARLY WARNING SYSTEM v1.0")
        print("="*55)
        time.sleep(1)

    def _check_season(self):
        """Check if it's actually rainy season"""
        month = datetime.now().month
        # June to November = rainy season
        return 6 <= month <= 11

    def check_system_health(self):
        """System diagnostics (spoiler: meron issue)"""
        print("\n🔧 Running system diagnostics...")
        time.sleep(2)

        if self.is_rainy_season:
            issues = [
                "⚠️  Sensor #1-12: OFFLINE (baha daw yung sensor)",
                "⚠️  Network Connection: UNSTABLE (natanggal yung cable ng baha)",
                "⚠️  Backup Power: DEPLETED (ginamit sa Christmas party)",
                "⚠️  Database Server: ERROR 404 (404: Funds not found)"
            ]

            for issue in issues:
                print(issue)
                time.sleep(1)

            print("\n❌ System Status: CRITICAL FAILURE")
            print("📝 Recommendation: 'Under maintenance. Check back next year.'")

        else:
            print("✅ All systems operational!")
            print("✅ All sensors responding perfectly!")
            print("✅ Network: 100% uptime!")
            print("✅ Data accuracy: 99.9%!")
            time.sleep(1)
            print("\n🎉 System Status: EXCELLENT")
            print("📸 *Perfect time for media coverage*")

    def detect_flood(self, water_level_cm):
        """Flood detection algorithm (very sophisticated)"""
        print(f"\n\n📡 Detecting flood conditions...")
        print(f"💧 Current water level: {water_level_cm} cm")
        time.sleep(2)

        if self.is_rainy_season:
            print("\n🤖 System response:")
            time.sleep(1)
            print("   'ERROR: Cannot process request'")
            time.sleep(1)
            print("   'Sensor malfunction detected'")
            time.sleep(1)
            print("   'Please try again later (next year)'")
            time.sleep(2)

            print("\n📱 Meanwhile, citizens:")
            print("   🏊 Already swimming on EDSA")
            print("   📸 Posting #WalangPasok selfies")
            print("   😤 Trending: #SaanAngBudget")

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

            time.sleep(1)
            print(f"\n🚨 Alert Level: {level}")
            print(f"📢 Recommended Action: {action}")
            print("\n✨ System working flawlessly!")
            print("👨‍💼 *Officials taking photos for press release*")

    def generate_report(self):
        """Monthly performance report for COA"""
        print("\n\n" + "="*55)
        print("📊 MONTHLY PERFORMANCE REPORT")
        print("="*55)
        time.sleep(1)

        if self.is_rainy_season:
            uptime = random.uniform(5, 15)
            print(f"⏱️  System Uptime: {uptime:.1f}%")
            print(f"✅ Successful Detections: 0")
            print(f"❌ Failed Detections: Lost count (database baha)")
            print(f"💸 Budget Utilized: 98% (remaining 2% = 'savings')")
            time.sleep(1)
            print("\n📝 Notes: 'Equipment needs upgrade (additional ₱300M)'")

        else:
            uptime = random.uniform(95, 99.9)
            print(f"⏱️  System Uptime: {uptime:.1f}%")
            print(f"✅ Successful Detections: 1,247")
            print(f"❌ Failed Detections: 0")
            print(f"💸 Budget Utilized: 100%")
            time.sleep(1)
            print("\n🏆 Status: EXCEEDS EXPECTATIONS")
            print("🎖️  Team to receive Performance Bonus!")


# Run the simulation
if __name__ == "__main__":
    system = FloodDetectionSystem()

    print(f"\n📅 Current season: {'🌧️  RAINY' if system.is_rainy_season else '☀️  DRY'}")
    time.sleep(1)

    # Check system health
    system.check_system_health()

    # Try to detect flood
    water_level = 85 if system.is_rainy_season else 5
    system.detect_flood(water_level)

    # Generate report
    system.generate_report()

    print("\n\n" + "="*55)
    print("💬 Official Statement:")
    print("   'The system is working as intended.'")
    time.sleep(1)
    print("\n🤔 Citizens: 'Intended for what exactly?'")
    print("="*55)
