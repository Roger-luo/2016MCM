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
    def __init__(self, pop, capacity, water, ifrstrc):
        self.pop = pop
        self.capacity = capacity
        self.water = water
        self.ifrstrc = ifrstrc

    def __repr__(self):
        return '%s\n%s'%(self.water,self.pop)