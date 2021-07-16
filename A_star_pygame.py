import pygame
import numpy as np
from A_star_functions import colindant, distance

# VARIABLES

# pygame parameters
WIDTH = 650 # size of the pygame window
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")
ROWS = 15 # number of rows and columns of the board

# colors RGB codes
RED = (255, 0, 0) # for Nodes in the open list
WHITE = (255, 255, 255) # for empty Nodes
BLACK = (0, 0, 0) # for obstacles Nodes
ORANGE = (255, 165 ,0) # for the initial point
TURQUOISE = (64, 224, 208) # for the final point
PURPLE = (128, 0, 128) # for the path 
GREY = (128, 128, 128) # for the lines that draw the different squares of the board


# NODE CLASS

class Node:
    def __init__(self,position=None,parent=None,width=None):
        self.position = position # given as a list
        self.parent = parent # given as another Node
        #initializing the node's parameters:
        self.g = 0
        self.h = 0
        self.f = 0
        
        self.color = WHITE
        self.width = width # width of every square in the Pygame interface
        
        #positions of a Node on the board:
        self.x = position[0]*width # x position
        self.y = position[1]*width # y position
    
    def __lt__(self,other):
        return False
    
         
# A* ALGORITHM

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
    
    # adding the initial node to the open list
    open_list.append(initial_node)
    
    # the searching process begins
    while len(open_list) !=0:
        
        # this loop enable us to close the Pygame window at any moment during the process
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:        
                pygame.quit()
                
        # changing the color of the Nodes that are included in the open list
        for open_node in open_list:
            if space[open_node.position[1]][open_node.position[0]].color == WHITE:
                space[open_node.position[1]][open_node.position[0]].color = RED
    
        draw(WIN,space,ROWS,width) 
            
        # searching the current node as the one with smallest 'F'
        current_node = open_list[0]
        for item in open_list:
            if item.f < current_node.f:
                current_node = item
            
        # removing the current node from the open list and adding it to the closed list
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
            
            # checking if it is in the closed list
            closed = 0
            for closed_node in closed_list:
                if child_position == closed_node.position:
                    closed = 1
            if closed == 1:
                continue
                    
            # setting the child as a Node
            child_node = Node(child_position,current_node,width)
            
            # computing its parameters
            child_node.g = current_node.g + 1
            child_node.h = distance(child_node.position,final_node.position)
            child_node.f = child_node.g + child_node.h
            open_list.append(child_node)
             
            #checking if it is in the open list
            param = 0
            for open_node in open_list:
                if child_node.position == open_node.position and child_node.g < open_node.g:
                    open_list.remove(open_node)
                    closed_list.append(child_node)
                    param = 1
                    
            if param == 1:
                continue
            
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:        
            pygame.quit()
    

# AUXILAR FUNCTIONS

def make_grid(rows, width):
    # function to build the matrix that enable to construct the board later
    # rows = number of rows of the board
    # width = pixel length of the window
	grid = []
	gap = width // rows # i teger division-> width of every square on the board
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			node = Node([i, j], None, gap)
			grid[i].append(node)
    
    # 'grid' is the matrix of the board. In each position it holds a Node object
	return grid


def draw_grid(win, rows, width):
    # function to draw the empty board--> called in the aux function 'draw'
	gap = width // rows # width of the squares (same as in 'make_grid' function)
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))
            

def draw(win, grid, rows, width):
    # function that draws the board with the Nodes during all the game
	win.fill(WHITE)
	for row in grid:
		for node in row:
			pygame.draw.rect(win, node.color, (node.x, node.y, width, width))
	draw_grid(win, rows, width)
	pygame.display.update()            

	
def get_clicked_pos(pos, rows, width):
    # function that saves the (matrix) position when a certain square is clicked 
	gap = width // rows
	y, x = pos
	row = y // gap
	col = x // gap
	return row, col


# MAIN FUNCTION
  
def main(win, width,ROWS):
    # building the grid matrix with the Nodes
    space = make_grid(ROWS, width)
    # another matrix just to hold the infrmation of free and obstacles positions
    space_matrix = np.zeros((ROWS,ROWS),int)
    
    start = None
    end = None
	
    run = True
    while run:
        
        draw(WIN,space,ROWS,width)
        for event in pygame.event.get():
            
            # quiting and closing the game
            if event.type == pygame.QUIT:
                run = False
            
            # detecting a click with the left side of the mouse
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row,col = get_clicked_pos(pos,ROWS,width)
                node_selected = space[row][col]
                
                # setting up the initial point/Node
                if start == None and node_selected != end:
                    start = node_selected
                    start.color = ORANGE
                    
                # setting up the final point/Node
                elif end == None and node_selected != start:
                    end = node_selected
                    end.color = TURQUOISE
                
                # setting up obstacles
                elif node_selected != start and node_selected != end:
                    node_selected.color = BLACK
                    space_matrix[node_selected.position[1],node_selected.position[0]] = 1
                    
            # detecting a click with the right side of the mouse
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
            
            # detecting KEYDOWN to start running the A* algorithm
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start != None and end != None:
                    start.position = start.position[::-1]
                    end.position = end.position[::-1]
                    pygame.display.set_caption("thinking...")
                    
                    # calling the A* algorithm to get the path
                    path = A_star(space_matrix,space,start.position,end.position,width)
                    walk = len(path)
                    pygame.display.set_caption("still thinking...")
                    
                    for j in range(1,walk-1):
                        step = path[j]
                        space[step[1]][step[0]].color = PURPLE
                        draw(WIN,space,ROWS,width)
                        
                    pygame.display.set_caption("A* Path Finding Algorithm")
    				   
    pygame.quit()
    
# RUNNING THE GAME
main(WIN,WIDTH,ROWS)
