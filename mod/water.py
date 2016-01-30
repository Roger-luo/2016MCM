class Water(object):
    """available water"""
    def __init__(self, curwater):
        self.curwater = curwater
        
    def __add__(self, water):
        return Water(self.curwater+water)

    def __repr__(self):
        print(self.curwater)

a = Water(2)
print((a+2))