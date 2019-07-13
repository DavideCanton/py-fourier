import matplotlib.pyplot as plt
import numpy as np

lines = open("out.txt").readlines()
yy = []
xx = []
for line in lines:
    x, y = map(lambda x: float(x.strip().strip('[]')), line.strip().split(','))
    xx.append(x)
    yy.append(y)

plt.plot(xx)
plt.plot(yy)
plt.show()
