from WaterCost import *
import Data
import Fit
import matplotlib.pyplot as plt
import numpy as np

Wr = ResWater(Data.WaterUseResidential,Data.Population,Data.PCGDP)
Wi = IndustWater(Data.WaterUseIndustry,Data.Population,Data.PCGDP,Data.Electricity,Data.SteelProduct)
Wa = AgriWater(Data.WaterUseAgriculture,Data.Population,Data.PCGDP,Data.IrrigationArea)

def AverSupply(time):
    if time <2014 :
        return (Wr(time)+Wi(time)+Wa(time))/Fit.PopulationFit(time)
    else:
        return (Wr(time)+Wi(time)+Wa(time))/Fit.PopulationFit(time)

x = range(years[0],years[-1]+15)
# y = AverSupply(x)


print(AverSupply(years[-1]+15))

plt.figure()
plt.xlabel("years")
plt.scatter(years,[(Data.WaterUseTotal[t])/Data.Population[t] for t in years],marker="^",s=100)
plt.plot(x,[AverSupply(i) for i in x],'b-')
plt.show()
plt.close()