import Data
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from numpy import linspace

# fit for population


def PopulationFunction(t,p):
	return p[2]/(1+np.exp(-p[1]*(t-p[0])))

def PopulationResFunction(p):
	return np.array([PopulationFunction(t,p)-Data.Population[t] for t in Data.Population])

PopulationFitParam=leastsq(PopulationResFunction,[1950,0.01,160000])[0]
print(PopulationFitParam)
xs=linspace(1950, 2030, 256)
ys=PopulationFunction(xs, PopulationFitParam)
plt.figure()
plt.xlim(1945, 2035)
plt.xlabel("Years")
plt.ylabel("Population/ 10k people")
plt.plot(xs,ys,"g-",linewidth=3, label="Fitting")
plt.plot(list(Data.Population),[Data.Population[t] for t in list(Data.Population)], "bo", label="Raw Data")
plt.legend(loc=0)
plt.show()
plt.close()

def PopulationFit(t):
	return PopulationFunction(t, PopulationFitParam)

# fit for PCGDP

def PCGDPFunction(t,p):
	return p[2]/(1+np.exp(-p[1]*(t-p[0])))

def PCGDPResFunction(p):
	return np.array([PCGDPFunction(t,p)-Data.PCGDP[t] for t in Data.PCGDP])

PCGDPFitParam=leastsq(PCGDPResFunction,[2050, 0.07, 200000])[0]
print(PCGDPFitParam)
xs=linspace(1975, 2030, 256)
ys=PCGDPFunction(xs, PCGDPFitParam)
plt.figure()
plt.xlim(1970, 2035)
plt.xlabel("Years")
plt.ylabel("PCGDP/ CNY")
plt.plot(xs,ys,"g-",linewidth=3, label="Fitting")
plt.plot(list(Data.PCGDP),[Data.PCGDP[t] for t in list(Data.PCGDP)], "bo", label="Raw Data")
plt.legend(loc=0)
plt.show()
plt.close()

def PCGDPFit(t):
	return PCGDPFunction(t, PCGDPFitParam)

# fit for Irrigation Area

def IrrigationAreaFunction(t,p):
	return p[0]+p[1]*t+p[2]*t**2

def IrrigationAreaResFunction(p):
	return np.array([IrrigationAreaFunction(t,p)-Data.IrrigationArea[t] for t in Data.IrrigationArea])

IrrigationAreaFitParam=leastsq(IrrigationAreaResFunction,[1000,100,1])[0]
print(IrrigationAreaFitParam)
xs=linspace(1977, 2030, 256)
ys=IrrigationAreaFunction(xs, IrrigationAreaFitParam)
plt.figure()
plt.xlim(1970, 2035)
plt.xlabel("Years")
plt.ylabel("Irrigation Area/ kha")
plt.plot(xs,ys,"g-",linewidth=3, label="Fitting")
plt.plot(list(Data.IrrigationArea),[Data.IrrigationArea[t] for t in Data.IrrigationArea], "bo", label="Raw Data")
plt.legend(loc=0)
plt.show()
plt.close()

def IrrigationAreaFit(t):
	return IrrigationAreaFunction(t, IrrigationAreaFitParam)

# fit of steel product

def SteelProductFunction(t,p):
	return p[0]+p[1]*t+p[2]*t**2

def SteelProductResFunction(p):
	return np.array([SteelProductFunction(t,p)-Data.SteelProduct[t] for t in Data.SteelProduct])

SteelProductFitParam=leastsq(SteelProductResFunction,[1000,100,1])[0]
print(SteelProductFitParam)
xs=linspace(1997, 2030, 256)
ys=SteelProductFunction(xs, SteelProductFitParam)
plt.figure()
plt.xlim(1993, 2035)
plt.xlabel("Years")
plt.ylabel("Steel Product/ 10k t")
plt.plot(xs,ys,"g-",linewidth=3, label="Fitting")
plt.plot(list(Data.SteelProduct),[Data.SteelProduct[t] for t in Data.SteelProduct], "bo", label="Raw Data")
plt.legend(loc=0)
plt.show()
plt.close()

def SteelProductFit(t):
	return SteelProductFunction(t, SteelProductFitParam)