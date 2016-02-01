import Data
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from numpy import linspace
import numpy as np
# fit for population


def PopulationFunction(t,p):
    return p[2]/(1+np.exp(-p[1]*(t-p[0])))

def PopulationResFunction(p):
    return np.array([PopulationFunction(t,p)-Data.Population[t] for t in Data.Population])

PopulationFitParam=leastsq(PopulationResFunction,[1950,0.01,160000])[0]

def decrease(time):
    return np.array([0,0.0094*(time-2015),0])

def PopulationFit(t):
    if t<2014:
        return PopulationFunction(t, PopulationFitParam)
    else:
        return 1/(1/PopulationFitParam[2]+(1/Data.Population[2014]-1/PopulationFitParam[2])*np.exp(-0.03*(t-2014)))
# fit for PCGDP

def PCGDPFunction(t,p):
    return p[2]/(1+np.exp(-p[1]*(t-p[0])))

def PCGDPResFunction(p):
    return np.array([PCGDPFunction(t,p)-Data.PCGDP[t] for t in Data.PCGDP])

PCGDPFitParam=leastsq(PCGDPResFunction,[2050, 0.07, 200000])[0]

def PCGDPFit(t):
    return PCGDPFunction(t, PCGDPFitParam)

# fit for Irrigation Area

def IrrigationAreaFunction(t,p):
    return p[0]+p[1]*t+p[2]*t*t

def IrrigationAreaResFunction(p):
    return np.array([IrrigationAreaFunction(t,p)-Data.IrrigationArea[t] for t in Data.IrrigationArea])

IrrigationAreaFitParam=leastsq(IrrigationAreaResFunction,[1000,100,1])[0]

def IrrigationAreaFit(t):
    return IrrigationAreaFunction(t, IrrigationAreaFitParam)

# fit of steel product

def SteelProductFunction(t,p):
    return p[0]+p[1]*t+p[2]*t*t

def SteelProductResFunction(p):
    return np.array([SteelProductFunction(t,p)-Data.SteelProduct[t] for t in Data.SteelProduct])

SteelProductFitParam=leastsq(SteelProductResFunction,[1000,100,1])[0]

def SteelProductFit(t):
    return SteelProductFunction(t, SteelProductFitParam)

# fit of Urban Engel

def UrbanEngelFunction(t,p):
    return p[1]/(t-p[0])

def UrbanEngelResFunction(p):
    return np.array([UrbanEngelFunction(t,p)-Data.UrbanEngel[t] for t in Data.UrbanEngel])

UrbanEngelFitParam=leastsq(UrbanEngelResFunction,[1950,0.1])[0]

def UrbanEngelFit(t):
    return UrbanEngelFunction(t, UrbanEngelFitParam)

# fit of Urban Engel

def RuralEngelFunction(t,p):
    return p[1]/(t-p[0])

def RuralEngelResFunction(p):
    return np.array([RuralEngelFunction(t,p)-Data.RuralEngel[t] for t in Data.RuralEngel])

RuralEngelFitParam=leastsq(RuralEngelResFunction,[1950,0.1])[0]

def RuralEngelFit(t):
    return RuralEngelFunction(t, RuralEngelFitParam)

# fit electricity

def ElectricityFunction(t,p):
    return p[0]+p[1]*t+p[2]*t*t

def ElectricityResFunction(p):
    return np.array([ElectricityFunction(t,p)-Data.Electricity[t] for t in Data.Electricity])

ElectricityFitParam=leastsq(ElectricityResFunction,[30000,5000,1])[0]

def ElectricityFit(t):
    return ElectricityFunction(t, ElectricityFitParam)
