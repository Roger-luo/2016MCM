import Data
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from numpy import linspace
import Fit

years=range(2004, 2015)

def Gaussian(x,p):
    return p[0]*np.exp(-p[1]*(x-p[2])**2)

def err(p, x, y):
    return (Gaussian(x,p)-y)**2

def para(datax,datay):
    x = [datax[t] for t in years]
    y = [datay[t] for t in years]
    return leastsq(err,[y[0],1e-8,x[y.index(np.max(y))]],args=(x,y))[0]

def comparedata(datax,datay):
    Para = para(datax,datay)
    x = np.linspace(datax[years[0]],datax[years[-1]],100)
    y = Gaussian(x,Para)
    plt.figure()
    plt.scatter([datax[t] for t in years],[datay[t] for t in years],marker="^",s=100)  
    plt.plot(x,y,'b-')
    plt.show()
    plt.close()

pPara = para(Data.Population,Data.WaterUseIndustry)
gPara = para(Data.PCGDP,Data.WaterUseIndustry)
ePara = para(Data.Electricity,Data.WaterUseIndustry)
sPara = para(Data.SteelProduct,Data.WaterUseIndustry)

def IndustWater(time):
    pop = (Gaussian(Fit.PopulationFit(time),pPara)/Gaussian(Fit.PopulationFit(years[3]),pPara))
    pcg = (Gaussian(Fit.PCGDPFit(time),gPara)/Gaussian(Fit.PCGDPFit(years[3]),gPara))
    ele = (Gaussian(Fit.ElectricityFit(time),ePara)/Gaussian(Fit.ElectricityFit(years[3]),ePara))
    spr = (Gaussian(Fit.SteelProductFit(time),sPara)/Gaussian(Fit.SteelProductFit(years[3]),sPara))
    return Data.WaterUseIndustry[years[3]]*pop*pcg*ele*spr

# comparedata(Data.Population,Data.WaterUseIndustry)
# comparedata(Data.PCGDP,Data.WaterUseIndustry)
# comparedata(Data.Electricity,Data.WaterUseIndustry)
# comparedata(Data.SteelProduct,Data.WaterUseIndustry)

plt.figure()
plt.scatter(years,[Data.WaterUseIndustry[t] for t in years],marker="^",s=100)
plt.plot(years,IndustWater(years),'b-')
plt.show()
plt.close()
# plt.figure()
# plt.xlabel("Steel Production/ CNY")
# plt.ylabel("Industry Water Usage/ 100m m^3")
# plt.scatter([Data.SteelProduct[t] for t in years],[Data.WaterUseIndustry[t] for t in years],marker="^",s=100)
# plt.show()
# plt.close()
