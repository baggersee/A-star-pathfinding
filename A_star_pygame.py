import pygame
import numpy as np
from A_star_functions import creation,distance,colindant,visualization

# variables for pygame

WIDTH = 650
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

ROWS = 15 

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208) 

# Node class
class Node:
    def __init__(self,position=None,parent=None,width=None):
        
        self.position = position
        self.parent = parent
        #initializing the node's parameters
        self.g = 0
        self.h = 0
        self.f = 0
        
        self.color = WHITE
        self.width = width # anchura de cada nodo--> de cada cuadrado
        
        #posiciones en el tablero
        self.x = position[0]*width # posicion x en el tablero
        self.y = position[1]*width # posicion y en el tablero
    
    def __lt__(self,other):
        return False
     
# A* pathfinding algorithm 
def A_star(space_m,space,start_point,final_point,width):
    
    #initializing the open and closed lists
    open_list = []
    closed_list = []
    
    #creating the initial and final nodes
    initial_node = Node(start_point,None,width)
    initial_node.g = 0
    initial_node.h = 0
    initial_node.f = 0
    
    final_node = Node(final_point,None,width)
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
            
            path = path[::-1]
            return path
      
        #generating the children
        children_positions = colindant(space_m,current_node.position)
   
        #treating the children
        for child_position in children_positions:
            #checking if there is some forbidden position
            if space_m[ child_position[0],child_position[1] ] == 1:
                continue 
            
            #setting the child as a Node
            child_node = Node(child_position,current_node,width)
            
            #checking if it is in the closed list
            for closed_child in closed_list:
                if child_node == closed_child:
                    continue
            
            #computing its parameters
            child_node.g = current_node.g + 1
            child_node.h = distance(child_node.position,final_node.position)
            child_node.f = child_node.g + child_node.h
            
            #checking if it is in the open list
            for open_node in open_list:
                if child_node == open_node and child_node.g > open_node.g:
                    closed_list.append(child_node)
                    continue
                
            #adding it to the open list
            open_list.append(child_node)
            if child_node.position != initial_node.position and child_node.position != final_node.position:
                if space[child_node.position[1]][child_node.position[0]].color != RED:
                    space[child_node.position[1]][child_node.position[0]].color = RED
                    
                else:
                    space[child_node.position[1]][child_node.position[0]].color = BLUE
            
            draw(WIN,space,ROWS,width)
            
# auxilary pygame functions

def make_grid(rows, width):
    # rows = number of rows of the board
    # width = pixel length of the window
	grid = []
	gap = width // rows # division entera-> anchura de cada cuadrado
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			node = Node([i, j], None, gap)
			grid[i].append(node)
    
    # 'grid' is the matrix of the board. In each position it holds a Node (Object)
	return grid



def draw_grid(win, rows, width):
    # function to draw the board--> called in the aux function 'draw'
	gap = width // rows # anchura de cada cuadrado
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        #pygame.draw.line(win, GREY, donde empieza , donde acaba
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))
            
 

def draw(win, grid, rows, width):
	win.fill(WHITE)
	for row in grid:
		for node in row:
			pygame.draw.rect(win, node.color, (node.x, node.y, width, width))
	draw_grid(win, rows, width)
	pygame.display.update()            

def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col



#%% main function
  
def main(win, width):
    
    ROWS = 15
    space = make_grid(ROWS, width)
    space_matrix = np.zeros((ROWS,ROWS),int)
    
    start = None
    end = None
	
    run = True
    while run:
		
        draw(WIN,space,ROWS,width)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row,col = get_clicked_pos(pos,ROWS,width)
                node_selected = space[row][col]
                
                if start == None and node_selected != end:
                    start = node_selected
                    start.color = ORANGE 
                
                elif end == None and node_selected != start:
                    end = node_selected
                    end.color = TURQUOISE
                    
                elif node_selected != start and node_selected != end:
                    node_selected.color = BLACK
                    space_matrix[node_selected.position[1],node_selected.position[0]] = 1
                   
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row,col = get_clicked_pos(pos,ROWS,width)
                node_selected = space[row][col]
                node_selected.color = WHITE
                space_matrix[node_selected.position[1],node_selected.position[0]] = 0
    				
    				
                if node_selected == start:
                    start = None
                    
                elif node_selected == end:
                    end = None
                  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start != None and end != None:
                    
                    start.position = start.position[::-1]
                    end.position = end.position[::-1]
                    pygame.display.set_caption("thinking...")
                    path = A_star(space_matrix,space,start.position,end.position,width)
                    walk = len(path)
                    
                    pygame.display.set_caption("still thinking...")
                    
                    start.color = ORANGE
                    end.color = TURQUOISE
                    
                    for j in range(1,walk-1):
                        step = path[j]
                        space[step[1]][step[0]].color = PURPLE
                        draw(WIN,space,ROWS,width)
                    pygame.display.set_caption("A* Path Finding Algorithm")
    				  
    pygame.quit()
    
main(WIN,WIDTH)
