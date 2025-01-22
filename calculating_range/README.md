# Range Calculator

This Python script determines whether it is possible to traverse a list of integers (called the `movement_field`) by jumping between positions. Each integer in the list represents the maximum distance that can be jumped forward from that position.

## Features

1. **Traversal Feasibility Check**:
   - The script calculates whether it is possible to traverse the entire `movement_field` list starting from the first position.

2. **Dynamic Range Expansion**:
   - The script dynamically updates the maximum reachable index (`max_range`) as it iterates through the list.

3. **Efficient Algorithm**:
   - Uses a single pass through the list (`O(n)` complexity) to determine the result, making it efficient for large inputs.

4. **Input Flexibility**:
   - Accepts any list of non-negative integers, where each value represents the maximum jump distance from that index.
