import time

from ..config import LINE_LENGTH
from ..sounds import play_with_wait, CORRUPTION_2
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause


class RiceCrisisSimulator:
    """
    Philippine Rice Price Crisis Simulator
    "The Government's Solution to Hunger" (joke)
    Budget for Rice Subsidy: 50B | Actual Rice in Market: Nowhere
    """

    def __init__(self):
        self.farmer_income_daily = 500  # pesos, if lucky
        self.family_size = 4
        self.rice_price_2020 = 35  # per kilo, simpler times
        self.rice_price_2025 = 65  # per kilo, goodbye nutrition
        self.tariff_rate = 0.35  # 35% import duty
        self.government_rice_buffer = 0  # "exists"

        print()
        print("="*LINE_LENGTH)
        typewriter_effect("RICE PRICE CRISIS SIMULATOR v2025")
        print("="*LINE_LENGTH)
        print()
        dramatic_pause(1)
        typing_with_pauses("Feeding the nation... with spreadsheets! (charts only)")
        dramatic_pause(2)

    def show_farmer_situation(self):
        """Show the reality of a rice farmer's daily struggle"""
        typewriter_effect("\nMeet Farmer Juan...")
        dramatic_pause(2)

        typing_with_pauses("\nJUAN'S PROFILE:")
        print("-"*LINE_LENGTH)
        time.sleep(0.5)

        typing_with_pauses(f"   * Daily Income: P{self.farmer_income_daily}")
        time.sleep(1)
        typing_with_pauses("   * Job: Growing rice (the irony is thick)")
        time.sleep(1)
        typing_with_pauses(f"   * Family Size: {self.family_size} mouths to feed")
        time.sleep(1)
        typing_with_pauses("   * Hope Level: Fading")
        dramatic_pause(2)

    def show_price_history(self):
        """Show how rice prices destroyed purchasing power"""
        print("\n\n" + "="*LINE_LENGTH)
        typewriter_effect("RICE PRICE HISTORY")
        print("="*LINE_LENGTH)
        dramatic_pause(2)

        typing_with_pauses(f"\n2020 (Pre-Crisis): P{self.rice_price_2020}/kilo")
        time.sleep(1)
        typing_with_pauses("   Status: AFFORDABLE (kinda)")
        time.sleep(1)

        typing_with_pauses(f"\n2025 (Now): P{self.rice_price_2025}/kilo")
        time.sleep(1)
        typing_with_pauses("   Status: YOUR SALARY BETTER INCREASED")

        price_increase = ((self.rice_price_2025 - self.rice_price_2020) / self.rice_price_2020) * 100
        time.sleep(1)

        print("\n")
        typing_with_pauses(f"Price Increase: {price_increase:.1f}%")
        dramatic_pause(2)

        typing_with_pauses("Juan Salary Increase: 0%")
        dramatic_pause(2)

    def calculate_buying_power(self):
        """The devastating math of lost purchasing power"""
        print("\n\n" + "="*LINE_LENGTH)
        typewriter_effect("THE MATH (Prepare yourself)")
        print("="*LINE_LENGTH)
        dramatic_pause(2)

        # How much rice could he buy?
        kilos_2020 = self.farmer_income_daily / self.rice_price_2020
        kilos_2025 = self.farmer_income_daily / self.rice_price_2025
        loss = ((kilos_2020 - kilos_2025) / kilos_2020) * 100

        typing_with_pauses("\nWith P500 daily income:")
        time.sleep(1)

        typing_with_pauses(f"\n   2020: Juan could buy {kilos_2020:.2f} kilos/day")
        time.sleep(1)
        typing_with_pauses(f"   2025: Juan can buy {kilos_2025:.2f} kilos/day")
        dramatic_pause(2)

        typing_with_pauses(f"\nPURCHASING POWER LOSS: {loss:.1f}%")
        time.sleep(1)
        typing_with_pauses("   (His salary stayed the same. Rice decided to betray him.)")
        dramatic_pause(2)

    def family_needs_vs_reality(self):
        """Show the gap between what family needs and what Juan can afford"""
        print("\n\n" + "="*LINE_LENGTH)
        typewriter_effect("JUAN'S FAMILY REALITY CHECK")
        print("="*LINE_LENGTH)
        dramatic_pause(2)

        family_rice_daily = 2.5  # kilos needed to not starve
        cost_2020 = family_rice_daily * self.rice_price_2020
        cost_2025 = family_rice_daily * self.rice_price_2025

        typing_with_pauses(f"\nFamily needs per day: {family_rice_daily} kilos")
        dramatic_pause(2)

        typing_with_pauses("\nCOST COMPARISON:")
        time.sleep(1)

        typing_with_pauses(f"\n   2020: P{cost_2020:.2f}/day")
        time.sleep(0.5)
        typing_with_pauses("   Juan: OKAY nakakabili pa")
        time.sleep(1)

        typing_with_pauses(f"\n   2025: P{cost_2025:.2f}/day")
        time.sleep(0.5)
        typing_with_pauses("   Juan: KUMUSTA NA ANG BUHAY")
        dramatic_pause(2)

        daily_deficit = cost_2025 - self.farmer_income_daily
        monthly_deficit = daily_deficit * 30

        print("\n")
        typing_with_pauses(f"Daily Deficit: P{daily_deficit:.2f}")
        typing_with_pauses(f"Monthly Deficit: P{monthly_deficit:,.2f}")
        dramatic_pause(2)

        typing_with_pauses("\nJuan: Paano ko kakainin ang pamilya?")
        time.sleep(1)
        typing_with_pauses("Government: Have you tried eating spreadsheets?")
        dramatic_pause(2)

    def tariff_system_explained(self):
        """Show how tariffs keep prices high"""
        print("\n\n" + "="*LINE_LENGTH)
        typewriter_effect("THE TARIFF SCAM EXPLAINED")
        print("="*LINE_LENGTH)
        dramatic_pause(2)

        typing_with_pauses("\nOfficial Narrative:")
        typing_with_pauses("   We need tariffs to protect local farmers!")
        dramatic_pause(1)

        typing_with_pauses("\nReality Check:")
        time.sleep(1)
        typing_with_pauses("   * Import tariff: 35% on rice")
        time.sleep(1)
        typing_with_pauses("   * Result: Higher prices for EVERYONE")
        time.sleep(1)
        typing_with_pauses("   * Who benefits: Monopoly importers")
        time.sleep(1)
        typing_with_pauses("   * Who suffers: Juan & family")
        time.sleep(1)
        typing_with_pauses("   * Local farmers: Also suffering (lower quality competition)")
        dramatic_pause(2)

        typing_with_pauses("\nJuan: I'm a farmer but even I can't afford rice!")
        dramatic_pause(1)
        typing_with_pauses("Government: Mission accomplished!")
        dramatic_pause(2)

    def government_solutions_vs_reality(self):
        """Compare what government claims vs reality"""
        print("\n\n" + "="*LINE_LENGTH)
        typewriter_effect("GOVERNMENT SOLUTIONS vs REALITY")
        print("="*LINE_LENGTH)
        dramatic_pause(2)

        solutions = [
            {
                "claim": "Increase rice buffer stock",
                "status": "ANNOUNCED",
                "reality": "Buffer: 50B allocated. Actual rice delivered: TBD since 2022"
            },
            {
                "claim": "Import more rice",
                "status": "ANNOUNCED",
                "reality": "But tariffs make it expensive. Defeats the purpose."
            },
            {
                "claim": "Price controls",
                "status": "ANNOUNCED",
                "reality": "Artificial prices = market disappears = ACTUAL shortage"
            },
            {
                "claim": "Direct rice subsidies to farmers",
                "status": "ANNOUNCED",
                "reality": "Juan got 50kg rice coupon. It expires. He can't use it."
            }
        ]

        for i, solution in enumerate(solutions, 1):
            typing_with_pauses(f"\nSolution #{i}: {solution['claim']}")
            time.sleep(1)
            typewriter_effect(f"   Status: {solution['status']}")
            time.sleep(0.5)
            typing_with_pauses(f"   Reality: {solution['reality']}")
            dramatic_pause(1.5)

    def simulate_juan_buying_rice(self):
        """Simulate Juan's actual journey to buy rice"""
        print("\n\n" + "="*LINE_LENGTH)
        typewriter_effect("JUAN'S ACTUAL DAY: BUYING RICE")
        print("="*LINE_LENGTH)
        dramatic_pause(2)

        events = [
            ("6:00 AM", "Juan wakes up, checks wallet"),
            ("6:15 AM", "Math confirms: Can't afford full family rice"),
            ("8:00 AM", "Goes to market anyway"),
            ("8:30 AM", "Rice stall sold out (mga hoarders na nag-bulk buy)"),
            ("9:00 AM", "Next stall: Rice available but P75/kilo"),
            ("9:15 AM", "Juan: stares at wallet in defeat"),
            ("9:30 AM", "Buys 5 kilos instead of 7"),
            ("5:00 PM", "Wife: Bakit kulang?"),
            ("5:15 PM", "Juan: Sorry. That is all I can afford today."),
            ("11:00 PM", "Family goes to bed slightly hungry")
        ]

        for time_slot, event in events:
            typing_with_pauses(f"\n{time_slot}: {event}")
            time.sleep(1)

        dramatic_pause(2)

    def final_verdict(self):
        """The brutal final summary"""
        print("\n\n" + "="*LINE_LENGTH)
        typewriter_effect("FINAL VERDICT: THE IMPOSSIBLE EQUATION")
        print("="*LINE_LENGTH)
        dramatic_pause(2)

        typing_with_pauses("\nTHE NUMBERS:")
        typing_with_pauses(f"   Juan Income: P{self.farmer_income_daily}/day")
        typing_with_pauses(f"   Family Rice Need: P{2.5 * self.rice_price_2025:.2f}/day")
        typing_with_pauses(f"   Daily Deficit: P{(2.5 * self.rice_price_2025) - self.farmer_income_daily:.2f}")
        dramatic_pause(2)

        typing_with_pauses("\nTHE CONTRADICTION:")
        typing_with_pauses("   * Juan GROWS rice")
        time.sleep(1)
        typing_with_pauses("   * But can NOT AFFORD to eat it")
        time.sleep(1)
        typing_with_pauses("   * Government protects farmers")
        time.sleep(1)
        typing_with_pauses("   * By making rice unaffordable")
        time.sleep(1)
        typing_with_pauses("   * Logic level: BROKEN")
        dramatic_pause(2)

        typing_with_pauses("\nWHO BENEFITS:")
        typing_with_pauses("   YES: Monopoly rice importers (make huge markups)")
        typing_with_pauses("   YES: Government (tariff taxes)")
        typing_with_pauses("   YES: Hoarders (buy low, sell high)")
        typing_with_pauses("   NO: Juan (the farmer)")
        typing_with_pauses("   NO: Families (everyone else)")
        dramatic_pause(2)

        print("\n" + "="*LINE_LENGTH)
        typing_with_pauses("CODE REPRESENTATION:")
        print("="*LINE_LENGTH)

        typewriter_effect("\nif government_protects_farmers:")
        typewriter_effect("    farmers_starve = True")
        typewriter_effect("    rice_expensive = True")
        typewriter_effect("    logic = None")
        typewriter_effect("    corruption = MAXIMUM")
        typewriter_effect("    ")
        typewriter_effect("# This is not a bug.")
        typewriter_effect("# This is by design.")


def main():
    """Main entry point"""
    simulator = RiceCrisisSimulator()

    # Show Juan's situation
    simulator.show_farmer_situation()

    # Price history
    simulator.show_price_history()

    # The devastating math
    simulator.calculate_buying_power()

    # Family reality
    simulator.family_needs_vs_reality()

    # Tariff system
    simulator.tariff_system_explained()

    # Government solutions
    simulator.government_solutions_vs_reality()

    # Juan's actual day
    simulator.simulate_juan_buying_rice()

    # Final verdict
    simulator.final_verdict()

    print("\n\n" + "="*LINE_LENGTH)
    typing_with_pauses("POST-SCRIPT")
    print("="*LINE_LENGTH)
    dramatic_pause(1)

    typing_with_pauses("Juan grew the rice.")
    dramatic_pause(1)
    typing_with_pauses("Middlemen profited.")
    dramatic_pause(1)
    typing_with_pauses("Family went hungry.")
    dramatic_pause(1)
    typing_with_pauses("Statistics looked good on paper.")
    dramatic_pause(2)

    typing_with_pauses("\n~fin~ Rice Crisis")

    play_with_wait(CORRUPTION_2)


# Run the simulation
if __name__ == "__main__":
    main()
