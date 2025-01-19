This Python script simulates the spread of a virus within a population moving randomly within a confined area. The program visualizes each step of the simulation and tracks how many individuals remain healthy or become sick over time. It leverages randomness for movement and infection spread, with key parameters customizable for different scenarios.

## People simulation

Randomly initializes people within a square area, each individual has an initial health status: "healthy" (g) or "sick" (r). Individuals move randomly in each step.

## Virus spread
A sick person can infect a healthy individual if they are within a specified distance defined by `spread_radius`.

## Visualization
The positions and health conditions of individuals are plotted for each step of the simulation. The title of the plot shows the current step, the number of healthy individuals, and the number of sick individuals.

## Parameters

- `simulation_steps` (int) - number of steps in the simulation.
- `area_side` (float) -  length of one side of the simulation area (area is square).
- `population` (int) - total number of people in the simulation.
- `vector` (float) - distance each person moves per simulation's step.
- `spread_radius` (float) - maximum distance within which the virus can spread from one person to another.