import numpy as np


def creation(M):
    
    dim = np.shape(M)
    rows = dim[0]
    cols = dim[1]
    
    file = open("space.txt","w")
    for i in range(rows):
        for j in range(cols):
            file. write(str(M[i,j])+' ')
        file.write('\n')
    file. close()
    
    return 0



def visualization(M,P):
    for element in P:
        M[element[0],element[1]] = 2
        
    creation(M)
    return 0


#M = np.zeros([7,7],int)
#creation(M)


#%%

def distance(R1,R2):
    #le doy dos puntos y me saca su distancia (al cuadrado)
    x1 = R1[0]
    y1 = R1[1]
    x2 = R2[0]
    y2 = R2[1]
    dist = (x2-x1)**2 + (y2-y1)**2
    return dist



def colindant(M,R):
    #le doy un punto y una matriz, y me saca los puntos adyacentes
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
        
    

    

#%%
class Node:
    def __init__(self,position=None,parent=None):
        self.position = position
        self.parent = parent
        #initializing the node's parameters
        self.g = 0
        self.h = 0
        self.f = 0
    
    #ESTO NO TENGO CLARO QUÉ HACE, ASI QUE LO PONGO POR ACTO DE FE
    #hypothesis--> enables the position change?
    def __eq__(self, other):
        return self.position == other.position


def A_star(space,start_point,final_point):
    #initializing the open and closed lists
    open_list = []
    closed_list = []
    
    
    #creating the initial and final nodes
    initial_node = Node(start_point,None)
    initial_node.g = 0
    initial_node.h = 0
    initial_node.f = 0
    
    final_node = Node(final_point,None)
    final_node.g = 0
    final_node.h = 0
    final_node.f = 0
    
    
    #adding the initial node to the open list
    open_list.append(initial_node)
    
    
    #the process begins
    while len(open_list) !=0:
        
        
        
        #defining the current node->the one with least f
        current_node = open_list[0]
        for item in open_list:
            if item.f < current_node.f:
                current_node = item
                
        #print(current_node.position)
        
        
        #removing the current node from the open list and adding it to the closed list
        open_list.remove(current_node)
        closed_list.append(current_node)
        
        
        #checking if it already made it
        if current_node.position == final_node.position:
            #tracing the path
            path = []
            step = current_node
            while step is not None:
                path.append(step.position)
                step = step.parent
                
            return path
        
        
        #generating the children
        children_positions = colindant(space,current_node.position)
        
        #print(children_positions)
        #saca correctamente todos los colindantes
        
        
        
        #treating the children
        for child_position in children_positions:
            
            #checking if there is some forbidden position
            if space[ child_position[0],child_position[1] ] == 1:
                #children_positions.remove(child_position)
                continue
            
            #instauring the child as a Node
            child_node = Node(child_position,current_node)
            
            #checking if it is in the closed list
            if child_node in closed_list:
                continue
            
            #computing its parameters
            child_node.g = current_node.g + 1
            child_node.h = distance(child_node.position,final_node.position)
            child_node.f = child_node.g + child_node.h
            
            #checking if it is in the open list
            for open_node in open_list:
                if child_node == open_node and child_node.g > open_node.g:
                    continue
                
            
            #adding it to the open list
            open_list.append(child_node)
            #print(child.position)
        #print("so far so good")
            
            
        
    
    
#%%
maze = [[0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

space = np.array(maze)
        
start = [7, 3]
endd = [2, 8]

#space= np.zeros([64,64],int)

path = A_star(space,start,endd)

#creation(space)

visualization(space,path)
#FUNCIONA!!!


    
    
    
    
    