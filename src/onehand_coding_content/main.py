#!/usr/bin/env python3
"""Main module for onehand-coding-content."""

import os
import sys
import subprocess
from pathlib import Path
from typing import Optional, List

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1" # Lets hide the pygame prompt.

from .config import PROJECT_ROOT


def run_script(script_name: str, args: list[str] = []):
    """Finds and runs a script."""
    python_executable = sys.executable
    content_dir = Path(__file__).parent / "content"
    script_path = content_dir / script_name

    if not script_path.exists():
        print(f"Script {script_path.name} not Found!")
        sys.exit(1)

    module_name = f"src.onehand_coding_content.content.{script_name[:-3]}"  # Remove .py extension
    module_command = [python_executable, "-m", module_name] + args

    try:
        result = subprocess.call(module_command, cwd=PROJECT_ROOT)
        # If module run fails, try direct execution
        if result != 0:
            command = [python_executable, str(script_path)] + args
            subprocess.call(command)
    except KeyboardInterrupt:
        print("\n👋 Program interrupted by user. Bye...")
        sys.exit(0)


def main():
    """Run the main function."""
    args = sys.argv

    # Lets support running one script at a time for now.
    if len(args) != 2:
        print("Choose a content srcipt to run!")
        sys.exit(1)
    elif len(args) > 2:
        print("Isa-isa script lang bro, mahina ang kalaban!")
        sys.exit(1)

    run_script(args[1])


if __name__ == "__main__":
    main()
