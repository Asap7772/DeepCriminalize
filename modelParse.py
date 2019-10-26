import numpy as np
with open('text.txt') as f:
    a = np.loadtxt(f)
    print(a)
