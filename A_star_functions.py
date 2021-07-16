

def distance(R1,R2):
    # function that computes the heuristic distance
    x1 = R1[0]
    y1 = R1[1]
    x2 = R2[0]
    y2 = R2[1]
    dist = (x2-x1)**2 + (y2-y1)**2
    return dist


def colindant(M,R):
    # function that gets the position coordinates of the adjacent points of a given point
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
