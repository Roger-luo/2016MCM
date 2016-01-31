import Data
import matplotlib.pyplot as plt

years=range(2004, 2015)

def Expo(x,p):
    return p[0]*np.exp(-p[1]*(x-p[2]))

def err(p, x, y):
    return Expo(x,p)-y

def para(datax,datay):
    

plt.figure()
plt.ylabel("Agriculture Water Usage/ 100m m^3")
plt.xlabel("Population/ 10k people")
plt.scatter([Data.Population[t] for t in years],[Data.WaterUseAgriculture[t] for t in years],marker="^",s=100)
plt.show()
plt.close()

plt.figure()
plt.ylabel("Agreculture Water Usage/ 100m m^3")
plt.xlabel("PCGDP/ CNY")
plt.scatter([Data.PCGDP[t] for t in years],[Data.WaterUseAgriculture[t] for t in years],marker="^",s=100)
plt.show()
plt.close()

plt.figure()
plt.ylabel("Agreculture Water Usage/ 100m m^3")
plt.xlabel("Irrigation Area/ kha")
plt.scatter([Data.IrrigationArea[t] for t in years],[Data.WaterUseAgriculture[t] for t in years],marker="^",s=100)
plt.show()
plt.close()