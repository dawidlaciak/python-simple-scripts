from random import seed, random, randint
from math import radians, sin, cos, sqrt
import matplotlib.pyplot as plt

coordinateX = [] # contains people x coordinates
coordinateY = [] # contains people y coordinates
condition = [] # contains people health condition - 'r' for sick and 'g' for healthy

simulation_steps = 20 # how many times, people move in simulation
area_side = 10 # length of arena's side of simulation
population = 20 # population of people in simulation
vector = 0.5 # distance which people move each step of simulation
spread_radius = 0.7 # virus spread radius

for i in range(population):
    x = random() * area_side
    y = random() * area_side
    
    coordinateX.append(x)
    coordinateY.append(y)
    condition.append('g')

condition[randint(0, 19)] = 'r'

for step in range(simulation_steps):

    for i in range(population):
        angle = radians(float(random() * 360)) # angle in which direction the person will go
        coordinateX[i] += vector * cos(angle)
        coordinateY[i] += vector * sin(angle)

    for i in range(population):
        if condition[i] == 'r':
            for j in range(population):
                distance = sqrt((coordinateX[i] - coordinateX[j])**2 + (coordinateY[i] - coordinateY[j])**2) # distance between sick and healthy person
                if distance < spread_radius:
                    condition[j] = 'r'

    healthy_people = 0 # amout of healthy people during specific step
    sick_people = 0 # amout of sick people during specific step
    for i in range(population):
        if condition[i] == 'g':
            healthy_people += 1
        else:
            sick_people += 1

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Step {step+1}, healthy people: {healthy_people}, sick people: {sick_people}')
    plt.grid(True)

    thismanager = plt.get_current_fig_manager()
    thismanager.window.wm_geometry('+1200+50')

    plt.scatter(coordinateX, coordinateY, c=condition)
    plt.show()