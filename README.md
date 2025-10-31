# Onehand Coding Content

This repository is a collection of diverse and interactive Python scripts, originally created for the [Onehand Coding FB Page](https://www.facebook.com/onehand.coding/). The project's main goal is to provide a modular framework for demonstrating various programming concepts in an educational and engaging way.

## Project Features

- **Modular Script Runner**: A simple command-line interface to easily discover and run any content script.
- **Diverse Content Library**: Includes a variety of scripts covering topics from data simulation and API integration to fun utilities and artistic displays.
- **Modern Python Tooling**: Utilizes `uv` for fast and efficient dependency management and script execution.
- **Advanced Script Examples**: Some scripts demonstrate more complex features like asynchronous programming, database caching (`sqlite`), and integration with external APIs and LLMs.

---

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Onehand-Coding/onehand-coding-content.git
cd onehand-coding-content
```

### 2. Install Dependencies
This project uses `uv` to manage the virtual environment and dependencies.

```bash
# Create a virtual environment and install all required packages
uv sync
```

### 3. Configure Environment (Optional)
Some scripts may require API keys or other secrets to function.

- Check if a `.env.example` file exists in the project root.
- If it does, copy it to a new `.env` file:
  ```bash
  cp .env.example .env
  ```
- Open the `.env` file and add the required values.

---

## Usage

All runnable scripts are located in the `src/onehand_coding_content/content/` directory.

To run a script, use the `uv run content` command followed by the script's filename.

### Examples:

```bash
# Run the Philippine Flag display script
uv run content philippine_flag.py

# Run the dynasty simulator
uv run content dynasty_simulator.py

# Run the interactive name meaning explorer
uv run content name_meaning_explorer.py
```

## Contributing

Contributions are welcome! If you have an idea for a new script or an improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.