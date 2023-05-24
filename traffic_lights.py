# Overview
# A character string represents a city road.

# Cars travel on the road obeying the traffic lights..

# Legend:

# . = Road
# C = Car
# G = GREEN traffic light
# O = ORANGE traffic light
# R = RED traffic light
# Something like this:

# CCC.G...R...
# Rules
# Simulation
# At each iteration:

# the lights change (according to the traffic light rules), then
# the car moves, obeying the car rules
# Traffic Light Rules
# Traffic lights change colour as follows:

# GREEN for 5 time units... then
# ORANGE for 1 time unit... then
# RED for 5 time units....
# ... and repeat the cycle
# Car Rules
# Cars travel left to right on the road, moving 1 character position per time unit

# Cars can move freely until they come to a traffic light. Then:

# if the light is GREEN they can move forward (temporarily occupying the same cell as the light)

# if the light is ORANGE then they must stop (if they have already entered the intersection they can continue through)

# if the light is RED the car must stop until the light turns GREEN again

# It is illegal to queue across an intersection. In other words, DO NOT enter an intersection unless you can see there is safe passage through it and out the other side!

# Kata Task
# Given the initial state of the road, return the states for all iterations of the simiulation.

# Input
# road = the road array
# n = how many time units to simulate (n >= 0)
# Output
# An array containing the road states at every iteration (including the initial state)
# Note: If a car occupies the same position as a traffic light then show only the car
# Notes
# There are 1 or more cars
# There are 0 or more traffic lights
# For the initial road state:
# cars can start anywhere except in the middle of intersections
# traffic lights are either GREEN or RED, and are at the beginning of their countdown cycles
# There are no reaction delays - when the lights change the car drivers will react immediately!
# If a car goes off the end of the road it just disappears from view
# There will always be some road between adjacent traffic lights
# If there is a traffic light at the end of the road then its exit is never blocked
# You cannot see beyond the car in front of you, so you cannot anticipate a gap that does not yet exist
# Example
# Run simulation for 16 time units

# Input

# road = "CCC.G...R..."
# n = 16
# Result

# [
#   "CCC.G...R...", // 0 initial state as passed
#   ".CCCG...R...", // 1
#   "..CCC...R...", // 2 show 1st car, not the green light
#   "..CCGC..R...", // 3 2nd car cannot enter intersection because 1st car blocks the exit
#   "...CC.C.R...", // 4 show 2nd car, not the green light
#   "...COC.CG...", // 5 3rd car stops for the orange light
#   "...CR.C.C...", // 6
#   "...CR..CGC..", // 7
#   "...CR...C.C.", // 8
#   "...CR...GC.C", // 9
#   "...CR...O.C.", // 10
#   "....C...R..C", // 11 3rd car can proceed
#   "....GC..R...", // 12
#   "....G.C.R...", // 13
#   "....G..CR...", // 14
#   "....G..CR...", // 15
#   "....O...C..."  // 16
# ]
# Good luck!

def traffic_lights(road, n):
    """main function of the program"""
    city = City(road)
    states =[]

    for i in range(n+1):  
        state = city.return_state()
        states.append(state)
        city.move_city()
    
    return states


class Car:
    """class representing a single car"""
    def __init__(self, init_position):
        self.pos = init_position
        self.counter = 0

    def move(self):
        self.pos+=1

    ##str and repr methods
    def __str__(self):
        return f'Car(position: {self.pos}'
    def __repr__(self):
        return f'Car - position = {self.pos}'


class Crossing:
    """class representing a single crossing"""
    def __init__(self, position, state):
        self.position = position
        self.state = state
        self.counter = 0

    def count(self):
        self.counter +=1

    def reset_counter(self):
        self.counter = 0

    def __repr__(self):
        return f'Crossing: position={self.position}, state={self.state}'


class City:
    """class representing a city filled with cars and traffic lights"""
    def __init__(self, road):
        l = list(road)
        self.cars = []
        self.crossings = {}
        self.length = len(road)
        
        counter = 0
        for x in l:
            if x == 'C':
                car = Car(counter)
                self.cars.append(car)
            elif x == 'G':
                crossing = Crossing(counter, 'G')
                self.crossings[counter] = crossing
            elif x == 'O':
                crossing = Crossing(counter, 'O')
                self.crossings[counter] = crossing
            elif x == 'R':
                crossing =Crossing(counter, 'R')
                self.crossings[counter] = crossing
            counter+=1
        self.cars.reverse()
        

    def move_city(self):
        """runs the lights and moves the cars"""
        _run_lights(self.crossings)
        _move_cars(self.cars, len(self.cars), self.crossings, self.length)


    def return_state(self):
        """prints the state of the road after one go"""
        road = []
        for a in range(self.length):
            road.append('.')
        for key, value in self.crossings.items():
            road[key] = value.state
        for car in self.cars:
            try:
                road[car.pos] = 'C'
            except IndexError:
                pass

        road = ('').join(road)
        return road



def _move_cars(cars, length, crossings, city_length):
    """moves the car following the rules of the game"""
    temporary_state = cars
    for x in range(length):
    
        
        if temporary_state[x].pos +1 == temporary_state[x-1].pos:
            continue


        if (temporary_state[x].pos + 1) in crossings.keys():
            if crossings[temporary_state[x].pos+1].state == 'G':
                #dumb way to solve the problem by adding these 2...
                if (((temporary_state[x].pos + 2) in [c.pos for c in temporary_state])
                and ((temporary_state[x].pos +2) < city_length)):
            
                    continue
                else:
                    temporary_state[x].move()
                
                
            elif crossings[temporary_state[x].pos+1].state == 'O':
                continue
            elif crossings[temporary_state[x].pos+1].state == 'R':
                continue
        else:
            temporary_state[x].move()
        cars = temporary_state

def _run_lights(crossings):
    """checks if the crossing lights should change and changes the lights if needed"""
    for key, value in crossings.items():

        value.count()
        
        if value.state =='G':
            if value.counter == 5:
                crossings[key].state = 'O'
                crossings[key].reset_counter()
        elif value.state =='R':
            if value.counter == 5:
                crossings[key].state = 'G'
                crossings[key].reset_counter()
        elif value.state == 'O':
            if value.counter == 1:
                crossings[key].state = 'R'
                crossings[key].reset_counter()

