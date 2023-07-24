"""
matplotlib --> mat plot lib

"""

import numpy as np
import matplotlib.pyplot as plt


# a = np.ones((4,2))
# print(a)

# x = np.arange(0, 3*np.pi,0.1)
# y = np.sin(x)
# # y = np.cos(x)
# plt.plot(x,y)
# # plt.plot(a)
# plt.show()

x = np.arange(0, 3*np.pi,0.01)
y_sin= np.sin(x)
y_cos = np.cos(x)

plt.plot(x,y_sin)
plt.plot(x,y_cos)

plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine Graph by TIWARIBRO')
plt.legend(['sin','cos'])


plt.show()

