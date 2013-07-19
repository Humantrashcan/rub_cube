"""
*** Rubik Cube Solver V1 ***

For this first version the programme will solve for each position in order, and not be optimised to skip if another position matches.
The guessing algorithm will run through possible moves till reaching a match, randomly - no optimisation in this version.

"""

# Define cube as a single list - hardcoded for the moment
# A standard 3*3 Rubik cube has 54 squres
""" 

*** Cube layout ***
Laying the cube on the table, top left moving across, then down is 0-8

Use Excel sheet

"""

original_cube=["g","g","o","b","b","g","r","w","y","y","y","w","g","r","b","r","o","w","y","o","r","y","w","w","g","r","g","g","b","o","w","b","y","b","w","w","g","r","o","o","g","b","r","w","r","y","o","b","o","y","r","o","y","b",]
print original_cube

working_cube=list(original_cube)     # blank cube will be used during the working 
prev_cube=list(original_cube)        # blank cube will be used to store the cube from the previous move

# Define possible moves and their impact on the work in progress cube

""" There are 10 possible moves I will only use 8
(the other two are turning the back face, clockwise and anti-clockwise)"""

# Each move defined separately.  A list will call the move to be used

# Move 1 - Left column moved up
def move_1():
    working_cube=[prev_cube[12],prev_cube[1],prev_cube[2],prev_cube[21],prev_cube[4],prev_cube[5],prev_cube[30],prev_cube[7],prev_cube[8],prev_cube[11],prev_cube[20],prev_cube[29],prev_cube[36],prev_cube[13],prev_cube[14],prev_cube[15],prev_cube[16],prev_cube[17],prev_cube[10],prev_cube[19],prev_cube[28],prev_cube[39],prev_cube[22],prev_cube[23],prev_cube[24],prev_cube[25],prev_cube[26],prev_cube[9],prev_cube[18],prev_cube[27],prev_cube[42],prev_cube[31],prev_cube[32],prev_cube[33],prev_cube[34],prev_cube[35],prev_cube[45],prev_cube[37],prev_cube[38],prev_cube[48],prev_cube[40],prev_cube[41],prev_cube[51],prev_cube[43],prev_cube[44],prev_cube[0],prev_cube[46],prev_cube[47],prev_cube[3],prev_cube[49],prev_cube[50],prev_cube[6],prev_cube[52],prev_cube[53]]
    print working_cube

# Move 2 - Left column moved down
def move_2():
    working_cube=[prev_cube[45],prev_cube[1],prev_cube[2],prev_cube[48],prev_cube[4],prev_cube[5],prev_cube[51],prev_cube[7],prev_cube[8],prev_cube[27],prev_cube[18],prev_cube[9],prev_cube[0],prev_cube[13],prev_cube[14],prev_cube[15],prev_cube[16],prev_cube[17],prev_cube[28],prev_cube[19],prev_cube[10],prev_cube[3],prev_cube[22],prev_cube[23],prev_cube[24],prev_cube[25],prev_cube[26],prev_cube[29],prev_cube[20],prev_cube[11],prev_cube[6],prev_cube[31],prev_cube[32],prev_cube[33],prev_cube[34],prev_cube[35],prev_cube[12],prev_cube[37],prev_cube[38],prev_cube[21],prev_cube[40],prev_cube[41],prev_cube[30],prev_cube[43],prev_cube[44],prev_cube[36],prev_cube[46],prev_cube[47],prev_cube[39],prev_cube[49],prev_cube[50],prev_cube[42],prev_cube[52],prev_cube[53]]
    print working_cube

