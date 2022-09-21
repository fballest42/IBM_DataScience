from ast import increment_lineno
import pandas as pd
import numpy as np


# a = np.array([0.5,1.5,2.5,3.5,4.5])
# print(type(a))
# print(a.dtype)
# print(a.size)
# print(a.ndim)
# print(a.shape)
# a[0] = 0
# print(a)
# b = a[1:3]
# print(b)
# #########

# u = np.array([1, 0])
# v = np.array([0, 1])
# z = u + v
# print(z)

# y = np.array([1,2])
# z = 2*y
# print(z)

# u = np.array([2, 3])
# v = np.array([1, 2])
# z = u * v
# print(z)

# u = np.array([2, 3])
# v = np.array([1, 2])
# z = np.dot(u,v)
# print(z)

# u = np.array([0,1,2,3])
# z = u+1
# print(z)

# a = np.array([1,2,3,4])
# z = a.max()
# print(z)

# x = np.array([0,np.pi/2,np.pi])
# y = np.sin(x)
# print(y)

x = np.linspace(0,2*np.pi,100)
y = np.sin(x)
import matplotlib.pyplot as plt  #libreria de python para crear gráficosNme
fig = plt.figure() #genera una variable para almacenar la imagen
plt.plot(x,y)      #genera la imagen con los datos indicados 
fig.savefig('temp.png', dpi=fig.dpi)  #crea un archivo con la figura

######## MODULE 6 VIDEO 2

# a = [[0,1,0,1,0]]
# A = np.array(a)
# print(A.ndim)
# print(A.shape)


# A = np.array([0,1])
# B = np.array([1,0])
# print(np.dot(A,B))

# a=np.array([1,1,1,1,1])
# print(a+10)
