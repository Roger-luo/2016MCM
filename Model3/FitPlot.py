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

# fit of Urban Engel

def UrbanEngelFunction(t,p):
	return p[1]/(t-p[0])

def UrbanEngelResFunction(p):
	return np.array([UrbanEngelFunction(t,p)-Data.UrbanEngel[t] for t in Data.UrbanEngel])

UrbanEngelFitParam=leastsq(UrbanEngelResFunction,[1950,0.1])[0]
print(UrbanEngelFitParam)

def UrbanEngelFit(t):
	return UrbanEngelFunction(t, UrbanEngelFitParam)

# fit of Urban Engel

def RuralEngelFunction(t,p):
	return p[1]/(t-p[0])

def RuralEngelResFunction(p):
	return np.array([RuralEngelFunction(t,p)-Data.RuralEngel[t] for t in Data.RuralEngel])

RuralEngelFitParam=leastsq(RuralEngelResFunction,[1950,0.1])[0]
print(RuralEngelFitParam)
xs=linspace(1980, 2030, 256)
ys1=UrbanEngelFunction(xs, UrbanEngelFitParam)
ys2=RuralEngelFunction(xs, RuralEngelFitParam)
plt.figure()
plt.xlim(1975, 2035)
plt.xlabel("Years")
plt.ylabel("Urban & Rural Engel/ Percentage")
plt.plot(xs,ys1,"g-",linewidth=3, label="Urban Fitting")
plt.plot(list(Data.UrbanEngel),[Data.UrbanEngel[t] for t in Data.UrbanEngel], "bo", label="Urban Raw Data")
plt.plot(xs,ys2,"y-",linewidth=3, label="Rural Fitting")
plt.plot(list(Data.RuralEngel),[Data.RuralEngel[t] for t in Data.RuralEngel], "mo", label="Rural Raw Data")
plt.legend(loc=0)
plt.show()
plt.close()

def RuralEngelFit(t):
	return RuralEngelFunction(t, RuralEngelFitParam)

# fit electricity

def ElectricityFunction(t,p):
	return p[0]+p[1]*t+p[2]*t**2

def ElectricityResFunction(p):
	return np.array([ElectricityFunction(t,p)-Data.Electricity[t] for t in Data.Electricity])

ElectricityFitParam=leastsq(ElectricityResFunction,[30000,5000,1])[0]
print(ElectricityFitParam)
xs=linspace(2000, 2030, 256)
ys=ElectricityFunction(xs, ElectricityFitParam)
plt.figure()
plt.xlim(1995, 2035)
plt.xlabel("Years")
plt.ylabel("Electricity/ 100m kWh")
plt.plot(xs,ys,"g-",linewidth=3, label="Fitting")
plt.plot(list(Data.Electricity),[Data.Electricity[t] for t in Data.Electricity], "bo", label="Raw Data")
plt.legend(loc=0)
plt.show()
plt.close()

def ElectricityFit(t):
	return ElectricityFunction(t, ElectricityFitParam)
