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
    import importlib.util
    from pathlib import PosixPath

    content_dir = Path(__file__).parent / "content"
    script_path = content_dir / script_name

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

        # If the module has a main function, call it
        if hasattr(module, 'main'):
            module.main()
    except KeyboardInterrupt:
        # Let the module handle its own interrupt behavior if it has proper handling
        # If we get here, the module didn't handle its own interrupt, so we exit
        print()  # Add a newline
        sys.exit(0)


def main():
    """Run the main function."""
    args = sys.argv

    # Lets support running one script at a time for now.
    if len(args) != 2:
        print("Choose a content srcipt to run!")
        sys.exit(1)
    elif len(args) > 2:
        print("Isa-isang script lang bro, mahina ang kalaban!")
        sys.exit(1)

    run_script(args[1])


if __name__ == "__main__":
    main()
