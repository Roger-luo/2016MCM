import Data
import matplotlib.pyplot as plt

years=range(2004, 2015)

plt.figure()
plt.subplot(2,1,1)
plt.xlabel("Years")
plt.ylabel("Population/ 10k people")
plt.plot(years,[Data.Population[t] for t in years], "b-")
plt.subplot(2,1,2)
plt.xlabel("Years")
plt.ylabel("GDP/ 100m CNY")
plt.plot(years,[Data.GDP[t] for t in years], "r-")
plt.show()
plt.close()
