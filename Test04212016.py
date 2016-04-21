import numpy as np
import matplotlib.pyplot as plt
#
# # things to talk about 4/21/16
#
# # creating a numpy array (1D,2D)
# # indexing
# # zeros and ones functions to initialize
# # vector/matrix operations (elementwise arithmetic, addition, sum, mean, etc.)
# # loops/lists = bad (speed comparison)
# # loading data/matrix from file
# # plotting, colors, labels, legends
# # http://matplotlib.org/examples/color/named_colors.html
# # subplots, sizing, saving (vector vs. raster)
# # different plot types, scatter
# # https://github.com/VictoriaLynn/plotting-examples
#
# # a list
# L = [6, 5, 4, 3, 6]
#
# # a numpy array
# A =np.array([6,3,7,4,5])
#
# #a 2d array (matrix)
# A2 = np.array([[6,3,4,6,5],[2,9,8,1,4]])
#
# #indexing [i,j]
# # print(A2[0,3])
#
# #get a row (: means "all")
#
# # # create a matrix of zeroes
# M = np.zeros((10,5))
# N = np.ones((4,3))
# print(M)
#
# # # what do you expect to happen?
# print(L+L)

# V = np.ones((1000,5))
# print(V.sum())
# print(V.sum(axis=1))
#
# for i in range(1000000):
#     for j in range(5):
#         s+=V[i,j]
#
#     print (s)

data = np.loadtxt('data/FOL.csv', delimiter=',',skiprows=1,usecols=[1,2,3])
print(data.shape)

storage = data[:,0] #TAF
elevation = data[:,1] #ft
outflow = data[:,2] #mean cfs per day

plt.plot(storage, color='steelblue', linewidth=2)
plt.xlabel('Days')
plt.ylabel('Storage (TAF)')
plt.title('Folsom Reservoir 2008-2015')
plt.show()

plt.savefig('class.pdf')