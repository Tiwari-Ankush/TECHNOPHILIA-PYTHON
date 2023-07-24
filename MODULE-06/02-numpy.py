"""
numpy --> num - py 

"""

import numpy as np

# a = np.array([1,2,3])  # rank1 array 
# print(a)
# print(type(a))
# print(a.shape)
# print(a[0], a[1], a[2])

# b = np.array([[1,2,3],[4,5,6]])  #rank2 array
# ls = [[1,2,3], [4,5,6]]

# print(b)
# print(b.shape)  #2 by 3 matrix
# print(b[1,2])  #2nd row third column

a = np.zeros((100,100))
# print(a) # it gives 100 x 100 matrix
print(a.shape)

a = np.ones((4,2))
print(a)

a = np.full((4,5), 1876)
print(a)

a = np.eye(3)
print(a)

a = np.random.randint(2,100, (2,2)) # from 2 to 100 random number, and 2 by 2 ka matrix

print(a)

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

print(np.add(x,y))
# print(np.multiply(y,x))
# print(np.divide(y,x))


print(np.sqrt(x))

print(x.ndim)
print(x.shape)

print(np.dot(x,y)) #dot product
print(np.cross(x,y))  #cross product

