import numpy as np
import numpy.random as random

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

class Region(object):
    """Region"""
    def __init__(self, pop, capacity, water, ifrstrc, dt):
        self.pop = pop
        self.capacity = capacity
        self.water = water
        self.ifrstrc = ifrstrc
        self.dt = dt

    def __repr__(self):
        return '%s\n%s'%(self.water,self.pop)

    def next_timestep(self):
        return self.mu()*self.dt+self.sigma()

    def mu(self):
        return (self.water-self.cost()+self.produce())/self.water

    def sigma(self):
        return self.uncrt_produce()-self.uncrt_cost()+np.sqrt(dt)*random.randn()

    def uncrt_cost(self):
        return

    def uncrt_produce(self):
        return

    def cost(self):
        return self.agriculture()+self.industrial()+self.resident()

    def produce(self):
        return self.waterrecycle()

    def waterrecycle(self):
        return

    def agriculture(self):
        return

    def industrial(self):
        pass

    def resident(self):
        pass


Region()