print("https://youtu.be/FgakZw6K1QQ")
import math

myDataSetX=[
    -1.38,
    -0.86,
    0.04,
    3.05,
    2.22,
    1.87,
    -0.04
]
myDataSetY=[
    0.8,
    -0.44,
    0.89,
    3.72,
    4.34,
    2.99,
    1.88
]
DATASIZE=len(myDataSetX)

myDataset=[(myDataSetX[k],myDataSetY[k]) for k in range(DATASIZE)]
DIMENSION=len(myDataset[0])

def main():
    print(myDataset)
    center=(mean(myDataSetX),mean(myDataSetY))
    datacpy=[(myDataSetX[k]-center[0],myDataSetY[k]-center[1]) for k in range(DATASIZE)]

    #Calculating the value of m using gradient descent minimizing distance between points and lines
    VecIterate=tuple(1/math.sqrt(DIMENSION) for k in range(DIMENSION))
    lamb=0.001
    for iterations in range(10000):
        gradTotalConsideringAllPoints=list(proj(VecIterate,k) for k in datacpy)
        VecNew=tuple(sum(gradTotalConsideringAllPoints[k]*datacpy[k][j] for k in range(DATASIZE)) for j in range(DIMENSION))
        magVecNew=magnitude(VecNew)
        VecIterate=tuple(k/magVecNew for k in VecNew)
    
    print(VecIterate)


    
    




def mean(list0):
    return sum(list0)/len(list0)

def magnitude(Vec):
    return math.sqrt(sum(k**2 for k in Vec))

def dotProd(Vec1,Vec2):
    return sum(Vec1[k]*Vec2[k] for k in range(len(Vec1)))

def proj(Vec,Point):
    mag=magnitude(Vec)
    vnorm = tuple(k/mag for k in Vec)
    return dotProd(vnorm,Point)




main()

