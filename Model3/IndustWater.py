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
    pop = (Gaussian(Fit.PopulationFit(time),pPara)/Gaussian(Fit.PopulationFit(years[-1]),pPara))
    pcg = (Gaussian(Fit.PCGDPFit(time),gPara)/Gaussian(Fit.PCGDPFit(years[-1]),gPara))
    ele = (Gaussian(Fit.ElectricityFit(time),ePara)/Gaussian(Fit.ElectricityFit(years[-1]),ePara))
    spr = (Gaussian(Fit.SteelProductFit(time),sPara)/Gaussian(Fit.SteelProductFit(years[-1]),sPara))
    return Data.WaterUseIndustry[years[-1]]*(pop/4+pcg/4+ele/4+spr/4)

# comparedata(Data.Population,Data.WaterUseIndustry)
# comparedata(Data.PCGDP,Data.WaterUseIndustry)
# comparedata(Data.Electricity,Data.WaterUseIndustry)
# comparedata(Data.SteelProduct,Data.WaterUseIndustry)

# plt.figure()
# plt.scatter(years,[Data.WaterUseIndustry[t] for t in years],marker="^",s=100)
# plt.plot(years,IndustWater(years),'b-')
# plt.show()
# plt.close()
x = np.linspace(years[0],years[-1],100)

plt.figure()
plt.xlabel("Steel Production/ 10kt")
plt.ylabel("Industry Water Usage/ 100m m^3")
plt.scatter([Data.SteelProduct[t] for t in years],[Data.WaterUseIndustry[t] for t in years],marker="^",s=50,label='Raw Data')
plt.plot(Fit.SteelProductFit(x),Gaussian(Fit.SteelProductFit(x),sPara),'g-',label="Fit")
plt.legend()
plt.show()
plt.close()


plt.figure()
plt.xlabel("Population /10k people")
plt.ylabel("Industry Water Usage/ 100m m^3")
plt.scatter([Data.Population[t] for t in years],[Data.WaterUseIndustry[t] for t in years],marker="^",s=50,label='Raw Data')
plt.plot(Fit.PopulationFit(x),Gaussian(Fit.PopulationFit(x),pPara),'g-',label="Fit")
plt.legend()
plt.show()
plt.close()

plt.figure()
plt.xlabel("PCGDP /CNY")
plt.ylabel("Industry Water Usage/ 100m m^3")
plt.scatter([Data.PCGDP[t] for t in years],[Data.WaterUseIndustry[t] for t in years],marker="^",s=50,label='Raw Data')
plt.plot(Fit.PCGDPFit(x),Gaussian(Fit.PCGDPFit(x),gPara),'g-',label="Fit")
plt.legend()
plt.show()
plt.close()

plt.figure()
plt.xlabel("Electricity /100M kWh")
plt.ylabel("Industry Water Usage/ 100m m^3")
plt.scatter([Data.Electricity[t] for t in years],[Data.WaterUseIndustry[t] for t in years],marker="^",s=50,label='Raw Data')
plt.plot(Fit.ElectricityFit(x),Gaussian(Fit.ElectricityFit(x),ePara),'g-',label="Fit")
plt.legend()
plt.show()
plt.close()
