import Data
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from numpy import linspace
import Fit

years=range(2004, 2015)

def Expo(x,p):
    return p[0]+p[1]*(x-p[2])

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

# comparedata(Data.Population,Data.WaterUseAgriculture,"Population/ 10k people","Agriculture Water Usage/ 100m m^3")
# comparedata(Data.PCGDP,Data.WaterUseAgriculture,"PCGDP/ CNY","Agreculture Water Usage/ 100m m^3")
# comparedata(Data.IrrigationArea,Data.WaterUseAgriculture,"Irrigation Area/ kha","Agreculture Water Usage/ 100m m^3")

pPara = para(Data.Population,Data.WaterUseAgriculture)
gPara = para(Data.PCGDP,Data.WaterUseAgriculture)
iPara = para(Data.IrrigationArea,Data.WaterUseAgriculture)

def AgricultureWater(time):
    pop = (Expo(Fit.PopulationFit(time),pPara)/Expo(Fit.PopulationFit(years[-1]),pPara))
    pcg = (Expo(Fit.PCGDPFit(time),gPara)/Expo(Fit.PCGDPFit(years[-1]),gPara))
    ira = (Expo(Fit.IrrigationAreaFit(time),iPara)/Expo(Fit.IrrigationAreaFit(years[-1]),iPara))
    return Data.WaterUseAgriculture[years[-1]]*pop*pcg*ira

plt.figure()
plt.scatter(years,[Data.WaterUseAgriculture[i] for i in years],marker="^",s=100)
plt.plot(years,AgricultureWater(years),'b-')
plt.show()
plt.close()