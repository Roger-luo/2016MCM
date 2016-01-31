import Data
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

years=range(2004, 2015)

plt.figure()
plt.subplot(2,1,1)
plt.xlabel("Years")
plt.ylabel("Population/ 10k people")
plt.plot(Data.Population.keys(),[Data.Population[t] for t in Data.Population.keys()], "bo-")
plt.subplot(2,1,2)
plt.xlabel("Years")
plt.ylabel("GDP/ 100m CNY")
plt.plot(Data.GDP.keys(),[Data.GDP[t] for t in Data.GDP.keys()], "ro-")
plt.show()
plt.close()

plt.figure()
plt.xlabel("Years")
plt.ylabel("Water Usage & Waste/ 100m m^3")
plt.plot(Data.WaterUseTotal.keys(),[Data.WaterUseTotal[t] for t in Data.WaterUseTotal.keys() ],"ko-",label="Total")
plt.plot(Data.WaterUseIndustry.keys(),[Data.WaterUseIndustry[t] for t in Data.WaterUseIndustry.keys()],"co-",label="Industrial")
plt.plot(Data.WaterUseAgriculture.keys(),[Data.WaterUseAgriculture[t] for t in Data.WaterUseAgriculture.keys()],"bo-",label="Agriculture")
plt.plot(Data.WaterUseResidential.keys(),[Data.WaterUseResidential[t] for t in Data.WaterUseResidential.keys()],"go-",label="Domestic")
plt.plot(Data.WaterWasteTotal.keys(),[Data.WaterWasteTotal[t] for t in Data.WaterWasteTotal.keys()],"yo-",label="Waste Discharge")
plt.ylim(0,9000)
plt.legend(loc=0)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Years")
plt.ylabel("Water Storage/ 100m m^3")
plt.plot(Data.WaterTotal.keys(),[Data.WaterTotal[t] for t in Data.WaterTotal.keys()],"ko-",label="Total Storage")
plt.plot(Data.WaterSurface.keys(),[Data.WaterSurface[t] for t in Data.WaterSurface.keys()],"co-",label="Surface Storage")
plt.plot(Data.WaterUnderground.keys(),[Data.WaterUnderground[t] for t in Data.WaterUnderground.keys()],"bo-",label="Underground Storage")
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
