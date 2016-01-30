import Data
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

years=range(2004, 2015)

plt.figure()
plt.subplot(2,1,1)
plt.xlabel("Years")
plt.ylabel("Population/ 10k people")
plt.plot(years,[Data.Population[t] for t in years], "bo-", markersize=10)
plt.subplot(2,1,2)
plt.xlabel("Years")
plt.ylabel("GDP/ 100m CNY")
plt.plot(years,[Data.GDP[t] for t in years], "ro-", markersize=10)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Years")
plt.ylabel("Water Usage & Waste/ 100m m^3")
plt.plot(years,[Data.WaterUseTotal[t] for t in years],"ko-",label="Total", markersize=10)
plt.plot(years,[Data.WaterUseIndustry[t] for t in years],"co-",label="Industrial", markersize=10)
plt.plot(years,[Data.WaterUseAgriculture[t] for t in years],"bo-",label="Agriculture", markersize=10)
plt.plot(years,[Data.WaterUseResidential[t] for t in years],"go-",label="Domestic", markersize=10)
plt.plot(years,[Data.WaterWasteTotal[t] for t in years],"yo-",label="Waste Discharge", markersize=10)
plt.ylim(0,9000)
plt.legend(loc=0)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Years")
plt.ylabel("Water Storage/ 100m m^3")
plt.plot(years,[Data.WaterTotal[t] for t in years],"ko-",label="Total Storage", markersize=10)
plt.plot(years,[Data.WaterSurface[t] for t in years],"co-",label="Surface Storage", markersize=10)
plt.plot(years,[Data.WaterUnderground[t] for t in years],"bo-",label="Underground Storage", markersize=10)
plt.legend(loc=0)
plt.show()
plt.close()


# analysis for GDP & Population
print("r(GDP,Population)="+str(pearsonr([Data.GDP[t] for t in years],[Data.Population[t] for t in years])))

# analysis for Wi
print("r(Wi,Population)="+str(pearsonr([Data.WaterUseIndustry[t] for t in years],[Data.Population[t] for t in years])))
print("r(Wi,GDP)="+str(pearsonr([Data.WaterUseIndustry[t] for t in years],[Data.GDP[t] for t in years])))

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

# analysis for Wa
print("r(Wa,Population)="+str(pearsonr([Data.WaterUseAgriculture[t] for t in years],[Data.Population[t] for t in years])))
print("r(Wa,GDP)="+str(pearsonr([Data.WaterUseAgriculture[t] for t in years],[Data.GDP[t] for t in years])))

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

# analysis for Wr
print("r(Wr,Population)="+str(pearsonr([Data.WaterUseResidential[t] for t in years],[Data.Population[t] for t in years])))
print("r(Wr,GDP)="+str(pearsonr([Data.WaterUseResidential[t] for t in years],[Data.GDP[t] for t in years])))

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
