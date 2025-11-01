#!/usr/bin/env python3
"""Main module for onehand-coding-content."""

import os
import sys
import asyncio
import inspect
import argparse
import importlib.util
from pathlib import Path
from typing import List

from .config import PROJECT_ROOT, LINE_LENGTH

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"  # Lets hide the pygame prompt.

CONTENT_DIR = Path(__file__).parent / "content"


def run_script(script_name: str, args: list[str] = []):
    """Finds and runs a script, handling both sync and async main functions."""
    script_path = CONTENT_DIR / script_name

    if not script_path.exists():
        print(f"Script {script_path.name} not Found!")
        sys.exit(1)

    # Add the project root to sys.path to allow imports
    if str(PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(PROJECT_ROOT))

    # Get the module name without .py extension
    module_name = Path(script_name).stem
    full_module_name = f"src.onehand_coding_content.content.{module_name}"

    # Load and execute the module
    spec = importlib.util.spec_from_file_location(full_module_name, script_path)
    module = importlib.util.module_from_spec(spec)

    # Add the module to sys.modules to enable relative imports
    sys.modules[full_module_name] = module

    try:
        spec.loader.exec_module(module)

        # If the module has a main function, call it appropriately
        if hasattr(module, 'main'):
            if inspect.iscoroutinefunction(module.main):
                asyncio.run(module.main())
            else:
                module.main()
    except KeyboardInterrupt:
        # Let the module handle its own interrupt behavior if it has proper handling
        # If we get here, the module didn't handle its own interrupt, so we exit
        print()  # Add a newline
        sys.exit(0)


def get_content_scripts():
    """
    Return a sorted list of all content scripts from content dir.
    Only return the names not absolute paths.
    """
    return sorted(content_code.name for content_code in CONTENT_DIR.glob("*.py"))


def list_content_scripts(content_scripts: List[str] = None) -> None:
    """List all content codes in content directory."""
    if content_scripts is None:
        content_scripts = []
    print()
    print("=" * LINE_LENGTH)
    print("AVAILABLE SCRIPTS TO RUN:")
    print("=" * LINE_LENGTH)

    if not content_scripts:
        print("\nNo Script to run, write a new one.")

    for i, content_code in enumerate(content_scripts, start=1):
        print(f"{i}.", content_code)
    print()


def choose_content_script(content_scripts: List[str] = None):
    """Pick a content script from content directory."""
    if content_scripts is None:
        content_scripts = []

    # List available scripts to choose from.
    list_content_scripts(content_scripts)

    # Choose the the script based on its index.
    while True:
        try:
            script_index = int(input("Enter script Index: "))
            if 0 < script_index <= len(content_scripts):
                return content_scripts[script_index - 1]
            print("\nEnter a valid Index!\n")
        except ValueError:
            print("\nEnter a valid Index!\n")
        except KeyboardInterrupt:
            print("Interrupted, exiting...")
            sys.exit()


def main():
    """Run the main function."""
    content_scripts = get_content_scripts()
    parser = argparse.ArgumentParser(description="Onehand-Coding FB page scripts content runner.")

    parser.add_argument("script", nargs="?", help="Name of the python script to run, must be located in content directory.")
    parser.add_argument("-l", "--list", action= "store_true", help="List all available scripts.")
    parser.add_argument("-c", "--choose", action= "store_true", help="Enables user to choose a script to run interactively.")

    args = parser.parse_args()

    if args.list:
        list_content_scripts(content_scripts)
    if args.choose:
        run_script(choose_content_script(content_scripts))

    # If the the script to run is provided as argument.
    script = args.script
    if script is not None:
        if script not in content_scripts:
            print(f"\n{script} not found in content dir, make sure to put it inside this directory: {CONTENT_DIR}/")
            return

        run_script(script)


if __name__ == "__main__":
    main()
