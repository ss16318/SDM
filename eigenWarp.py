## MODELLING

import os
import numpy as np
import matplotlib as plt

from defMatrix import createMatrix
from newTP import newTP
from reconstruct import reconstruct
from display import *
from check import *
from alpha3D import getAlpha3D
from warp import warpGrid
from volume import skullVol


# 1. Create deformation matrix 
defMatrix = createMatrix()   #outputs matrix of deformations


# 2. Perform SVD on matrix

dm = defMatrix.T                                #transposes matrix
average = np.mean(dm,axis=1)                    #finds average of each column
X = dm - np.tile(average,(dm.shape[1],1)).T     #subtracts average to get a zero mean

#performs SVD on zero mean deformation matirx (U are eigenvectors & S eigenvalues)
U , S , VT = np.linalg.svd(X,full_matrices=0)

PC = 2

# create a random parameter vector w/ elements set at 1000
b = np.full((U.shape[1],1),1000)

newTP(average)

averageSkull = reconstruct()


warpedGrid = warpGrid(averageSkull,0)
   
b[PC] = 3*np.sqrt(S[PC])     
 
#multiplies random parameter vector with principal eigenvectors
residualDef = U[:,PC] * b[PC] 

newDef = average + residualDef

newTP(newDef)  #function creates transform paramter file with new control pt deformations

# 4. Artificial skull reconstruction 

artificialSkull1 = reconstruct()   #deforms model image using DFM reconstruction from new pm

print( skullVol(artificialSkull1,500))

warpedGrid = warpGrid(averageSkull,1)

displayGrid(warpedGrid,artificialSkull1," +ve Warping with eigenmode " + str(PC) )


newDef = average - residualDef

newTP(newDef)  #function creates transform paramter file with new control pt deformations

# 4. Artificial skull reconstruction 

artificialSkull2 = reconstruct()   #deforms model image using DFM reconstruction from new pm

print( skullVol(artificialSkull2,500))

warpedGrid = warpGrid(averageSkull,1)

displayGrid(warpedGrid,artificialSkull2," -ve Warping with eigenmode " + str(PC) )

compare(artificialSkull1,artificialSkull2,'Comparison')
    
    
    