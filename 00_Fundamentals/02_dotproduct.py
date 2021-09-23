#%% Import Libraries

import numpy as np
import torch

""" Using numpy """
#%% create a vector
nv1 = np.array([1,2,3,4])
nv2 = np.array([0,1,0,-1])

# dot product via function
print(np.dot(nv1, nv2))

# dot product via computation
print(np.sum( nv1*nv2 ))


""" Using PyTorch """
# %% create a vector
tv1 = torch.tensor([1,2,3,4])
tv2 = torch.tensor([0,1,0,-1])

# dot product via function
print(torch.dot(tv1, tv2))

# dot product via computation
print(torch.sum( tv1*tv2 ))
