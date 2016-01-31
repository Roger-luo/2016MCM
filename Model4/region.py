import numpy as np
from numpy.random import randn

class Region(object):
    """docstring for Region"""
    def __init__(self, pop, capacity, water, ifrstrc, pGDP, year, dt):
        self.pop = pop
        self.capacity = capacity
        self.water = water
        self.ifrstrc = ifrstrc
        self.pGDP = pGDP
        self.year = year
        self.dt = dt
 
    def mu(self):
        return 0

    def sigma(self):
        return 0

    def nextstep(self):
        self.water.water_supply = self.water.water_supply+self.water.water_supply*(self.mu()*self.dt+self.sigma()*np.sqrt(self.dt)*randn())

    def nextyear(self):
        for i in np.linspace(0,1,100):
            self.nextstep()

class infras(object):
    """object for infrastructure"""
    def __init__(self, dam, recycle):
        self.dam = dam
        self.recycle = recycle

    def average(self):
        return self.dam+self.recycle

    def variance(self):
        return 0

    def recycle(self):
        return 0

    def desalt(self):
        return 0

    def produce(self):
        return self.recycle()+self.desalt()

class water(object):
           """docstring for water"""
           def __init__(self, water_storage, water_supply, water_waste):
               self.water_storage = water_storage
               self.water_supply = water_supply
               self.water_waste = water_waste
                      