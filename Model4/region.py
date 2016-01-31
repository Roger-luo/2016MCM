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

    def nextstep(self):
        return self.water_supply

    def nextyear(self):
        for 

class water(object):
           """docstring for water"""
           def __init__(self, water_storage, water_supply, water_waste):
               self.water_storage = water_storage
               self.water_supply = water_supply
               self.water_waste = water_waste
                      