# Dart Board Game

This Python script simulates a dartboard game where a player throws darts at a generated board and scores points based on the impact radius and the values in the board's layers.

## Features

1. **Dartboard Generation**:

   - Creates a square dartboard of a specified size.
   - The board is divided into layers, where each layer has a unique value (starting from `0` at the center and increasing outward).

2. **Random Dart Throw**:

   - Simulates throwing a dart at a random position on the board.
   - The script calculates and displays the area affected by the dart's impact.

3. **Scoring System**:

   - Points are calculated based on the values of cells within the dart's radius from the point of impact.
   - The radius is determined by the dart type (3x3 or 5x5 area).

4. **Customizable Settings**:
   - **Board Size**: You can define the size of the dartboard.
   - **Dart Type**: Choose between a 3x3 (`darts_type = 3`) or 5x5 (`darts_type = 5`) scoring area.
