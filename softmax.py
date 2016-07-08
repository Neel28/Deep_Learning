"""Softmax."""

#scores = [[3.0, 1.0, 0.2],[3.0,1.0,0.2]]
import numpy as np
from math import exp

scores = np.array([[1.0,2.0,3.0,6.0],
                   [2.0,4.0,5.0,6.0],
                   [3.0,8.0,7.0,6.0]])

"""compute softmax for each sets of scores in x"""
def softmax(x):
	e_x = np.exp(x)
	return e_x / np.sum(e_x,axis=0)

"""
softmax(scores)
print(softmax(scores/10))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)

scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
"""

a = 1000000000 
for i in xrange(1000000):
	a = a + 1e-6
print a - 1000000000


