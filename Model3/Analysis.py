import Data
import matplotlib.pyplot as plt
<<<<<<< HEAD

years=range(2004, 2015)

=======
import numpy as np
<<<<<<< HEAD

=======
"""
>>>>>>> cdc868660893b75318d1a9b30573ae1fb68a7f84
>>>>>>> 9a2c0111afdb65356d5b4f8ed5b61a9d84825564
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
"""
for key in Population:
    print(key,Population[key])

plt.figure()
plt.plot([key for key in Population],[Population[key] for key in Population],"*")
plt.show()
plt.close()
"""
