from WaterCost import *
import Data
import Base
import matplotlib.pyplot as plt
import numpy as np

pop = Base.Population(Data.Population)
pcg = Base.PCGDP(Data.PCGDP)
ira = Base.IrrArea(Data.IrrigationArea)
stl = Base.SteelProduct(Data.SteelProduct)
ele = Base.Electricity(Data.Electricity)


Wr = ResWater(Data.WaterUseResidential,pop,pcg)
Wi = IndustWater(Data.WaterUseIndustry,pop,pcg,ele,stl)
Wa = AgriWater(Data.WaterUseAgriculture,pop,pcg,ira)

def AverSupply(time):
    if time <2014 :
        return (Wr(time)+Wi(time)+Wa(time))/pop(time)
    else:
        return (Wr(time)+Wi(time)+Wa(time))/pop(time)

# x = range(years[0],years[-1]+15)
# # y = AverSupply(x)


# print(AverSupply(years[-1]+15))



plt.figure()
plt.xlabel("years")
plt.scatter(years,[Data.WaterUseTotal[t]/Data.Population[t] for t in years],marker="^",s=100)
plt.plot(range(2004,2030),[AverSupply(i) for i in range(2004,2030)],'b-')
plt.show()
# plt.close()