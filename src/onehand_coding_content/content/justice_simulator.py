#!/usr/bin/env python3
"""
Philippine Justice System Simulator
A satirical simulation highlighting disparities in legal outcomes based on socioeconomic status.

Note: This is a work of social commentary and does not represent actual legal processes.
"""
import random
import time
import sys
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

from ..config import LINE_LENGTH
from ..sounds import play_with_wait, UNFAIR_1, UNFAIR_2
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause


class SocialClass(Enum):
    POOR = "Poor (Minimum wage earner)"
    MIDDLE = "Middle Class (Professional)"
    WEALTHY = "Wealthy (Business owner)"
    POLITICIAN = "Politician (Honorable)"


class CrimeType(Enum):
    THEFT = "Theft"
    CORRUPTION = "Corruption"
    TAX_EVASION = "Tax Evasion"
    DRUG_POSSESSION = "Drug Possession"
    PLUNDER = "Plunder"


@dataclass
class Evidence:
    type: str
    strength: float  # 0.0 to 1.0
    description: str


@dataclass
class Accused:
    name: str
    social_class: SocialClass
    connections: int  # 0-10 scale
    wealth: float  # In millions of pesos
    media_influence: int  # 0-10 scale


class JusticeSimulator:
    def __init__(self):
        self.cases_processed = 0
        self.convictions = {"total": 0, "by_class": {}}

    def print_header(self):
        print("\n" + "="*LINE_LENGTH)
        typewriter_effect("🏛️  PHILIPPINE JUSTICE SYSTEM SIMULATOR")
        print("=" * LINE_LENGTH)
        dramatic_pause(2)

        typing_with_pauses('⚖️  "Equal Justice Under Law"')
        typing_with_pauses("   *Terms and conditions apply. Wealth and connections may affect outcome*")
        dramatic_pause(1)

    def calculate_conviction_probability(self, accused: Accused, evidence_strength: float) -> float:
        """Calculate the probability of conviction based on various factors."""
        base_probability = evidence_strength

        # Social class modifiers
        class_modifiers = {
            SocialClass.POOR: 0.3,           # +30% more likely to be convicted
            SocialClass.MIDDLE: 0.0,         # Neutral
            SocialClass.WEALTHY: -0.2,       # -20% less likely
            SocialClass.POLITICIAN: -0.4,    # -40% less likely
        }

        # Apply social class modifier
        probability = base_probability + class_modifiers[accused.social_class]

        # Wealth factor (more wealth = better lawyers)
        wealth_factor = min(accused.wealth * 0.05, 0.3)  # Max 30% reduction
        probability -= wealth_factor

        # Connections factor
        connection_factor = accused.connections * 0.03  # 3% per connection
        probability -= connection_factor

        # Media influence factor
        media_factor = accused.media_influence * 0.02  # 2% per media point
        probability -= media_factor

        return max(0.05, min(0.95, probability))  # Keep between 5% and 95%

    def get_delay_time(self, accused: Accused) -> int:
        """Calculate case processing delay in months."""
        base_delay = 12  # 1 year base delay

        if accused.social_class in [SocialClass.POLITICIAN]:
            delay = base_delay + (accused.connections * 6) + (accused.wealth * 2)
        elif accused.social_class == SocialClass.WEALTHY:
            delay = base_delay + (accused.connections * 3) + (accused.wealth * 1.5)
        elif accused.social_class == SocialClass.POOR:
            delay = max(3, base_delay - 6)  # Faster processing, not necessarily good
        else:
            delay = base_delay

        return int(delay)

    def get_excuse_generator(self, accused: Accused) -> List[str]:
        """Generate creative excuses based on social status."""
        excuses = {
            SocialClass.POLITICIAN: [
                "Political persecution by the opposition",
                "Selective justice targeting public servants",
                "Evidence was planted during the previous administration",
                "Currently serving the people, cannot be detained",
                "Immunity due to ongoing legislative duties"
            ],
            SocialClass.WEALTHY: [
                "Job creator, conviction would hurt the economy",
                "Technicality in the legal procedure",
                "Will appeal to higher courts indefinitely",
                "Plea bargain negotiations ongoing",
                "Medical condition requires treatment abroad"
            ]
        }

        return excuses.get(accused.social_class, ["No special excuses available"])

    def animate_processing(self, message: str, duration: float = 3.0):
        """Animate processing with dots."""
        typing_with_pauses(message)
        for _ in range(int(duration * 2)):
            print(".", end="", flush=True)
            dramatic_pause(1)
        dramatic_pause(0.5)  # pause after

    def process_case(self, accused: Accused, crime: CrimeType, evidence: Evidence):
        """Process a single case through the justice system."""
        self.cases_processed += 1

        typing_with_pauses(f"\n📋 CASE #{self.cases_processed}")
        typing_with_pauses(f"👤 Accused: {accused.name}")
        typing_with_pauses(f"💰 Social Status: {accused.social_class.value}")
        typing_with_pauses(f"🔗 Connections: {accused.connections}/10")
        typing_with_pauses(f"💸 Wealth: ₱{accused.wealth:.1f} million")
        typing_with_pauses(f"📺 Media Influence: {accused.media_influence}/10")
        typing_with_pauses(f"⚖️ Crime: {crime.value}")
        typing_with_pauses(f"🔍 Evidence: {evidence.description}")
        typing_with_pauses(f"💪 Evidence Strength: {evidence.strength*100:.0f}%")
        dramatic_pause(0.5)

        # Calculate conviction probability
        conviction_prob = self.calculate_conviction_probability(accused, evidence.strength)
        delay_months = self.get_delay_time(accused)

        typing_with_pauses("🏛️ Processing through the justice system", end_with_newline=False)
        dramatic_pause(4)

        typing_with_pauses(f"⏰ Expected case duration: {delay_months} months")
        if accused.social_class in [SocialClass.POLITICIAN, SocialClass.WEALTHY]:
            typing_with_pauses(f"⚖️ Conviction probability: {conviction_prob*100:.1f}% (adjusted for status)")
            excuses = self.get_excuse_generator(accused)
            typing_with_pauses(f"🎭 Primary defense strategy: {random.choice(excuses)}")
        else:
            typing_with_pauses(f"⚖️ Conviction probability: {conviction_prob*100:.1f}%")

        typing_with_pauses("\n⚖️ Deliberating verdict", end_with_newline=False)
        dramatic_pause(4)

        # Determine outcome
        is_convicted = random.random() < conviction_prob

        if is_convicted:
            sentence = self.get_sentence(accused, crime, evidence.strength)
            typing_with_pauses(f"⚖️ VERDICT: GUILTY")
            typing_with_pauses(f"📏 Sentence: {sentence}")
            self.convictions["total"] += 1
            class_name = accused.social_class.name
            self.convictions["by_class"][class_name] = self.convictions["by_class"].get(class_name, 0) + 1
        else:
            typing_with_pauses(f"⚖️ VERDICT: NOT GUILTY / DISMISSED")
            if accused.social_class == SocialClass.POLITICIAN:
                typing_with_pauses(f"📰 Press statement: 'Justice has been served. I am vindicated.'")

        dramatic_pause(2)  # Pause before next case

    def get_sentence(self, accused: Accused, crime: CrimeType, evidence_strength: float) -> str:
        """Generate appropriate sentence based on crime and social status."""
        base_sentences = {
            CrimeType.THEFT: "6 months to 2 years",
            CrimeType.DRUG_POSSESSION: "6-12 years",
            CrimeType.CORRUPTION: "6-10 years + disqualification",
            CrimeType.TAX_EVASION: "2-6 years + fines",
            CrimeType.PLUNDER: "Life imprisonment"
        }

        sentence = base_sentences[crime]

        # Status-based sentence modifications
        if accused.social_class == SocialClass.POOR:
            return sentence + " (served immediately)"
        elif accused.social_class == SocialClass.POLITICIAN:
            return sentence + " (suspended pending appeal, may run for office)"
        elif accused.social_class == SocialClass.WEALTHY:
            return sentence + " (house arrest possible, bail pending appeal)"
        else:
            return sentence

    def run_simulation(self):
        """Run the complete simulation with multiple test cases."""
        self.print_header()

        # Test cases representing different scenarios
        test_cases = [
            {
                "accused": Accused("Juan dela Cruz", SocialClass.POOR, 0, 0.01, 0),
                "crime": CrimeType.THEFT,
                "evidence": Evidence("CCTV footage", 0.9, "Clear video evidence of theft")
            },
            {
                "accused": Accused("Sen. Ricardo Milyones", SocialClass.POLITICIAN, 9, 50.0, 8),
                "crime": CrimeType.PLUNDER,
                "evidence": Evidence("Bank records + witnesses", 0.95, "Overwhelming documentary evidence")
            },
            {
                "accused": Accused("Maria Santos", SocialClass.MIDDLE, 2, 0.5, 1),
                "crime": CrimeType.TAX_EVASION,
                "evidence": Evidence("BIR audit", 0.7, "Incomplete tax filings for 3 years")
            },
            {
                "accused": Accused("Don Arturo Yaman", SocialClass.WEALTHY, 7, 25.0, 5),
                "crime": CrimeType.CORRUPTION,
                "evidence": Evidence("Wiretapped conversations", 0.85, "Audio evidence of bribery")
            },
            {
                "accused": Accused("Aling Nena", SocialClass.POOR, 0, 0.005, 0),
                "crime": CrimeType.DRUG_POSSESSION,
                "evidence": Evidence("Police testimony", 0.6, "Found with 5 grams of shabu (allegedly)")
            }
        ]

        # Process all cases
        for i, case in enumerate(test_cases):
            if i > 0:  # Add extra pause between cases
                typing_with_pauses("\n" + "🔄 Moving to next case...")
                dramatic_pause(2)
            self.process_case(case["accused"], case["crime"], case["evidence"])

        # Pause before statistics
        typing_with_pauses("\n🔄 Compiling final statistics...")
        dramatic_pause(3)

        # Print statistics
        self.print_statistics()

    def print_statistics(self):
        """Print simulation statistics."""
        print("\n" + "=" * LINE_LENGTH)
        typing_with_pauses("📊 SIMULATION STATISTICS")
        print("=" * LINE_LENGTH)

        dramatic_pause(2)
        typing_with_pauses(f"📋 Total cases processed: {self.cases_processed}")
        typing_with_pauses(f"⚖️ Total convictions: {self.convictions['total']}")
        typing_with_pauses(f"📈 Overall conviction rate: {(self.convictions['total']/self.cases_processed)*100:.1f}%")
        typing_with_pauses("\n🏷️ Conviction rate by social class:")

        class_counts = {}
        for case in [SocialClass.POOR, SocialClass.MIDDLE, SocialClass.WEALTHY,
                    SocialClass.POLITICIAN]:
            class_name = case.name
            class_counts[class_name] = sum(1 for _ in range(self.cases_processed) if True)  # Simplified

        for class_name, convictions in self.convictions["by_class"].items():
            rate = (convictions / 2) * 100  # Simplified calculation for demo
            typing_with_pauses(f"   {class_name}: {rate:.1f}%")

        dramatic_pause(2)

        print("\n" + "=" * LINE_LENGTH)
        typing_with_pauses("⚖️ 'Justice is blind... to bank account balances and political connections.'")
        typing_with_pauses("💡 Disclaimer: This is a work of satire and social commentary.")
        typing_with_pauses("   Real justice systems should treat all individuals equally.")
        print("=" * LINE_LENGTH)

def main():
    """Main function to run the simulation."""
    typing_with_pauses("\n🚀 Initializing Philippine Justice System Simulator...")
    typing_with_pauses("⚖️  Loading legal frameworks and bias algorithms...")
    typing_with_pauses("💰 Calibrating wealth-to-justice conversion rates...")
    typing_with_pauses("🏛️ System ready!\n")
    dramatic_pause(2)

    simulator = JusticeSimulator()

    try:
        simulator.run_simulation()
    except KeyboardInterrupt:
        typing_with_pauses("\n⚠️ Simulation interrupted by user.")
        typing_with_pauses("🏛️ Even the simulation respects your right to due process!")

    dramatic_pause(2)
    typing_with_pauses("\n👋 Think about it 💭!")

    play_with_wait(UNFAIR_1)
    play_with_wait(UNFAIR_2)

if __name__ == "__main__":
    main()
