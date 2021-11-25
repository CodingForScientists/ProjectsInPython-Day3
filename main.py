import numpy as np
import matplotlib.pyplot as plt


data = np.random.randn(300) * 10 + 5
plt.hist(data, bins=15)
plt.show()
