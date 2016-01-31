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

p=leastsq(PopulationResFunction,[1950,0.01,160000])[0]
print(p)
xs=linspace(1950, 2030, 256)
ys=PopulationFunction(xs, p)
plt.figure()
plt.xlim(1945, 2035)
plt.xlabel("Years")
plt.ylabel("Population/ 10k people")
plt.plot(xs,ys,"g-",linewidth=3)
plt.plot(list(Data.Population),[Data.Population[t] for t in list(Data.Population)], "bo")
plt.show()
plt.close()

def PopulationFit(t):
	return PopulationFunction(t, p)

# fit for PCGDP

def PCGDPFunction(t,p):
	return p[2]/(1+np.exp(-p[1]*(t-p[0])))

def PCGDPResFunction(p):
	return np.array([PCGDPFunction(t,p)-Data.PCGDP[t] for t in Data.PCGDP])

p=leastsq(PCGDPResFunction,[2050, 0.07, 200000])[0]
print(p)
xs=linspace(1975, 2030, 256)
ys=PCGDPFunction(xs, p)
plt.figure()
plt.xlim(1970, 2035)
plt.xlabel("Years")
plt.ylabel("PCGDP/ CNY")
plt.plot(xs,ys,"g-",linewidth=3)
plt.plot(list(Data.PCGDP),[Data.PCGDP[t] for t in list(Data.PCGDP)], "bo")
plt.show()
plt.close()

def PCGDPFit(t):
	return PCGDPFunction(t, p)

# fit for Irrigation Area

def IrrigationAreaFunction(t,p):
	return p[0]+p[1]*t+p[2]*t**2

def IrrigationAreaResFunction(p):
	return np.array([IrrigationAreaFunction(t,p)-Data.IrrigationArea[t] for t in Data.IrrigationArea])

p=leastsq(IrrigationAreaResFunction,[1000,100,1])[0]
print(p)
xs=linspace(1977, 2030, 256)
ys=IrrigationAreaFunction(xs, p)
plt.figure()
plt.xlim(1970, 2035)
plt.xlabel("Years")
plt.ylabel("Irrigation Area/ kha")
plt.plot(xs,ys,"g-",linewidth=3)
plt.plot(list(Data.IrrigationArea),[Data.IrrigationArea[t] for t in Data.IrrigationArea], "bo")
plt.show()
plt.close()

def IrrigationAreaFit(t):
	return IrrigationAreaFunction(t, p)