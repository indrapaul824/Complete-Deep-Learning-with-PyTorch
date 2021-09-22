#%% Import Libraries

import numpy as np
import torch

""" Using numpy """
# %% Vector
# create a vector
nv = np.array([ [1, 2, 3, 4] ])
print(nv), print(' ')

# transpose it
print(nv.T), print(' ')
# or np.transpose() alternately

# transpose the transpose!
nvT = nv.T
print(nvT.T)

# %% Matrix
# repeat for a matrix
nM = np.array([ [1, 2, 3, 4],
                [5, 6, 7, 8] ])
print(nM), print(' ')

# transpose it
print(nM.T), print(' ')

# transpose the transpose
nMT = nM.T
print(nMT.T)

# %%
