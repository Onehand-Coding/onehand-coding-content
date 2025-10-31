"""
Name Meaning Explorer
A module that dynamically fetches and presents meanings for names using external APIs
"""
import os
import time
import asyncio

from ..name_meanings import NameMeaningProvider
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause


class NameMeaningExplorer:
    """Interactive name meaning exploration tool."""
    LINE_LENGTH = 50

    def __init__(self):
        """Initialize the name meaning explorer."""
        self.name_meaning_provider = NameMeaningProvider()
        print("\n" + "="*self.LINE_LENGTH)
        typewriter_effect("🔍 NAME MEANING EXPLORER")
        print("="*self.LINE_LENGTH)
        dramatic_pause(2)
        typewriter_effect("Discover the hidden meanings behind names!")
        dramatic_pause(2)

    async def analyze_name_concurrently(self, name: str):
        """Analyze a name while showing animations."""
        # Start the analysis task
        analysis_task = asyncio.create_task(self.name_meaning_provider.analyze_name(name))
        
        # Run the animations
        await self._show_loading_animations(name)
        
        # Wait for the analysis to complete
        analysis_result = await analysis_task
        
        # Display the results
        self._display_name_info(analysis_result.get('formatted_description', 'No information available.'))

    async def _show_loading_animations(self, name: str):
        """Display loading animations."""
        typing_with_pauses(f"\n🔄 Analyzing name: '{name}'")
        await asyncio.sleep(1)
        
        typing_with_pauses("🌍 Fetching etymology data...")
        await asyncio.sleep(1)
        
        typing_with_pauses("📚 Consulting name databases...")
        await asyncio.sleep(1)
        
        typing_with_pauses("🔍 Processing meaning information...")
        await asyncio.sleep(2)

    def _display_name_info(self, description: str):
        """Display name information using presentation effects."""
        
        if description:
            print("\n" + "="*self.LINE_LENGTH)
            typewriter_effect("📊 NAME ANALYSIS RESULTS")
            print("="*self.LINE_LENGTH, "\n")
            
            # Print the description with effect, line by line
            lines = description.split('\n')
            for line in lines:
                if line.strip():
                    typing_with_pauses(f"  {line.strip()}")
                    time.sleep(0.5)

            # Print line break based on terminal width.
            print("\n" + "="*os.get_terminal_size().columns, "\n\n")
        else:
            typewriter_effect("❌ No information found for this name.")


async def main():
    """Main entry point for the name meaning explorer."""
    explorer = NameMeaningExplorer()
    dramatic_pause(1)

    loop = asyncio.get_running_loop()

    while True:
        typewriter_effect("\n📋 Enter a name to analyze (or 'quit' to exit): ", end_with_newline=False)
        
        # Get user input asynchronously
        user_input = await loop.run_in_executor(None, lambda: input().strip().title())

        if user_input.lower() in ['quit', 'exit', 'q']:
            typewriter_effect("\n👋 Thank you for exploring name meanings!")
            break

        if user_input:
            await explorer.analyze_name_concurrently(user_input)
        else:
            typewriter_effect("⚠️  Please enter a valid name.")


# Usage
if __name__ == "__main__":
    asyncio.run(main())
