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

f = open('ability.md','w')

for i in range(2014,2030):
    f.write('year:%s\n ability:%s\n'%(i,AverSupply(i)))

# plt.figure()
# plt.xlabel("years /yr")
# plt.ylabel("Ability /per person per yr 100m cubic meters")
# plt.scatter(years,[Data.WaterUseTotal[t]/Data.Population[t] for t in years],marker="^",s=100,label='raw data')
# plt.plot(range(2004,2030),[AverSupply(i) for i in range(2004,2030)],'b-',label="prediction")
# plt.legend(loc=0)
# plt.show()

# plt.figure()
# plt.xlabel("years /yr")
# plt.ylabel("Industrial Water Cost /100m cubic meters per yr")
# plt.scatter(years,[Data.WaterUseIndustry[t] for t in years],marker="^",s=100,label='raw data')
# plt.plot(range(2004,2030),[Wi(i) for i in range(2004,2030)],'b-',label="prediction")
# plt.legend(loc=0)
# plt.show()

# plt.figure()
# plt.xlabel("years /yr")
# plt.ylabel("Residential Water Cost /100m cubic meters per yr")
# plt.scatter(years,[Data.WaterUseResidential[t] for t in years],marker="^",s=100,label='raw data')
# plt.plot(range(2004,2030),[Wr(i) for i in range(2004,2030)],'b-',label="prediction")
# plt.legend(loc=0)
# plt.show()

# plt.figure()
# plt.xlabel("years /yr")
# plt.ylabel("Agricultural Water Cost /100m cubic meters per yr")
# plt.scatter(years,[Data.WaterUseAgriculture[t] for t in years],marker="^",s=100,label='raw data')
# plt.plot(range(2004,2030),[Wa(i) for i in range(2004,2030)],'b-',label="prediction")
# plt.legend(loc=0)
# plt.show()