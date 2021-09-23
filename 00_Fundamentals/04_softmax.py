#%% Import Libraries

import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

""" Using numpy """
#%% Manual computation
# the list of numbers
z = [1, 2, 3]

# compute the softmax result
num = np.exp(z)
den = np.sum( np.exp(z) )
sigma = num / den

print(sigma)

# Output:
# [0.09003057 0.24472847 0.66524096]

#%% Repeat with some random integers and Plot data
z = np.random.randint(-5, high=15, size=50)
print(z)

# compute softmax result
num = np.exp(z)
den = np.sum( np.exp(z) )
sigma = num / den
print(sigma)

# compare
plt.plot(z, sigma, 'ko')
plt.xlabel('Original number (z)')
plt.ylabel('Softmaxified $\sigma$')
# plt.yscale('log')
plt.title('$\sum\sigma$ = %g' %np.sum(sigma))
plt.show()
plt.savefig("plots/Softmax.jpg")


""" Using PyTorch """
# %% create a vector
tv1 = torch.tensor([1,2,3,4])
tv2 = torch.tensor([0,1,0,-1])

# dot product via function
print(torch.dot(tv1, tv2))

# dot product via computation
print(torch.sum( tv1*tv2 ))

# Output:
# tensor(-2)
# tensor(-2)