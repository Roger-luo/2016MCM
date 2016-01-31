import Data
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from numpy import linspace

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


# comparedata(Data.Population,Data.WaterUseResidential,"Population/ 10k people","Domestic Water Usage/ 100m m^3")
# comparedata(Data.PCGDP,Data.WaterUseResidential,"PCGDP/ CNY","Domestic Water Usage/ 100m m^3")

pPara = para(Data.Population,Data.WaterUseResidential)
gPara = para(Data.PCGDP,Data.WaterUseResidential)
def ResidentWater(time):
    return Data.WaterUseResidential[years[0]]*(Expo(time,pPara)/Expo(years[0],pPara))*(Expo(time,gPara)/Expo(years[0],gPara))


plt.figure()
plt.scatter(years,[Data.WaterUseResidential[t] for t in years])
plt.plot(years,ResidentWater(years),'b-')
plt.show()
plt.close()

# plt.figure()
# plt.ylabel("Domestic Water Usage/ 100m m^3")
# plt.xlabel("Rural Engel/ Percentage")
# plt.scatter([Data.RuralEngel[t] for t in years],[Data.WaterUseResidential[t] for t in years],marker="^",s=100)
# plt.show()
# plt.close()

# plt.figure()
# plt.ylabel("Domestic Water Usage/ 100m m^3")
# plt.xlabel("UrbanEngel/ Percentage")
# plt.scatter([Data.UrbanEngel[t] for t in years],[Data.WaterUseResidential[t] for t in years],marker="^",s=100)
# plt.show()
# plt.close()