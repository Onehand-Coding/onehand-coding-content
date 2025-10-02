import time
import random
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause

class ProjectBudget:
    """
    Philippine Government Budget Allocator v2025
    Guaranteed to maximize... uhh... efficiency? 👀
    """

    def __init__(self, project_name, actual_cost):
        self.project_name = project_name
        self.actual_cost = actual_cost
        typewriter_effect(f"\n💰 Processing budget for: {project_name}")
        typewriter_effect(f"📋 Actual project cost: ₱{actual_cost:,.2f}")
        dramatic_pause(1)

    def add_contingency(self):
        """Standard 10% contingency... or is it?"""
        typewriter_effect("\n⚙️  Adding contingency fund...")
        dramatic_pause(1)
        contingency = self.actual_cost * random.uniform(0.30, 0.50)
        typing_with_pauses(f"✓ Contingency: ₱{contingency:,.2f} (wait, wasn't it supposed to be 10%?)")
        return contingency

    def add_consulting_fees(self):
        """Experts are expensive, daw"""
        typewriter_effect("\n👔 Adding consulting fees...")
        dramatic_pause(1)
        consulting = self.actual_cost * random.uniform(0.25, 0.40)
        typewriter_effect(f"✓ Consultants: ₱{consulting:,.2f}")
        typing_with_pauses("   (Kamaganak ba? Ay, I mean... 'qualified professionals')")
        return consulting

    def add_admin_overhead(self):
        """Processing fees, paperwork, coffee meetings..."""
        typewriter_effect("\n📎 Calculating administrative overhead...")
        dramatic_pause(1)
        overhead = self.actual_cost * random.uniform(0.20, 0.35)
        typewriter_effect(f"✓ Admin costs: ₱{overhead:,.2f}")
        typing_with_pauses("   (Kasama na daw yung team building sa Boracay)")
        return overhead

    def mysterious_rounding(self, total):
        """The magic happens here ✨"""
        typewriter_effect("\n🎩 Applying 'standard rounding procedures'...")
        dramatic_pause(2)

        # Always rounds to the nearest million... UP
        rounded = ((total // 1000000) + 1) * 1000000
        difference = rounded - total

        typewriter_effect(f"✓ Rounded amount: ₱{rounded:,.2f}")
        if difference > 100000:
            typing_with_pauses(f"   (Namali ata ng zero? +₱{difference:,.2f} 'clerical error')")

        return rounded

    def allocate(self):
        """Run the full 'transparent' allocation process"""
        print("\n" + "="*60)
        typing_with_pauses("🏛️  OFFICIAL BUDGET ALLOCATION IN PROGRESS", delay=0.03)
        print("="*60)

        contingency = self.add_contingency()
        consulting = self.add_consulting_fees()
        overhead = self.add_admin_overhead()

        subtotal = self.actual_cost + contingency + consulting + overhead

        print("\n" + "-"*60)
        typewriter_effect(f"📊 Subtotal: ₱{subtotal:,.2f}")

        final_budget = self.mysterious_rounding(subtotal)

        print("\n" + "="*60)
        typing_with_pauses(f"✅ APPROVED BUDGET: ₱{final_budget:,.2f}", delay=0.03)
        print("="*60)

        markup = ((final_budget - self.actual_cost) / self.actual_cost) * 100
        typewriter_effect(f"\n💡 Total markup: {markup:.1f}%")
        dramatic_pause(1)
        typing_with_pauses("📢 'This is within international standards daw.' - Official Statement")
        dramatic_pause(1)
        typewriter_effect("\n🤷 Taxpayers: *visible confusion*")


# Example usage
if __name__ == "__main__":
    typing_with_pauses("🇵🇭 Welcome to the Philippine Project Budget Calculator", delay=0.03)
    typing_with_pauses("Where mathematics meets... creativity! 🎨\n", delay=0.03)
    dramatic_pause(2)

    project = ProjectBudget(
        project_name="Flood Control Drainage System (300m)",
        actual_cost=5000000.00
    )

    project.allocate()

    typewriter_effect("\n\n💬 Remember: 'Walang korapsiyon dito, may resibo!' 📄")
    typing_with_pauses("(Yung resibo naka-file sa cabinet na naka-lock sa bodega na walang susi)")
