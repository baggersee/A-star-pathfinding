#function that creates the free space
def blank_space(x):
    
    blank = []
    for i in range(x):
        blank.append([])
        for j in range(x):
            blank[i].append(0)
    
    return blank

#function that reads a list of lists and creates a .txt 
def creation(M):
    
    #dim = np.shape(M)
    dim = len(M)
    #rows = dim[0]
    #cols = dim[1]
    
    file = open("space.txt","w")
    for i in range(dim):
        for j in range(dim):
            file. write(str(M[i][j])+' ')
        file.write('\n')
    file. close()
    
    return 0


#function that reads the modified .txt file
def constraints_setup():
    space = []
    with open("space.txt") as fname:
        for lines in fname:
            space.append(lines.split())
    
    return space
import numpy as np


#function that computes the heuristic distance
def distance(R1,R2):
    x1 = R1[0]
    y1 = R1[1]
    x2 = R2[0]
    y2 = R2[1]
    dist = (x2-x1)**2 + (y2-y1)**2
    return dist


#function that gets the position coordinates of the adjacent points of a given point
"""
def colindant(M,R):
    #le doy un punto y una matriz, y me saca los puntos adyacentes
    M = np.array(M)
    dim = np.shape(M)
    x = R[0]
    y = R[1]
    if R[0] == 0:
        if R[1] == 0:
            P3 = [x,y+1]
            P4 =[x+1,y+1]
            P5 = [x+1,y]
            P = [P3,P4,P5]
        elif R[1] == dim[1] -1:
            P5 = [x+1,y]
            P6 = [x+1,y-1]
            P7 = [x,y-1]
            P = [P5,P6,P7]
        else:
            P3 = [x,y+1]
            P4 =[x+1,y+1]
            P5 = [x+1,y]
            P6 = [x+1,y-1]
            P7 = [x,y-1]
            P = [P3,P4,P5,P6,P7]
    elif R[0] == dim[0] -1:
            if R[1] == 0:
                P1 = [x-1,y]
                P2 = [x-1,y+1]
                P3 = [x,y+1]
                P = [P1,P2,P3]
            elif R[1] == dim[1] -1:
                P1 = [x-1,y]
                P7 = [x,y-1]
                P8 = [x-1,y-1]
                P = [P1,P7,P8]
            else:
                P1 = [x-1,y]
                P2 = [x-1,y+1]
                P3 = [x,y+1]
                P7 = [x,y-1]
                P8 = [x-1,y-1]
                P = [P1,P2,P3,P7,P8]
    elif R[1] == 0:
        if R[0] == 0:
            P3 = [x,y+1]
            P4 =[x+1,y+1]
            P5 = [x+1,y]
            P = [P3,P4,P5]
        elif R[0]== dim[0] -1:
            P1 = [x-1,y]
            P2 = [x-1,y+1]
            P3 = [x,y+1]
            P = [P1,P2,P3]
        else:
            P1 = [x-1,y]
            P2 = [x-1,y+1]
            P3 = [x,y+1]
            P4 =[x+1,y+1]
            P5 = [x+1,y]
            P = [P1,P2,P3,P4,P5]
    elif R[1] == dim[1] -1:
        if R[0] == 0:
            P5 = [x+1,y]
            P6 = [x+1,y-1]
            P7 = [x,y-1]
            P = [P5,P6,P7]
        elif R[0] == dim[0] -1:
            P1 = [x-1,y]
            P7 = [x,y-1]
            P8 = [x-1,y-1]
            P = [P1,P7,P8]
        else:
            P1 = [x-1,y]
            P5 = [x+1,y]
            P6 = [x+1,y-1]
            P7 = [x,y-1]
            P8 = [x-1,y-1]
            P = [P1,P5,P6,P7,P8]
    else:
        P1 = [x-1,y]
        P2 = [x-1,y+1]
        P3 = [x,y+1]
        P4 =[x+1,y+1]
        P5 = [x+1,y]
        P6 = [x+1,y-1]
        P7 = [x,y-1]
        P8 = [x-1,y-1]
        P = [P1,P2,P3,P4,P5,P6,P7,P8]
        
    return P
"""

def colindant(M,R):
    # M is the matrix (list of lists) with the points
    # P is a list with the coordinates of a point in M
    P = []
    dim = len(M)
    x = R[0]
    y = R[1]
    for i in range(-1,2):
        for j in range(-1,2):
            if x+i == dim or y+j == dim or x+i<0 or y+j<0:
                continue
            P.append([x+i,y+j])
    
    
    P.remove([x,y])
    return P


#function that incorporates the path into the space
def visualization(M,P):
    for element in P:
        M[element[0],element[1]] = 2
        
    creation(M)
    return 0