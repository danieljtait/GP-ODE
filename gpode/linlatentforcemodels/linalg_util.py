import numpy as np


##
# Carries out the matrix inversion
#
#       res = C^{-1} x
#
# using the cholesky factor L of C
def _back_sub(L, x):
    return np.linalg.solve(L.T, np.linalg.solve(L, x))


def cholesky(M):
    try:
        return np.linalg.cholesky(M)
    except:
        # Modify to use a jittering routine
        return np.linalg.cholesky(M)
