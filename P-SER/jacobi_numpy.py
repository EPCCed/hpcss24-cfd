# 
# Jacobi routine for CFD calculation
#
import numpy as np

import sys
import math

def jacobi(niter, psi):

    (m, n) = psi.shape
    m = m - 2
    n = n - 2

    bnorm = math.sqrt(np.sum(psi[:][:]*psi[:][:]))

    psitmp = np.zeros((m+2, n+2))

    print("\nStarting main loop...\n");

    for iter in range(1,niter+1):

        # Use index notation and offsets to compute the stream function
        psitmp[1:m+1,1:n+1] = 0.25 * (psi[2:m+2,1:n+1]+psi[0:m,1:n+1]+psi[1:m+1,2:n+2]+psi[1:m+1,0:n])

        if (iter == niter):

            error = np.sum(   (psitmp[1:m+1,1:n+1]-psi[1:m+1,1:n+1])*(psitmp[1:m+1,1:n+1]-psi[1:m+1,1:n+1]) )

            error = math.sqrt(error)
            error = error/bnorm

        # Update psi
        np.copyto(psi[1:m+1,1:n+1], psitmp[1:m+1,1:n+1])
        
        # Debug output
        if iter%1000 == 0:
            print("Completed iteration ", iter)

    print("\n... finished");
    print("After ", niter, " iterations, the error is ", error);
