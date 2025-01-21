# SMS Converter

This Python script implements a bi-directional SMS text converter, allowing conversion between regular text and the numerical representation used in old mobile phones' SMS input systems. It maps text to numbers and vice versa, based on the T9 predictive text input standard.

## Features

1. **Text to T9 Conversion**: Converts uppercase alphabetical text into a T9 numerical sequence, separated by slashes (`/`).
2. **T9 to Text Conversion**: Converts a T9 numerical sequence back into text.
3. **Spaces Support**: Includes support for spaces, represented as `0` in the T9 format.
4. **Error Handling**: Checks the validity of the input to ensure proper processing.

## Input and Output

- **Text to Numbers**: Converts a given string of text into its T9 representation, with each letter mapped to the corresponding number repeated as many times as the position of the letter within its group (e.g., `C` → `222`).
- **Numbers to Text**: Converts a T9 numerical sequence (separated by `/`) back into text, interpreting numbers and spaces correctly.
