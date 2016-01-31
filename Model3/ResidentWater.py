import Data
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from numpy import linspace
import Fit

years=range(2004, 2015)

def Expo(x,p):
    return p[0]*np.exp(-p[1]*(x-p[2]))

def err(p, x, y):
    return Expo(x,p)-y

def para(datax,datay):
    x = [datax[t] for t in years]
    y = [datay[t] for t in years]
    return leastsq(err,[y[0],1e-8,x[0]],args=(x,y))[0]

def comparedata(datax,datay,xlabel,ylabel):
    Para = para(datax,datay)
    x = np.linspace(datax[years[0]],datax[years[-1]],100)
    y = Expo(x,Para)
    plt.figure()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.scatter([datax[t] for t in years],[datay[t] for t in years],marker="^",s=100)  
    plt.plot(x,y,'b-')
    plt.show()
    plt.close()


pPara = para(Data.Population,Data.WaterUseResidential)
gPara = para(Data.PCGDP,Data.WaterUseResidential)
def ResidentWater(time):
    pop = (Expo(Fit.PopulationFit(time),pPara)/Expo(Fit.PopulationFit(years[-1]),pPara))
    pcg = (Expo(Fit.PCGDPFit(time),gPara)/Expo(Fit.PCGDPFit(years[-1]),gPara))
    return Data.WaterUseResidential[years[-1]]*(pop/2+pcg/2)

# plt.figure()
# plt.scatter(years,[Data.WaterUseResidential[t] for t in years],marker="^",s=100)
# plt.plot(years,ResidentWater(years),'b-')
# plt.show()
# plt.close()

# plt.figure()
# plt.ylabel("Domestic Water Usage/ 100m m^3")
# plt.xlabel("UrbanEngel/ Percentage")
# plt.scatter([Data.UrbanEngel[t] for t in years],[Data.WaterUseResidential[t] for t in years],marker="^",s=100)
# plt.show()
# plt.close()