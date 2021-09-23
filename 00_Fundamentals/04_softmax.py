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
# -2
# -2

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