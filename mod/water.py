class Water(object):
    """water"""
    def __init__(self, curwater):
        self.curwater = curwater

    def __add__(self, water):
        return Water(self.curwater+water)

    def __sub__(self, water):
        return Water(self.curwater-water)

    def __mul__(self, water):
        return Water(self.curwater*water)

    def __div__(self, water):
        return Water(self.curwater/water)

    def __repr__(self):
        return 'water storage:%s'%self.curwater


class AvailableWater(Water):
    """Available Water"""
    def __init__(self, curwater):
        super(AvailableWater, self).__init__(curwater)

    def __repr__(self):
        return 'Available water storage:%s'%self.curwater

class WasteWater(Water):
    """Waste Water"""
    def __init__(self, curwater):
        super(WasteWater, self).__init__(curwater)

    def __repr__(self):
        return 'waste water quantum:%s'%self.curwater


class WaterAmount(object):
    """the whole quantum of water in a given region"""
    def __init__(self, available, waste):
        self.available = available
        self.waste = waste

    def __repr__(self):
        return 'available water: %s\nwaste water: %s'%(self.available,self.waste)
