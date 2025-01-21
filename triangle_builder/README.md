This Python script generates a specified number of random triangle-like number sequences, checks whether they satisfy a specific condition (one side cannot be greater than sum of two different sides of triangle), and categorizes them into two groups. The script then saves the results into two separate files: one for "correct" triangles and one for "incorrect" triangles.

- `generate_numbers_to_file` - generates a customizable number of sets, each containing three random numbers, and writes them to a file.
- `triangle_builder` - each set of three numbers is validated based on a condition: if the largest number divided by the sum of the numbers is greater than or equal to 0.5, the set is classified as "incorrect," otherwise it is classified as "correct."

Folder *result* contains sample output of running the script.