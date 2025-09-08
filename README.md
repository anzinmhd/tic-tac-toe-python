# generate_readme.py

# Project metadata - you can edit these
project_name = "Tic Tac Toe Game"
project_description = "A graphical Tic Tac Toe game built in Python using Tkinter, allowing two players to play on the same computer. The game features a modern GUI, turn-based play, win detection, tie detection, and a restart button."
technologies = ["Python 3.x", "Tkinter"]
features = [
    "Two-player gameplay on a single machine.",
    "Highlighting the winning row, column, or diagonal.",
    "Tie detection when all cells are filled.",
    "Restart button to reset the game.",
    "Modern color-coded GUI for better user experience."
]
gameplay_steps = [
    "The game starts with Player X.",
    "Players take turns clicking on empty cells to mark their symbol (X or O).",
    "The game detects a win if a player completes a row, column, or diagonal.",
    "The game detects a tie if all cells are filled without a winner.",
    "Players can click Restart to start a new game at any time."
]
installation_steps = [
    "Ensure Python 3.x is installed.",
    "Tkinter is included with Python, so no additional installation is required.",
    "Download the project files."
]
usage_instructions = [
    "Run the game using:\n```python\npython tic_tac_toe.py\n```",
    "Click on a cell to place your symbol.",
    "The game automatically detects wins or ties and highlights winning cells.",
    "Click Restart to reset the game."
]
code_structure = [
    "Main Game Window: Handles window creation, size, and centering.",
    "Game Board: 3x3 grid of Tkinter buttons.",
    "Game Logic:",
    "    - set_tile(row, col) → Marks the clicked cell and switches the player.",
    "    - check_winner() → Checks horizontal, vertical, diagonal, and anti-diagonal for a winner.",
    "    - Tie detection after 9 turns.",
    "    - Highlights the winning line with distinct colors.",
    "Restart Function: Resets the board and game variables."
]
future_enhancements = [
    "Add AI opponent for single-player mode.",
    "Implement score tracking across multiple games.",
    "Improve GUI with animations and sound effects.",
    "Make the game scalable for larger board sizes."
]
license_info = "This project is open-source and free to use. You can modify or distribute it under the MIT License."

# Generate README content
readme_content = f"""
# {project_name}

{project_description}

## Features
"""

for feature in features:
    readme_content += f"- {feature}\n"

readme_content += "\n## Technologies\n"
for tech in technologies:
    readme_content += f"- {tech}\n"

readme_content += "\n## Gameplay\n"
for i, step in enumerate(gameplay_steps, 1):
    readme_content += f"{i}. {step}\n"

readme_content += "\n## Installation\n"
for i, step in enumerate(installation_steps, 1):
    readme_content += f"{i}. {step}\n"

readme_content += "\n## Usage\n"
for step in usage_instructions:
    readme_content += f"{step}\n"

readme_content += "\n## Code Structure\n"
for line in code_structure:
    readme_content += f"- {line}\n"

readme_content += "\n## Future Enhancements\n"
for feature in future_enhancements:
    readme_content += f"- {feature}\n"

readme_content += f"\n## License\n{license_info}\n"

# Write to README.md
with open("README.md", "w") as file:
    file.write(readme_content)

print("README.md generated successfully!")
