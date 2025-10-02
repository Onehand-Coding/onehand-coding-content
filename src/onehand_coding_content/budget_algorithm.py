import time
import random

class ProjectBudget:
    """
    Philippine Government Budget Allocator v2025
    Guaranteed to maximize... uhh... efficiency? 👀
    """

    def __init__(self, project_name, actual_cost):
        self.project_name = project_name
        self.actual_cost = actual_cost
        print(f"\n💰 Processing budget for: {project_name}")
        print(f"📋 Actual project cost: ₱{actual_cost:,.2f}")
        time.sleep(1)

    def add_contingency(self):
        """Standard 10% contingency... or is it?"""
        print("\n⚙️  Adding contingency fund...")
        time.sleep(1)
        contingency = self.actual_cost * random.uniform(0.30, 0.50)
        print(f"✓ Contingency: ₱{contingency:,.2f} (wait, wasn't it supposed to be 10%?)")
        return contingency

    def add_consulting_fees(self):
        """Experts are expensive, daw"""
        print("\n👔 Adding consulting fees...")
        time.sleep(1)
        consulting = self.actual_cost * random.uniform(0.25, 0.40)
        print(f"✓ Consultants: ₱{consulting:,.2f}")
        print("   (Kamaganak ba? Ay, I mean... 'qualified professionals')")
        return consulting

    def add_admin_overhead(self):
        """Processing fees, paperwork, coffee meetings..."""
        print("\n📎 Calculating administrative overhead...")
        time.sleep(1)
        overhead = self.actual_cost * random.uniform(0.20, 0.35)
        print(f"✓ Admin costs: ₱{overhead:,.2f}")
        print("   (Kasama na daw yung team building sa Boracay)")
        return overhead

    def mysterious_rounding(self, total):
        """The magic happens here ✨"""
        print("\n🎩 Applying 'standard rounding procedures'...")
        time.sleep(2)

        # Always rounds to the nearest million... UP
        rounded = ((total // 1000000) + 1) * 1000000
        difference = rounded - total

        print(f"✓ Rounded amount: ₱{rounded:,.2f}")
        if difference > 100000:
            print(f"   (Namali ata ng zero? +₱{difference:,.2f} 'clerical error')")

        return rounded

    def allocate(self):
        """Run the full 'transparent' allocation process"""
        print("\n" + "="*60)
        print("🏛️  OFFICIAL BUDGET ALLOCATION IN PROGRESS")
        print("="*60)

        contingency = self.add_contingency()
        consulting = self.add_consulting_fees()
        overhead = self.add_admin_overhead()

        subtotal = self.actual_cost + contingency + consulting + overhead

        print("\n" + "-"*60)
        print(f"📊 Subtotal: ₱{subtotal:,.2f}")

        final_budget = self.mysterious_rounding(subtotal)

        print("\n" + "="*60)
        print(f"✅ APPROVED BUDGET: ₱{final_budget:,.2f}")
        print("="*60)

        markup = ((final_budget - self.actual_cost) / self.actual_cost) * 100
        print(f"\n💡 Total markup: {markup:.1f}%")
        time.sleep(1)
        print("📢 'This is within international standards daw.' - Official Statement")
        time.sleep(1)
        print("\n🤷 Taxpayers: *visible confusion*")


# Example usage
if __name__ == "__main__":
    print("🇵🇭 Welcome to the Philippine Project Budget Calculator")
    print("Where mathematics meets... creativity! 🎨\n")
    time.sleep(2)

    project = ProjectBudget(
        project_name="Flood Control Drainage System (300m)",
        actual_cost=5000000.00
    )

    project.allocate()

    print("\n\n💬 Remember: 'Walang korapsiyon dito, may resibo!' 📄")
    print("(Yung resibo naka-file sa cabinet na naka-lock sa bodega na walang susi)")
