from cProfile import label
from math import sqrt
from statistics import NormalDist
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
from scipy.stats import norm
from matplotlib import animation
from matplotlib.animation import PillowWriter

# def confidence_interval(data, confidence=0.99):
#   dist = NormalDist.from_samples(data)
#   z = NormalDist().inv_cdf((1 + confidence) / 2.)
#   h = dist.stdev * z / ((len(data) - 1) ** .5)
#   return dist.mean - h, dist.mean + h

# values = np.array([])
# figure, ax = plt.subplots()
# samples = 1000

# def animation_function(i):
#     global values
#     if i < 10:
#         values = np.append(values, np.random.normal(171, 7, 1))
#     elif i < 20:
#         values = np.append(values, np.random.normal(171, 7, 10))
#     else:
#         values = np.append(values, np.random.normal(171, 7, 100))
        
#     plt.hist(values, bins=range(140, 210), color='b')


# plt.xlabel("Height in cms")
# plt.ylabel("Number of people")
# plt.title("People's height")

# animation = animation.FuncAnimation(figure, func=animation_function, interval=500, frames=100)
# animation.save("TLI.gif", dpi=300, writer=PillowWriter(fps=25))


values = np.random.normal(2200, 300, 100000)
values = np.append(values, [10_000_000])
ci = norm(*norm.fit(values)).interval(0.95)
height, bins, patches = plt.hist(values, bins=list(range(1300, 3200)), alpha=0.3)
plt.fill_betweenx([0, height.max()], ci[0], ci[1], color='r', alpha=0.1, label="95% confidence interval")
plt.legend()
# plt.hist(values, bins=(list(range(1400, 3000))))
plt.xlabel("Monthly salary")
plt.ylabel("Number of people")
plt.title("People's salary")
plt.show()