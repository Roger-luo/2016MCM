import Data
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

years=range(2004, 2015)

plt.figure()
plt.subplot(2,1,1)
plt.xlabel("Years")
plt.ylabel("Population/ 10k people")
plt.plot(list(Data.Population),[Data.Population[t] for t in list(Data.Population)], "bo")
plt.subplot(2,1,2)
plt.xlabel("Years")
plt.ylabel("GDP/ 100m CNY")
plt.plot(list(Data.GDP),[Data.GDP[t] for t in list(Data.GDP)], "ro")
plt.show()
plt.close() 

plt.figure()
plt.xlabel("Years")
plt.ylabel("PCGDP/ CNY")
plt.plot(list(Data.PCGDP),[Data.PCGDP[t] for t in list(Data.PCGDP)], "bo")
plt.show()
plt.close()

plt.figure()
plt.ylabel("Urban & Rural Engel Coef.")
plt.xlabel("Years")
plt.plot(list(Data.UrbanEngel), [Data.UrbanEngel[t] for t in list(Data.UrbanEngel)],"bs", label="Urban")
plt.plot(list(Data.RuralEngel), [Data.RuralEngel[t] for t in list(Data.RuralEngel)],"k^", label="Rural")
plt.legend(loc=0)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Years")
plt.ylabel("Irrigation Area/ kha")
plt.plot(list(Data.IrrigationArea), [Data.IrrigationArea[t] for t in list(Data.IrrigationArea)],"bo")
plt.show()
plt.close()

plt.figure()
plt.xlabel("Years")
plt.ylabel("Steel Production/ 10k t")
plt.plot(list(Data.SteelProduct), [Data.SteelProduct[t] for t in list(Data.SteelProduct)],"bo")
plt.show()
plt.close()

plt.figure()
plt.xlabel("Years")
plt.ylabel("Water Usage & Waste/ 100m m^3")
plt.plot(list(Data.WaterUseTotal),[Data.WaterUseTotal[t] for t in list(Data.WaterUseTotal) ],"ks",label="Total")
plt.plot(list(Data.WaterUseIndustry),[Data.WaterUseIndustry[t] for t in list(Data.WaterUseIndustry)],"co",label="Industrial")
plt.plot(list(Data.WaterUseAgriculture),[Data.WaterUseAgriculture[t] for t in list(Data.WaterUseAgriculture)],"b^",label="Agriculture")
plt.plot(list(Data.WaterUseResidential),[Data.WaterUseResidential[t] for t in list(Data.WaterUseResidential)],"gh",label="Domestic")
plt.plot(list(Data.WaterWasteTotal),[Data.WaterWasteTotal[t] for t in list(Data.WaterWasteTotal)],"yd",label="Waste Discharge")
plt.ylim(0,9000)
plt.legend(loc=0)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Years")
plt.ylabel("Water Storage/ 100m m^3")
plt.plot(list(Data.WaterTotal),[Data.WaterTotal[t] for t in list(Data.WaterTotal)],"ko",label="Total Storage")
plt.plot(list(Data.WaterSurface),[Data.WaterSurface[t] for t in list(Data.WaterSurface)],"co",label="Surface Storage")
plt.plot(list(Data.WaterUnderground),[Data.WaterUnderground[t] for t in list(Data.WaterUnderground)],"bo",label="Underground Storage")
plt.legend(loc=0)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Years")
plt.ylabel("Investment for Waste Water/ 10k CNY")
plt.plot(list(Data.WasteWaterInvestment), [Data.WasteWaterInvestment[t] for t in list(Data.WasteWaterInvestment)], "bo")
plt.show()
plt.close()

# analysis for GDP & Population
print("r(GDP,Population)="+str(spearmanr([Data.GDP[t] for t in years],[Data.Population[t] for t in years])))

# analysis for Wi
print("r(Wi,Population)="+str(spearmanr([Data.WaterUseIndustry[t] for t in years],[Data.Population[t] for t in years])))
print("r(Wi,GDP)="+str(spearmanr([Data.WaterUseIndustry[t] for t in years],[Data.GDP[t] for t in years])))
print("r(Wi,PCGDP)="+str(spearmanr([Data.WaterUseIndustry[t] for t in years],[Data.PCGDP[t] for t in years])))
print("r(Wi,SteelProduct)="+str(spearmanr([Data.WaterUseIndustry[t] for t in years],[Data.SteelProduct[t] for t in years])))

