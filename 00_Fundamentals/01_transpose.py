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

""" Using PyTorch """
# %% Vector
# create a vector
tv = torch.tensor([ [1, 2, 3, 4] ])
print(tv), print(' ')

# transpose it
print(tv.T), print(' ')
# or np.transpose() alternately

# transpose the transpose!
tvT = tv.T
print(tvT.T)

# %% Matrix
# repeat for a matrix
tM = torch.tensor([ [1, 2, 3, 4],
                [5, 6, 7, 8] ])
print(tM), print(' ')

# transpose it
print(tM.T), print(' ')

# transpose the transpose
tMT = tM.T
print(tMT.T)

# %% Examine data types
print(f'Variable nv is of type {type(nv)}')
print(f'Variable nM is of type {type(nM)}')
print(f'Variable tv is of type {type(tv)}')
print(f'Variable tM is of type {type(tM)}')

# Output:
# Variable nv is of type <class 'numpy.ndarray'>
# Variable nM is of type <class 'numpy.ndarray'>
# Variable tv is of type <class 'torch.Tensor'>
# Variable tM is of type <class 'torch.Tensor'>
