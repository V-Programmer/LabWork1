import numpy as np
from sklearn. preprocessing import normalize
#create matrix
x = np.arange (0, 100, 4). reshape (5,5)

#view matrix
print(x)
print("")
x_normed = normalize(x, axis= 1 , norm='l1')
print("Normalized by X")
print(x_normed)
print("")
y_normed = normalize(x, axis= 0 , norm='l1')
print("Normalized by Y")
print(y_normed)
print("")

vector = np.linspace(0,1,12,endpoint=True)[1:-1]
print("Vector with 10 values in range from 0 to 1, excluding 0 and 1 values")
print(vector)