# Move 3 - Move right column up
def move_3():
    working_cube=[prev_cube[0],prev_cube[1],prev_cube[14],prev_cube[3],prev_cube[4],prev_cube[23],prev_cube[6],prev_cube[7],prev_cube[32],prev_cube[9],prev_cube[10],prev_cube[11],prev_cube[12],prev_cube[13],prev_cube[38],prev_cube[33],prev_cube[24],prev_cube[15],prev_cube[18],prev_cube[19],prev_cube[20],prev_cube[21],prev_cube[22],prev_cube[41],prev_cube[34],prev_cube[25],prev_cube[16],prev_cube[27],prev_cube[28],prev_cube[29],prev_cube[30],prev_cube[31],prev_cube[44],prev_cube[35],prev_cube[26],prev_cube[17],prev_cube[36],prev_cube[37],prev_cube[47],prev_cube[39],prev_cube[40],prev_cube[50],prev_cube[42],prev_cube[43],prev_cube[53],prev_cube[45],prev_cube[46],prev_cube[2],prev_cube[48],prev_cube[49],prev_cube[5],prev_cube[51],prev_cube[52],prev_cube[8]]
    print working_cube

# Move 4 - Move right column down
def move_4():
    working_cube=[prev_cube[0],prev_cube[1],prev_cube[47],prev_cube[3],prev_cube[4],prev_cube[50],prev_cube[6],prev_cube[7],prev_cube[53],prev_cube[9],prev_cube[10],prev_cube[11],prev_cube[12],prev_cube[13],prev_cube[2],prev_cube[17],prev_cube[26],prev_cube[35],prev_cube[18],prev_cube[19],prev_cube[20],prev_cube[21],prev_cube[22],prev_cube[5],prev_cube[16],prev_cube[25],prev_cube[34],prev_cube[27],prev_cube[28],prev_cube[29],prev_cube[30],prev_cube[31],prev_cube[8],prev_cube[15],prev_cube[24],prev_cube[33],prev_cube[36],prev_cube[37],prev_cube[14],prev_cube[39],prev_cube[40],prev_cube[23],prev_cube[42],prev_cube[43],prev_cube[32],prev_cube[45],prev_cube[46],prev_cube[38],prev_cube[48],prev_cube[49],prev_cube[41],prev_cube[51],prev_cube[52],prev_cube[44]]
    print working_cube
    
# Move 5 - Move top row left
def move_5():
    working_cube=[prev_cube[6],prev_cube[3],prev_cube[0],prev_cube[7],prev_cube[4],prev_cube[1],prev_cube[8],prev_cube[5],prev_cube[2],prev_cube[12],prev_cube[13],prev_cube[14],prev_cube[15],prev_cube[16],prev_cube[17],prev_cube[53],prev_cube[52],prev_cube[51],prev_cube[18],prev_cube[19],prev_cube[20],prev_cube[21],prev_cube[22],prev_cube[23],prev_cube[24],prev_cube[25],prev_cube[26],prev_cube[27],prev_cube[28],prev_cube[29],prev_cube[30],prev_cube[31],prev_cube[32],prev_cube[33],prev_cube[34],prev_cube[35],prev_cube[36],prev_cube[37],prev_cube[38],prev_cube[39],prev_cube[40],prev_cube[41],prev_cube[42],prev_cube[43],prev_cube[44],prev_cube[45],prev_cube[46],prev_cube[47],prev_cube[48],prev_cube[49],prev_cube[50],prev_cube[9],prev_cube[10],prev_cube[11]]
    print working_cube

# Move 6 - Move top row left
def move_6():
    working_cube=[prev_cube[2],prev_cube[5],prev_cube[8],prev_cube[1],prev_cube[4],prev_cube[7],prev_cube[0],prev_cube[3],prev_cube[6],prev_cube[53],prev_cube[52],prev_cube[51],prev_cube[9],prev_cube[10],prev_cube[11],prev_cube[12],prev_cube[13],prev_cube[14],prev_cube[18],prev_cube[19],prev_cube[20],prev_cube[21],prev_cube[22],prev_cube[23],prev_cube[24],prev_cube[25],prev_cube[26],prev_cube[27],prev_cube[28],prev_cube[29],prev_cube[30],prev_cube[31],prev_cube[32],prev_cube[33],prev_cube[34],prev_cube[35],prev_cube[36],prev_cube[37],prev_cube[38],prev_cube[39],prev_cube[40],prev_cube[41],prev_cube[42],prev_cube[43],prev_cube[44],prev_cube[45],prev_cube[46],prev_cube[47],prev_cube[48],prev_cube[49],prev_cube[50],prev_cube[17],prev_cube[16],prev_cube[15]]
    print working_cube

move_6()