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
        
    def Gaussian(self, x,p):
        return (p[0]+p[1]*(x-p[2])**2)**2

    def err(self, p, x, y):
        return self.Gaussian(x,p)-y

    def para(self, datax):
        x = [datax[t] for t in years]
        y = [self.WaterUse[t] for t in years]
        return leastsq(self.err,[y[0],1e-8,x[y.index(np.max(y))]],args=(x,y))[0]

    def __call__(self, time):
        pPara = self.para(self.Pop.data)
        gPara = self.para(self.PCGDP.data)
        ePara = self.para(self.Elec.data)
        sPara = self.para(self.Steel.data)
        # if time>2015:
        #     pPara[1] *= np.exp(1e-1*(2015-time))
        #     gPara[1] *= np.exp(1e-1*(2015-time))
        #     ePara[1] *= np.exp(1e-1*(2015-time))
        #     sPara[1] *= np.exp(1e-1*(2015-time))
        pass
        pop = (self.Gaussian(self.Pop(time),pPara)/self.Gaussian(self.Pop(years[-1]),pPara))
        pcg = (self.Gaussian(self.PCGDP(time),gPara)/self.Gaussian(self.PCGDP(years[-1]),gPara))
        ele = (self.Gaussian(self.Elec(time),ePara)/self.Gaussian(self.Elec(years[-1]),ePara))
        spr = (self.Gaussian(self.Steel(time),sPara)/self.Gaussian(self.Steel(years[-1]),sPara))
        # print((pop/4+pcg/4+ele/4+spr/4))
        return self.WaterUse[years[-1]]*(pop/4+pcg/4+ele/4+spr/4)

class AgriWater(object):
    """docstring for AgriWater"""
    def __init__(self, WaterUse, Pop, PCGDP, IrrArea):
        self.Pop      = Pop
        self.PCGDP    = PCGDP
        self.IrrArea  = IrrArea
        self.WaterUse = WaterUse

    def Expo(self,x,p):
        return p[0]+p[1]*x

    def err(self,p, x, y):
        return self.Expo(x,p)-y

    def para(self,datax):
        x = [datax[t] for t in years]
        y = [self.WaterUse[t] for t in years]
        return leastsq(self.err,[y[0],1e-8],args=(x,y))[0]

    def __call__(self,time):
        pPara = self.para(self.Pop.data)
        gPara = self.para(self.PCGDP.data)
        iPara = self.para(self.IrrArea.data)
        pop = (self.Expo(self.Pop(time),pPara)/self.Expo(self.Pop(years[-1]),pPara))
        pcg = (self.Expo(self.PCGDP(time),gPara)/self.Expo(self.PCGDP(years[-1]),gPara))
        ira = (self.Expo(self.IrrArea(time),iPara)/self.Expo(self.IrrArea(years[-1]),iPara))
        return self.WaterUse[years[-1]]*(pop/3+pcg/3+ira/3)

class ResWater(object):
    """docstring for ResWater"""
    def __init__(self, WaterUse, Pop, PCGDP):
        self.WaterUse = WaterUse
        self.Pop = Pop
        self.PCGDP = PCGDP

    def Expo(self,x,p):
        return p[0]+p[1]*x

    def err(self,p, x, y):
        return self.Expo(x,p)-y

    def para(self,datax):
        x = [datax[t] for t in years]
        y = [self.WaterUse[t] for t in years]
        return leastsq(self.err,[y[0],1e-8],args=(x,y))[0]
    
    def __call__(self,time):
        pPara = self.para(self.Pop.data)
        gPara = self.para(self.PCGDP.data)
        pop = (self.Expo(self.Pop(time),pPara)/self.Expo(self.Pop(years[-1]),pPara))
        pcg = (self.Expo(self.PCGDP(time),gPara)/self.Expo(self.PCGDP(years[-1]),gPara))
        return self.WaterUse[years[-1]]*(pop/2+pcg/2)