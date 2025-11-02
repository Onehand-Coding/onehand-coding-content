import time
from random import randint, choice
from abc import ABC, abstractmethod

from ..config import LINE_LENGTH
from ..sounds import play_with_wait, CORRUPTION_3
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause


class CorruptOfficial(ABC):
    def __init__(self, name, position):
        self.name, self.position, self.wealth, self.stolen_taxes = name, position, 0, 0
    @abstractmethod
    def steal_money(self, amount): pass


class CongressOfficial(CorruptOfficial):
    def __init__(self, name):
        super().__init__(name, "Congress Member")
        self.insertions_made = 0
    def steal_money(self, amount):
        insertion = amount * 0.30  # 30% markup through budget insertion
        self.wealth += insertion
        self.stolen_taxes += insertion
        self.insertions_made += 1
        return f"🏛️ {self.name}: Inserted ₱{insertion:,.0f} in budget (Insertion #{self.insertions_made})"


class DPWHOfficial(CorruptOfficial):
    def __init__(self, name):
        super().__init__(name, "DPWH Official")
        self.projects_awarded = 0
    def steal_money(self, amount):
        kickback = amount * 0.25  # 25% kickback from contractors
        self.wealth += kickback
        self.stolen_taxes += kickback
        self.projects_awarded += 1
        return f"🤝 {self.name}: Received ₱{kickback:,.0f} kickback (Project #{self.projects_awarded})"


class CorruptContractor(CorruptOfficial):
    def __init__(self, name):
        super().__init__(name, "Private Contractor")
        self.luxury_items = 0
    def steal_money(self, amount):
        profit = amount * 0.70  # 70% profit on substandard/ghost work
        self.wealth += profit
        self.stolen_taxes += profit
        self.luxury_items += randint(1, 3)
        return f"💰 {self.name}: Made ₱{profit:,.0f} profit, bought {self.luxury_items} luxury items"


class FloodProject:
    def __init__(self, budget, location):
        self.budget, self.location = budget, location
        self.project_type = choice(["ghost", "substandard", "overpriced"])
        self.actual_value, self.taxes_wasted = 0, budget
    def implement(self):
        if self.project_type == "ghost":
            self.actual_value = 0
            status = "👻 GHOST PROJECT - Nothing built!"
        elif self.project_type == "substandard":
            self.actual_value = self.budget * 0.15  # Only 15% actual work done
            status = f"🗑️ SUBSTANDARD - ₱{self.actual_value:,.0f} work for ₱{self.budget:,.0f}"
        else:  # overpriced
            self.actual_value = self.budget * 0.20  # 20% actual value
            status = f"💸 OVERPRICED - ₱{self.actual_value:,.0f} value for ₱{self.budget:,.0f}"
        return f"{self.location}: {status}"


class Taxpayer:
    def __init__(self, name, location="Flood-prone Area"):
        self.name, self.location = name, location
        self.times_flooded, self.anger_level = 0, 0
        self.taxes_paid = randint(50000, 200000)
    def experience_flood(self):
        self.times_flooded += 1
        self.anger_level += 10
        complaints = ["Nasaan ang tax namin?!", "Bakit walang project dito?!", "Puro ghost projects!"]
        return f"🌊 {self.name}: {choice(complaints)} (Flood #{self.times_flooded}, Anger: {self.anger_level})"
    def pay_taxes(self):
        return f"💸 {self.name}: Paid ₱{self.taxes_paid:,.0f} taxes this year"


class CorruptionSystem:
    def __init__(self):
        self.total_budget = 500_000_000_000
        self.senators_congressmen = ["Sen. Pothole", "Cong. Kickback", "Rep. Budget Master"]
        self.dpwh_officials = ["Usec. Under-the-table", "Dir. Porscha", "Engr. Ghostly"]
        self.contractors = ["Phantom Builders Co.", "Substandard Solutions Inc.", "Infinite Profit Corp."]
        self.locations = ["Metro Manila", "Bulacan", "Pampanga", "Rizal", "Cavite"]

    def simulate_corruption_cycle(self):
        print("\n" + "="*LINE_LENGTH)
        typewriter_effect("🏛️ PHILIPPINE FLOOD CONTROL CORRUPTION SIMULATOR 🌊")
        print("="*LINE_LENGTH)
        dramatic_pause(2)  # Dramatic pause after title

        congress = CongressOfficial(choice(self.senators_congressmen))
        dpwh = DPWHOfficial(choice(self.dpwh_officials))
        contractor = CorruptContractor(choice(self.contractors))
        taxpayer = Taxpayer("Juan Taxpayer")
        project_budget = 100_000_000
        project = FloodProject(project_budget, choice(self.locations))

        typing_with_pauses(f"💸 TAXPAYER CONTRIBUTION:")
        dramatic_pause(1)
        typing_with_pauses(taxpayer.pay_taxes())
        dramatic_pause(3)

        typing_with_pauses("\n💼 THE CORRUPTION CYCLE:")
        dramatic_pause(2)

        typing_with_pauses(f"1. {congress.steal_money(project_budget)}")
        dramatic_pause(2.5)

        typing_with_pauses(f"2. {dpwh.steal_money(project_budget)}")
        dramatic_pause(2.5)

        typing_with_pauses(f"3. {contractor.steal_money(project_budget)}")
        dramatic_pause(3)

        typing_with_pauses(f"\n🏗️ PROJECT 'IMPLEMENTATION':")
        dramatic_pause(1.5)
        typing_with_pauses(project.implement())
        dramatic_pause(4)

        typing_with_pauses("\n🌊 FLOOD SEASON ARRIVES:")
        dramatic_pause(2)
        typing_with_pauses(taxpayer.experience_flood())
        dramatic_pause(2)
        typing_with_pauses(taxpayer.experience_flood())
        dramatic_pause(3)

        total_stolen = congress.wealth + dpwh.wealth + contractor.wealth
        typing_with_pauses(f"\n💀 THE DEVASTATING RESULT:")
        dramatic_pause(2)

        typing_with_pauses(f"💰 Money stolen: ₱{total_stolen:,.0f}")
        dramatic_pause(1.5)

        typing_with_pauses(f"🏗️ Actual project value: ₱{project.actual_value:,.0f}")
        dramatic_pause(1.5)

        typing_with_pauses(f"💸 Taxpayer money wasted: ₱{project.taxes_wasted:,.0f}")
        dramatic_pause(1.5)

        typing_with_pauses(f"🌊 {taxpayer.name} flooded {taxpayer.times_flooded} times")
        dramatic_pause(1.5)

        typing_with_pauses(f"😡 Public anger level: {taxpayer.anger_level}/100")
        dramatic_pause(3)

        typing_with_pauses("\n🔄 MULTIPLY THIS BY 10,000+ PROJECTS & IMAGINE THE SCALE...")
        dramatic_pause(3)

        typing_with_pauses(f"🎭 Welcome to Philippine Flood Control Reality! 🇵🇭")
        dramatic_pause(2)


def main():
    """Flood Control Simulator Entry Point."""
    CorruptionSystem().simulate_corruption_cycle()

    play_with_wait(CORRUPTION_3)


if __name__ == "__main__":
    main()
