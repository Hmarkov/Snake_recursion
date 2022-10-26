# 4x4 grid (snake length 16) has 552 paths.

# 5x5 grid (snake length 25) has 8648 paths.

# The program below uses recursion to get the total ways the snake can be laid out on a grid. 
# To get the result for other grid sizes, simply change the value of the n variable and run the code.
#  Some explanations are written as comments. The code is shown below.



def find_paths(grid, path):
    """ The functions takes the size of the grid and the path taken by the snake as parameter.
    Grid is an integer, while Path is a list of tuples, where a tuple (i,j) denotes a position in the grid.
    For instance, in a 2x2 grid, the path could be [(0,0),(0,1),(1,1),(1,0)]. """
    
    # A variable which counts the number of ways the snake can be laid in the grid
    no_paths = 0   
    
    # If the length of the path is equal to the length of the snake (grid^2),
    # then the code returns 1, denoting that the snake has fully been laid in the grid.
    if len(path) == grid ** 2:
        return 1
    
    # Move UP from the current position (note that path[-1] denotes the current position) -
    # if the new position is not outside the grid and not already in the path
    # If the condition is satisfied, then the function is called again with 
    # grid as the size, and the current path with the new position appended to it.
    # This is the same for the other three if-statements below.
    if path[-1][0] - 1 >= 0 and not (path[-1][0] - 1, path[-1][1]) in path: 
        no_paths += find_paths(grid, path + [(path[-1][0] - 1, path[-1][1])])
    
    # Move LEFT from the current position -
    # if the new position is not outside the grid and not already in the path
    if path[-1][1] - 1 >= 0 and not (path[-1][0], path[-1][1] - 1) in path:
        no_paths += find_paths(grid, path + [(path[-1][0], path[-1][1] - 1)])


    # Move DOWN from the current position -
    # if the new position is not outside the grid and not already in the path    
    if path[-1][0] + 1 < grid and not (path[-1][0] + 1, path[-1][1]) in path:
        no_paths += find_paths(grid, path + [(path[-1][0] + 1, path[-1][1])])

    # Move RIGHT from the current position -
    # if the new position is not outside the grid and not already in the path
    if path[-1][1] + 1 < grid and not (path[-1][0], path[-1][1] + 1) in path:
        no_paths += find_paths(grid, path + [(path[-1][0], path[-1][1] + 1)])
        
    # return the total number of paths
    return no_paths

n = 4
no_paths = 0

# This basically loops through all the possible starting points (i,j) in a nxn grid
# The results from each of the starting points are added into a variable, no_paths
for i in range(n):
    for j in range(n):
        no_paths += find_paths(n, [(i,j)])
        
# The final result is then printed out
print(no_paths)