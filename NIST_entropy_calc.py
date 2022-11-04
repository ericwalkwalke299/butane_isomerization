import numpy as np
def NIST_entropy_calc(T = 673.15, A = 0.0, B = 0.0, C = 0.0, D = 0.0, E = 0.0, F = 0.0, G = 0.0): # If A-G are not supplied, this function will return zero entropy correction.
    t = T/1000
    entropy_J_per_mol_K = A*np.log(t) + B*t + C*np.power(t,2)/2 + D*np.power(t,3)/3 - E/(2*np.power(t,2)) + G
    entropy_eV_per_K = entropy_J_per_mol_K / (1000*96.485)
    entropy_correction = entropy_eV_per_K * T
    return entropy_correction