plt.figure()
plt.xlabel("Industry Water Usage/ 100m m^3")
plt.ylabel("Population/ 10k people")
plt.scatter([Data.WaterUseIndustry[t] for t in years],[Data.Population[t] for t in years],marker="^",s=100)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Industry Water Usage/ 100m m^3")
plt.ylabel("GDP/ 100m CNY")
plt.scatter([Data.WaterUseIndustry[t] for t in years],[Data.GDP[t] for t in years],marker="^",s=100)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Industry Water Usage/ 100m m^3")
plt.ylabel("PCGDP/ CNY")
plt.scatter([Data.WaterUseIndustry[t] for t in years],[Data.PCGDP[t] for t in years],marker="^",s=100)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Industry Water Usage/ 100m m^3")
plt.ylabel("Steel Production/ 10k t")
plt.scatter([Data.WaterUseIndustry[t] for t in years],[Data.SteelProduct[t] for t in years],marker="^",s=100)
plt.show()
plt.close()

# analysis for Wa
print("r(Wa,Population)="+str(spearmanr([Data.WaterUseAgriculture[t] for t in years],[Data.Population[t] for t in years])))
print("r(Wa,GDP)="+str(spearmanr([Data.WaterUseAgriculture[t] for t in years],[Data.GDP[t] for t in years])))
print("r(Wa,PCGDP)="+str(spearmanr([Data.WaterUseAgriculture[t] for t in years],[Data.PCGDP[t] for t in years])))
print("r(Wa,IrrigationArea)="+str(spearmanr([Data.WaterUseAgriculture[t] for t in years],[Data.IrrigationArea[t] for t in years])))


plt.figure()
plt.xlabel("Agriculture Water Usage/ 100m m^3")
plt.ylabel("Population/ 10k people")
plt.scatter([Data.WaterUseAgriculture[t] for t in years],[Data.Population[t] for t in years],marker="^",s=100)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Agreculture Water Usage/ 100m m^3")
plt.ylabel("GDP/ 100m CNY")
plt.scatter([Data.WaterUseAgriculture[t] for t in years],[Data.GDP[t] for t in years],marker="^",s=100)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Agreculture Water Usage/ 100m m^3")
plt.ylabel("PCGDP/ CNY")
plt.scatter([Data.WaterUseAgriculture[t] for t in years],[Data.PCGDP[t] for t in years],marker="^",s=100)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Agreculture Water Usage/ 100m m^3")
plt.ylabel("Irrigation Area/ kha")
plt.scatter([Data.WaterUseAgriculture[t] for t in years],[Data.IrrigationArea[t] for t in years],marker="^",s=100)
plt.show()
plt.close()

# analysis for Wr
print("r(Wr,Population)="+str(spearmanr([Data.WaterUseResidential[t] for t in years],[Data.Population[t] for t in years])))
print("r(Wr,GDP)="+str(spearmanr([Data.WaterUseResidential[t] for t in years],[Data.GDP[t] for t in years])))
print("r(Wr,PCGDP)="+str(spearmanr([Data.WaterUseResidential[t] for t in years],[Data.PCGDP[t] for t in years])))
print("r(Wr,RuralEngel)="+str(spearmanr([Data.WaterUseResidential[t] for t in years],[Data.RuralEngel[t] for t in years])))
print("r(Wr,UrbanEngel)="+str(spearmanr([Data.WaterUseResidential[t] for t in years],[Data.UrbanEngel[t] for t in years])))

plt.figure()
plt.xlabel("Domestic Water Usage/ 100m m^3")
plt.ylabel("Population/ 10k people")
plt.scatter([Data.WaterUseResidential[t] for t in years],[Data.Population[t] for t in years],marker="^",s=100)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Domestic Water Usage/ 100m m^3")
plt.ylabel("GDP/ 100m CNY")
plt.scatter([Data.WaterUseResidential[t] for t in years],[Data.GDP[t] for t in years],marker="^",s=100)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Domestic Water Usage/ 100m m^3")
plt.ylabel("PCGDP/ CNY")
plt.scatter([Data.WaterUseResidential[t] for t in years],[Data.PCGDP[t] for t in years],marker="^",s=100)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Domestic Water Usage/ 100m m^3")
plt.ylabel("Rural Engel Coef./ Percentage")
plt.scatter([Data.WaterUseResidential[t] for t in years],[Data.RuralEngel[t] for t in years],marker="^",s=100)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Domestic Water Usage/ 100m m^3")
plt.ylabel("Urban Engel Coef./ Percentage")
plt.scatter([Data.WaterUseResidential[t] for t in years],[Data.UrbanEngel[t] for t in years],marker="^",s=100)
plt.show()
plt.close()
