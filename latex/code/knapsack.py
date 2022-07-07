import numpy as np

C = 11
sizes = [1, 2, 5, 6, 7]
values = [1, 6, 18, 22, 28]
n = len(sizes)
V = np.zeros((n+1, C+1))
for i in range(1, n+1):
    for j in range(1, C+1):
        V[i, j] = V[i-1, j]
        if sizes[i-1] <= j:
            V[i, j] = max(V[i, j], V[i-1, j-sizes[i-1]]+values[i-1])
