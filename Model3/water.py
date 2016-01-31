class water(object):
    """water"""
    def __init__(self, water_storage, water_supply, waste_water):
        self.water_storage = water_storage
        self.water_supply = water_supply
        self.waste_water = waste_water

    def __repr__(self):
        return 'water storage:%s\nwater supply:%s\nwaste water:%s'%(self.water_storage,self.water_supply,self.waste_water)

    def next(self):
        self.water_storage -=self.water_supply
        self.waste_water   +=self.water_supply