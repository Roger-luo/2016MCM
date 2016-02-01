import numpy as np
from scipy.optimize import leastsq

years=range(2004, 2015)

class IndustWater(object):
    """docstring for IndustWater"""
    def __init__(self, WaterUse, Pop, PCGDP, Elec, Steel):
        self.Pop = Pop
        self.PCGDP = PCGDP
        self.Elec = Elec
        self.Steel = Steel
        self.WaterUse = WaterUse
        pass
        self.pcoeff = self.para(self.Pop.data)
        self.gcoeff = self.para(self.PCGDP.data)
        self.ecoeff = self.para(self.Elec.data)
        self.scoeff = self.para(self.Steel.data)
        pass
        self.pvar = self.variance(self.Pop,self.pcoeff)
        self.gvar = self.variance(self.PCGDP,self.gcoeff)
        self.evar = self.variance(self.Elec,self.ecoeff)
        self.svar = self.variance(self.Steel,self.scoeff)
        
    def Gaussian(self, x,p):
        return p[0]*np.exp(-p[1]*(x-p[2])**2)

    def err(self, p, x, y):
        return self.Gaussian(x,p)-y

    def para(self, datax):
        x = [datax[t] for t in years]
        y = [self.WaterUse[t] for t in years]
        return leastsq(self.err,[y[0],1e-8,x[y.index(np.max(y))]],args=(x,y))[0]

    def variance(self, ob, coeff):
        return np.mean([(ob.data[i]-self.Gaussian(i,coeff))**2 for i in years])

    def __call__(self, time, intr=False):
        if time>2015 and intr==True:
            self.pcoeff[1] *= np.exp(1e-1*(2015-time))
            self.gcoeff[1] *= np.exp(1e-1*(2015-time))
            self.ecoeff[1] *= np.exp(1e-1*(2015-time))
            self.scoeff[1] *= np.exp(1e-1*(2015-time))
        pass
        pop = (self.Gaussian(self.Pop(time,intr),self.pcoeff)/self.Gaussian(self.Pop(years[-1],intr),self.pcoeff))
        pcg = (self.Gaussian(self.PCGDP(time,intr),self.gcoeff)/self.Gaussian(self.PCGDP(years[-1],intr),self.gcoeff))
        ele = (self.Gaussian(self.Elec(time,intr),self.ecoeff)/self.Gaussian(self.Elec(years[-1],intr),self.ecoeff))
        spr = (self.Gaussian(self.Steel(time,intr),self.scoeff)/self.Gaussian(self.Steel(years[-1],intr),self.scoeff))
        # print((pop/4+pcg/4+ele/4+spr/4))
        return self.WaterUse[years[-1]]*(0.584*pop+0.565*pcg+0.577*ele+0.577*spr)/2.303

class AgriWater(object):
    """docstring for AgriWater"""
    def __init__(self, WaterUse, Pop, PCGDP, IrrArea):
        self.Pop      = Pop
        self.PCGDP    = PCGDP
        self.IrrArea  = IrrArea
        self.WaterUse = WaterUse
        self.pcoeff = self.para(self.Pop.data)
        self.gcoeff = self.para(self.PCGDP.data)
        self.icoeff = self.para(self.IrrArea.data)

    def Expo(self,x,p):
        return p[0]+p[1]*(x-p[2])

    def err(self,p, x, y):
        return self.Expo(x,p)-y

    def para(self,datax):
        x = [datax[t] for t in years]
        y = [self.WaterUse[t] for t in years]
        return leastsq(self.err,[y[0],1e-8,x[0]],args=(x,y))[0]

    def __call__(self,time,intr=False):
        pop = (self.Expo(self.Pop(time,intr),self.pcoeff)/self.Expo(self.Pop(years[-1],intr),self.pcoeff))
        pcg = (self.Expo(self.PCGDP(time,intr),self.gcoeff)/self.Expo(self.PCGDP(years[-1],intr),self.gcoeff))
        ira = (self.Expo(self.IrrArea(time,intr),self.icoeff)/self.Expo(self.IrrArea(years[-1],intr),self.icoeff))
        return self.WaterUse[years[-1]]*(0.878*pop+0.882*pcg+0.879*ira)/2.639

class ResWater(object):
    """docstring for ResWater"""
    def __init__(self, WaterUse, Pop, PCGDP):
        self.WaterUse = WaterUse
        self.Pop = Pop
        self.PCGDP = PCGDP
        self.pcoeff = self.para(self.Pop.data)
        self.gcoeff = self.para(self.PCGDP.data)

    def Expo(self,x,p):
        return p[0]+p[1]*(x-p[2])

    def err(self,p, x, y):
        return self.Expo(x,p)-y

    def para(self,datax):
        x = [datax[t] for t in years]
        y = [self.WaterUse[t] for t in years]
        return leastsq(self.err,[y[0],1e-8,x[0]],args=(x,y))[0]
    
    def __call__(self,time,intr=False):
        pop = (self.Expo(self.Pop(time,intr),self.pcoeff)/self.Expo(self.Pop(years[-1],intr),self.pcoeff))
        pcg = (self.Expo(self.PCGDP(time,intr),self.gcoeff)/self.Expo(self.PCGDP(years[-1],intr),self.gcoeff))
        return self.WaterUse[years[-1]]*(0.808*pop+0.796*pcg)/1.604