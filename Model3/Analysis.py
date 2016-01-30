from Data import *
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.subplot(3,1,1)
plt.plot(range(2004,2015),[Population[year] for year in range(2004,2015)], "b-")
plt.subplot(3,1,2)
plt.plot(range(2004,2015),[WaterTotal[year] for year in range(2004,2015)], "r-")
plt.subplot(3,1,3)
plt.plot(range(2004,2015),[GDP[year] for year in range(2004,2015)], "g-")
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