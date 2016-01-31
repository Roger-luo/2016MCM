import numpy as np
from scipy.optimize import leastsq
import Fit

years=range(2004, 2015)

class IndustWater(object):
    """docstring for IndustWater"""
    def __init__(self, WaterUse, Pop, PCGDP, Elec, Steel):
        self.Pop = Pop
        self.PCGDP = PCGDP
        self.Elec = Elec
        self.Steel = Steel
        self.WaterUse = WaterUse
        
    def Gaussian(self, x,p):
        return p[0]*np.exp(-p[1]*(x-p[2])**2)

    def err(self, p, x, y):
        return (self.Gaussian(x,p)-y)**2

    def para(self, datax):
        x = [datax[t] for t in years]
        y = [self.WaterUse[t] for t in years]
        return leastsq(self.err,[y[0],1e-8,x[y.index(np.max(y))]],args=(x,y))[0]

    def __call__(self, time):
        pPara = self.para(self.Pop)
        gPara = self.para(self.PCGDP)
        ePara = self.para(self.Elec)
        sPara = self.para(self.Steel)
        pass
        pop = (self.Gaussian(Fit.PopulationFit(time),pPara)/self.Gaussian(Fit.PopulationFit(years[-1]),pPara))
        pcg = (self.Gaussian(Fit.PCGDPFit(time),gPara)/self.Gaussian(Fit.PCGDPFit(years[-1]),gPara))
        ele = (self.Gaussian(Fit.ElectricityFit(time),ePara)/self.Gaussian(Fit.ElectricityFit(years[-1]),ePara))
        spr = (self.Gaussian(Fit.SteelProductFit(time),sPara)/self.Gaussian(Fit.SteelProductFit(years[-1]),sPara))
        return self.WaterUse[years[-1]]*(pop/4+pcg/4+ele/4+spr/4)

class AgriWater(object):
    """docstring for AgriWater"""
    def __init__(self, WaterUse, Pop, PCGDP, IrrArea):
        self.Pop      = Pop
        self.PCGDP    = PCGDP
        self.IrrArea  = IrrArea
        self.WaterUse = WaterUse

    def Expo(self,x,p):
        return p[0]+p[1]*(x-p[2])

    def err(self,p, x, y):
        return self.Expo(x,p)-y

    def para(self,datax):
        x = [datax[t] for t in years]
        y = [self.WaterUse[t] for t in years]
        return leastsq(self.err,[y[0],1e-8,x[0]],args=(x,y))[0]

    def __call__(self,time):
        pPara = self.para(self.Pop)
        gPara = self.para(self.PCGDP)
        iPara = self.para(self.IrrArea)
        pop = (self.Expo(Fit.PopulationFit(time),pPara)/self.Expo(Fit.PopulationFit(years[-1]),pPara))
        pcg = (self.Expo(Fit.PCGDPFit(time),gPara)/self.Expo(Fit.PCGDPFit(years[-1]),gPara))
        ira = (self.Expo(Fit.IrrigationAreaFit(time),iPara)/self.Expo(Fit.IrrigationAreaFit(years[-1]),iPara))
        return self.WaterUse[years[-1]]*(pop/3+pcg/3+ira/3)

class ResWater(object):
    """docstring for ResWater"""
    def __init__(self, WaterUse, Pop, PCGDP):
        self.WaterUse = WaterUse
        self.Pop = Pop
        self.PCGDP = PCGDP

    def Expo(self,x,p):
        return p[0]*np.exp(-p[1]*(x-p[2]))

    def err(self,p, x, y):
        return self.Expo(x,p)-y

    def para(self,datax):
        x = [datax[t] for t in years]
        y = [self.WaterUse[t] for t in years]
        return leastsq(self.err,[y[0],1e-8,x[0]],args=(x,y))[0]
    
    def __call__(self,time):
        pPara = self.para(self.Pop)
        gPara = self.para(self.PCGDP)
        pop = (self.Expo(Fit.PopulationFit(time),pPara)/self.Expo(Fit.PopulationFit(years[-1]),pPara))
        pcg = (self.Expo(Fit.PCGDPFit(time),gPara)/self.Expo(Fit.PCGDPFit(years[-1]),gPara))
        return self.WaterUse[years[-1]]*(pop/2+pcg/2)