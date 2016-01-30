import numpy as np
import numpy.random as random

class WaterAmount(object):
    """the whole quantum of water in a given region"""
    def __init__(self, available, waste):
        self.available = available
        self.waste = waste

    def __repr__(self):
        return 'available water: %s\nwaste water: %s'%(self.available,self.waste)

    def next_available(self, mu, sigma, dt):
        return self.available + self.available*(mu*dt+np.sqrt(dt)*random.randn())

    def avlb(self,time,mu,sigma, dt=1e-3):
        for i in np.linspace(0,dt,time):
            self.available = self.next_available(mu,sigma,dt)


a = WaterAmount(2,3)

a.avlb(10,1,0.4)

print(a)