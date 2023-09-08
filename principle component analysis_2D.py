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

def main():
    print(myDataset)
    center=(mean(myDataSetX),mean(myDataSetY))
    datacpy=[(myDataSetX[k]-center[0],myDataSetY[k]-center[1]) for k in range(DATASIZE)]

    #Calculating the value of m
    polya=sum(datacpy[k][0]*datacpy[k][1] for k in range(DATASIZE))
    polyb=sum(datacpy[k][0]**2-datacpy[k][1]**2 for k in range(DATASIZE))
    polyc=-polya
    m=(-polyb+math.sqrt(polyb**2-4*polya*polyc))/(2*polya)
    print(m)
    sumofsquaresdistances=lambda m00:sum((datacpy[k][1]-m00*datacpy[k][0])**2/(1+m00**2) for k in range(DATASIZE))
    singularValue=math.sqrt(sumofsquaresdistances(m))
    




def mean(list0):
    return sum(list0)/len(list0)


main()

