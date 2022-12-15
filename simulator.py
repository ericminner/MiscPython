import random
import math
from matplotlib import pyplot as plt
import numpy as np
#em3373

def normpdf(x, mean, sd):
    """
    Return the value of the normal distribution 
    with the specified mean and standard deviation (sd) at
    position x.
    You do not have to understand how this function works exactly. 
    """
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def pdeath(x, mean, sd):
    start = x-0.5
    end = x+0.5
    step =0.01    
    integral = 0.0
    while start<=end:
        integral += step * (normpdf(start,mean,sd) + normpdf(start+step,mean,sd)) / 2
        start += step            
    return integral    

mean = 3
sd = 0.2
    
recovery_time = 4 # recovery time in time-steps
virality = 0.9    # probability that a neighbor cell is infected in 
                  # each time step                                                  

class Cell(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y 
        self.state = "S" # can be "S" (susceptible), "R" (resistant = dead), or 
                         # "I" (infected)
        self.time = 0
    
    def __str__(self):
        return str(self.x) + ', ' + str(self.y)
    
    def infect(self):
        if self.state == 'S':
            self.state = 'I'
            self.time = 0
            
    def recover(self):
        if self.state == 'I':
            self.state = 'S'
            self.time = 0
            
    def death(self):
        if self.state == 'I':
            self.state = 'R'
            self.time = 0
            
            
    def process(self, adjacent_cells):
        if self.state == 'I':
            self.time += 1
            if self.time >= 4:
                self.recover()
                return
            
            death_random = random.random()
            death_probability = pdeath(self.time, mean, sd)
            
            if death_random < death_probability:
                self.death()
                return
            
            for cell in adjacent_cells:
                prb = random.random()
                if prb <= virality:
                    cell.infect()
        
        
        
class Map(object):
    
    cells = dict()
    
    def __init__(self):
        self.height = 150
        self.width = 150           
        self.cells = {}
        self.map = [[None]*self.height for i in range(self.width)]

    def add_cell(self, cell):
        self.cell = cell
        key = (cell.x, cell.y)
        self.cells[key] = self.cell
        
    def display(self):
        for h in range(self.height):
            for w in range(self.width):
                if (h,w) not in self.cells:
                    self.map[h][w] = (0.0, 0.0, 0.0)
                    continue
                state = self.cells[(h,w)].state
                if state == 'S':
                    self.map[h][w] = (0.0, 1.0, 0.0)
                elif state == 'R':
                    self.map[h][w] = (0.5, 0.5, 0.5)
                else: 
                    self.map[h][w] = (1.0, 0.0, 0.0)
                
        plt.imshow(self.map)
        
    def adjacent_cells(self, x,y):
        
        adj = []
        if x < 150 and (x+1, y) in self.cells:
            adj.append(self.cells[(x+1, y)])
        if y < 150 and (x, y+1) in self.cells:
            adj.append(self.cells[(x, y+1)])
        if x > 0 and (x-1, y) in self.cells:
            adj.append(self.cells[(x-1, y)])
        if y > 0 and (x, y-1) in self.cells:
            adj.append(self.cells[(x, y-1)])
            
        return adj
    
    
    def time_step(self):
        for h in range(self.height):
           for w in range(self.width):
               if (h,w) not in self.cells:
                   continue
               cell = self.cells[(h,w)]
               if cell.state == 'I':
                   a = self.adjacent_cells(h,w)
                   cell.process(a)
        
        self.display()
        
def read_map(filename):
    
    m = Map()
    
    f = open(filename,'r')
    
    for line in f:
        coordinates = line.strip().split(',')
        c = Cell(int(coordinates[0]),int(coordinates[1]))
        Map.add_cell(m, c)

    return m

name = 'nyc_map.csv'
m = read_map(name)
m.cells[(118,78)].infect()
m.display()

for i in range(30):
    m.time_step()
    plt.pause(0.001)

plt.show()


