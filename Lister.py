listA = []
for i in range(15):
    listA.append(i+1)
    listA.append("i")

print(listA)

# From here I can start working with numpy

import numpy as np

a = 10
arrayA = np.array([1,2,3])
arrayB = np.array([4,5,6])

arrayC = np.multiply(arrayA, arrayB)

print(arrayC)




