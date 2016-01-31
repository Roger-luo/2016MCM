from WaterCost import *
import Data
import Fit
import matplotlib.pyplot as plt
import numpy as np

Wr = ResWater(Data.WaterUseResidential,Data.Population,Data.PCGDP)
Wi = IndustWater(Data.WaterUseIndustry,Data.Population,Data.PCGDP,Data.Electricity,Data.SteelProduct)
Wa = AgriWater(Data.WaterUseAgriculture,Data.Population,Data.PCGDP,Data.IrrigationArea)

def AverSupply(time):
    return (Wr(time)+Wi(time)+Wa(time))/Fit.PopulationFit(time)

x = range(years[0],years[-1]+15)
y = AverSupply(x)

plt.figure()
plt.plot(x,y,'b-')
plt.show()
plt.close()