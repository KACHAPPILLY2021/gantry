import sympy as sp
from sympy import *
import math as mt

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import math
## define the function to find the transformation matrix
def tran(a,alpha,d,theta):

    ## rot@z*trans@z*trans@x*rot@z
    A = sp.Matrix([[sp.cos(theta), -sp.sin(theta), 0, 0 ], [sp.sin(theta), sp.cos(theta), 0, 0 ], [0 , 0, 1, 0], [0, 0, 0, 1]])@sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d],[0, 0, 0, 1]])@sp.Matrix([[1, 0, 0, a],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])@sp.Matrix([[1, 0, 0, 0], [0, sp.cos(alpha), -sp.sin(alpha), 0], [0, sp.sin(alpha), sp.cos(alpha), 0],[ 0, 0, 0, 1]])
    return A

##define the final transformation matrix

def finalTransformation(t1, t2, t3, t4, t5, t6):
    
    ##transformation of frame 1 to 6 by passing DH parameter to tran function
    
    A1 = tran(0,-sp.pi/2,26,t1)
    A2 = tran(102.52,0,29,-sp.pi/2-t2)
    A3 = tran(0,sp.pi/2,-17.5,sp.pi/2+t3)
    A4 = tran(0,sp.pi/2,142.49,sp.pi/2+t4)
    A5 = tran(0,-sp.pi/2,0,t5)
    A6 = tran(0,0,0,t6)
    A = A1@A2@A3@A4@A5@A6
    return A

x = []
y = []
z = []
P0=sp.Matrix([[0] , [0] , [0] , [1]])
# The maximum reachable workspace is obtained by providing angle limits of joint 1 and joint 2 of manipulator 
for i in range(-18,19):

    for j in range(-9,10):

        T07=finalTransformation(((sp.pi*2)/18)*i , ((sp.pi*2)/36)*j, 0,0,0,0)
            
        P7=T07@P0
        x.append(-P7[0])
        y.append(-P7[1])
        z.append(-P7[2])

    
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x,y,z,"o",markersize=2,color="red" )

plt.show()



    
    
    
