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

    def recycle(self):
        return 0

    def desalt(self):
        return 0

    def produce(self):
        return self.recycle()+self.desalt()

class year(object):
    """year"""
    def __init__(self, year):
        self.year = year

    def __repr__(self):
        return 'current year: %s'%(year)


class perCapitaGDP(object):
    """per capita GDP"""
    def __init__(self, GDP):
        self.GDP = GDP

    def __repr__(self):
        return 'per Capita GDP: %s'%self.GDP

class Region(object):
    """Region"""
    def __init__(self, pop, capacity, water, ifrstrc, pGDP, year, dt):
        super(Region, self).__init__()
        self.pop = pop
        self.capacity = capacity
        self.water = water
        self.ifrstrc = ifrstrc
        self.dt = dt
        self.pGDP = pGDP
        self.year = year

    def __repr__(self):
        return '%s\naverage water supply:%s'%(self.water,self.water.water_supply/self.pop.population)

    #industrial water supply after dt
    def indust_next(self):
        return 0

    def agriculture_next(self):
        return 0

    def resident_next(self):
        return 0

    #supply after next time step
    def supplynext(self):
        self.water.supply = self.indust_next()+self.agriculture_next()+self.resident_next()
        self.water.next()

    def climate(self):
        return 0

    def nextadd(self):
        waterget = self.ifrstrc.produce()+self.climate()
        self.water.water_storage += waterget
        self.water.waste_water -= waterget

    def evolute(self):
        for i in np.linspace(0,dt,1):
            supplynext()
            nextadd()
        self.year+=1


w = water.water(2,3,4)
i = infras(2,2)
r = Region(population(2,2), 20, w, i, 20, year(2000), 1e-3)

print(r)