import Data
import matplotlib.pyplot as plt


years=range(2004, 2015)


plt.figure()
plt.subplot(2,1,1)
plt.xlabel("Years")
plt.ylabel("Population/ 10k people")
plt.plot(years,[Data.Population[t] for t in years], "bo-")
plt.subplot(2,1,2)
plt.xlabel("Years")
plt.ylabel("GDP/ 100m CNY")
plt.plot(years,[Data.GDP[t] for t in years], "ro-")
plt.show()
plt.close()

plt.figure()
plt.xlabel("Years")
plt.ylabel("Water Usage & Waste/ 100m m^3")
plt.plot(years,[Data.WaterUseTotal[t] for t in years],"ko-",label="Total")
plt.plot(years,[Data.WaterUseIndustry[t] for t in years],"co-",label="Industrial")
plt.plot(years,[Data.WaterUseAgriculture[t] for t in years],"bo-",label="Agriculture")
plt.plot(years,[Data.WaterUseResidential[t] for t in years],"go-",label="Domestic")
plt.plot(years,[Data.WaterWasteTotal[t] for t in years],"yo-",label="Waste Discharge")
plt.ylim(0,9000)
plt.legend(loc=0)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Years")
plt.ylabel("Water Storage/ 100m m^3")
plt.plot(years,[Data.WaterTotal[t] for t in years],"ko-",label="Total Storage")
plt.plot(years,[Data.WaterSurface[t] for t in years],"co-",label="Surface Storage")
plt.plot(years,[Data.WaterUnderground[t] for t in years],"bo-",label="Underground Storage")
plt.legend(loc=0)
plt.show()
plt.close()
