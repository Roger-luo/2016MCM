import numpy as np
import numpy.random as random
import water
class population(object):
    """population"""
    def __init__(self, population, icrrate):
        self.population = population
        self.icrrate = icrrate

    def __repr__(self):
        return 'current population: %s'%self.population

    def next_timestep(self, region):
        self.population*(1-region.capacity)


class infras(object):
    """object for infrastructure"""
    def __init__(self, dam, recycle):
        self.dam = dam
        self.recycle = recycle

    def average(self):
        return self.dam+self.recycle

    def variance(self):
        return 0

class Region(object):
    """Region"""
    def __init__(self, pop, capacity, water, ifrstrc, dt):
        super(Region, self).__init__()
        self.pop = pop
        self.capacity = capacity
        self.water = water
        self.ifrstrc = ifrstrc
        self.dt = dt

    def __repr__(self):
        return '%s\naverage water supply:%s'%(self.water,self.water.water_supply/self.pop)

    def agriculture_supply(self, supply):
        return 0

    def industrial_supply(self, supply):
        return 0

    def resident_supply(self, supply):
        return 0




w = water.water(2,3,4)
i = infras(2,2)
r = Region(20,100,w,i,1e-3)

print(r)