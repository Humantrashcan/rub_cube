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
print "Original cube:"
print original_cube

working_cube=list(original_cube)     # blank cube will be used during the working 
print "Working cube at the beginning"
print working_cube

prev_cube=list(original_cube)        # blank cube will be used to store the cube from the previous move
print "Previous cube at the beginning"
print prev_cube

# Keep a list of the moves
list_moves=[]

# Define possible moves and their impact on the work in progress cube

""" There are a large number of possible moves I will only use 8"""

# Each move defined separately.  A list will call the move to be used

# Move 1 - Left column moved up
def move_1():
    working_cube=[prev_cube[12],prev_cube[1],prev_cube[2],prev_cube[21],prev_cube[4],prev_cube[5],prev_cube[30],prev_cube[7],prev_cube[8],prev_cube[11],prev_cube[20],prev_cube[29],prev_cube[36],prev_cube[13],prev_cube[14],prev_cube[15],prev_cube[16],prev_cube[17],prev_cube[10],prev_cube[19],prev_cube[28],prev_cube[39],prev_cube[22],prev_cube[23],prev_cube[24],prev_cube[25],prev_cube[26],prev_cube[9],prev_cube[18],prev_cube[27],prev_cube[42],prev_cube[31],prev_cube[32],prev_cube[33],prev_cube[34],prev_cube[35],prev_cube[45],prev_cube[37],prev_cube[38],prev_cube[48],prev_cube[40],prev_cube[41],prev_cube[51],prev_cube[43],prev_cube[44],prev_cube[0],prev_cube[46],prev_cube[47],prev_cube[3],prev_cube[49],prev_cube[50],prev_cube[6],prev_cube[52],prev_cube[53]]
    print "Working cube after some work"
    print working_cube
    print "Previous cube after some work"
    print prev_cube
    return working_cube
    return prev_cube

# Move 2 - Left column moved down
def move_2():
    working_cube=[prev_cube[45],prev_cube[1],prev_cube[2],prev_cube[48],prev_cube[4],prev_cube[5],prev_cube[51],prev_cube[7],prev_cube[8],prev_cube[27],prev_cube[18],prev_cube[9],prev_cube[0],prev_cube[13],prev_cube[14],prev_cube[15],prev_cube[16],prev_cube[17],prev_cube[28],prev_cube[19],prev_cube[10],prev_cube[3],prev_cube[22],prev_cube[23],prev_cube[24],prev_cube[25],prev_cube[26],prev_cube[29],prev_cube[20],prev_cube[11],prev_cube[6],prev_cube[31],prev_cube[32],prev_cube[33],prev_cube[34],prev_cube[35],prev_cube[12],prev_cube[37],prev_cube[38],prev_cube[21],prev_cube[40],prev_cube[41],prev_cube[30],prev_cube[43],prev_cube[44],prev_cube[36],prev_cube[46],prev_cube[47],prev_cube[39],prev_cube[49],prev_cube[50],prev_cube[42],prev_cube[52],prev_cube[53]]
    print "Working cube after some work"
    print working_cube
    print "Previous cube after some work"
    print prev_cube
    return working_cube
    return prev_cube

# Move 3 - Move right column up
def move_3():
    working_cube=[prev_cube[0],prev_cube[1],prev_cube[14],prev_cube[3],prev_cube[4],prev_cube[23],prev_cube[6],prev_cube[7],prev_cube[32],prev_cube[9],prev_cube[10],prev_cube[11],prev_cube[12],prev_cube[13],prev_cube[38],prev_cube[33],prev_cube[24],prev_cube[15],prev_cube[18],prev_cube[19],prev_cube[20],prev_cube[21],prev_cube[22],prev_cube[41],prev_cube[34],prev_cube[25],prev_cube[16],prev_cube[27],prev_cube[28],prev_cube[29],prev_cube[30],prev_cube[31],prev_cube[44],prev_cube[35],prev_cube[26],prev_cube[17],prev_cube[36],prev_cube[37],prev_cube[47],prev_cube[39],prev_cube[40],prev_cube[50],prev_cube[42],prev_cube[43],prev_cube[53],prev_cube[45],prev_cube[46],prev_cube[2],prev_cube[48],prev_cube[49],prev_cube[5],prev_cube[51],prev_cube[52],prev_cube[8]]
    print "Working cube after some work"
    print working_cube
    print prev_cube

# Move 4 - Move right column down
def move_4():
    working_cube=[prev_cube[0],prev_cube[1],prev_cube[47],prev_cube[3],prev_cube[4],prev_cube[50],prev_cube[6],prev_cube[7],prev_cube[53],prev_cube[9],prev_cube[10],prev_cube[11],prev_cube[12],prev_cube[13],prev_cube[2],prev_cube[17],prev_cube[26],prev_cube[35],prev_cube[18],prev_cube[19],prev_cube[20],prev_cube[21],prev_cube[22],prev_cube[5],prev_cube[16],prev_cube[25],prev_cube[34],prev_cube[27],prev_cube[28],prev_cube[29],prev_cube[30],prev_cube[31],prev_cube[8],prev_cube[15],prev_cube[24],prev_cube[33],prev_cube[36],prev_cube[37],prev_cube[14],prev_cube[39],prev_cube[40],prev_cube[23],prev_cube[42],prev_cube[43],prev_cube[32],prev_cube[45],prev_cube[46],prev_cube[38],prev_cube[48],prev_cube[49],prev_cube[41],prev_cube[51],prev_cube[52],prev_cube[44]]
    print "Working cube after some work"
    print working_cube
    print prev_cube
    
# Move 5 - Move top row left
def move_5():
    working_cube=[prev_cube[6],prev_cube[3],prev_cube[0],prev_cube[7],prev_cube[4],prev_cube[1],prev_cube[8],prev_cube[5],prev_cube[2],prev_cube[12],prev_cube[13],prev_cube[14],prev_cube[15],prev_cube[16],prev_cube[17],prev_cube[53],prev_cube[52],prev_cube[51],prev_cube[18],prev_cube[19],prev_cube[20],prev_cube[21],prev_cube[22],prev_cube[23],prev_cube[24],prev_cube[25],prev_cube[26],prev_cube[27],prev_cube[28],prev_cube[29],prev_cube[30],prev_cube[31],prev_cube[32],prev_cube[33],prev_cube[34],prev_cube[35],prev_cube[36],prev_cube[37],prev_cube[38],prev_cube[39],prev_cube[40],prev_cube[41],prev_cube[42],prev_cube[43],prev_cube[44],prev_cube[45],prev_cube[46],prev_cube[47],prev_cube[48],prev_cube[49],prev_cube[50],prev_cube[9],prev_cube[10],prev_cube[11]]
    print "Working cube after some work"
    print working_cube
    print prev_cube

# Move 6 - Move top row left
def move_6():
    working_cube=[prev_cube[2],prev_cube[5],prev_cube[8],prev_cube[1],prev_cube[4],prev_cube[7],prev_cube[0],prev_cube[3],prev_cube[6],prev_cube[53],prev_cube[52],prev_cube[51],prev_cube[9],prev_cube[10],prev_cube[11],prev_cube[12],prev_cube[13],prev_cube[14],prev_cube[18],prev_cube[19],prev_cube[20],prev_cube[21],prev_cube[22],prev_cube[23],prev_cube[24],prev_cube[25],prev_cube[26],prev_cube[27],prev_cube[28],prev_cube[29],prev_cube[30],prev_cube[31],prev_cube[32],prev_cube[33],prev_cube[34],prev_cube[35],prev_cube[36],prev_cube[37],prev_cube[38],prev_cube[39],prev_cube[40],prev_cube[41],prev_cube[42],prev_cube[43],prev_cube[44],prev_cube[45],prev_cube[46],prev_cube[47],prev_cube[48],prev_cube[49],prev_cube[50],prev_cube[17],prev_cube[16],prev_cube[15]]
    print "Working cube after some work"
    print working_cube
    print prev_cube

# Move 7 - Turn front face anti-clockwise
def move_7():
    working_cube=[prev_cube[0],prev_cube[1],prev_cube[2],prev_cube[3],prev_cube[4],prev_cube[5],prev_cube[15],prev_cube[24],prev_cube[33],prev_cube[9],prev_cube[10],prev_cube[8],prev_cube[14],prev_cube[23],prev_cube[32],prev_cube[38],prev_cube[16],prev_cube[17],prev_cube[18],prev_cube[19],prev_cube[7],prev_cube[13],prev_cube[22],prev_cube[31],prev_cube[37],prev_cube[25],prev_cube[26],prev_cube[27],prev_cube[28],prev_cube[6],prev_cube[12],prev_cube[21],prev_cube[30],prev_cube[36],prev_cube[34],prev_cube[35],prev_cube[11],prev_cube[20],prev_cube[29],prev_cube[39],prev_cube[40],prev_cube[41],prev_cube[42],prev_cube[43],prev_cube[44],prev_cube[45],prev_cube[46],prev_cube[47],prev_cube[48],prev_cube[49],prev_cube[50],prev_cube[51],prev_cube[52],prev_cube[53]]
    print "Working cube after some work"
    print working_cube
    print prev_cube

# Move 8 - Turn front face clockwise
def move_8():
    working_cube=[prev_cube[0],prev_cube[1],prev_cube[2],prev_cube[3],prev_cube[4],prev_cube[5],prev_cube[29],prev_cube[20],prev_cube[11],prev_cube[9],prev_cube[10],prev_cube[36],prev_cube[30],prev_cube[21],prev_cube[12],prev_cube[6],prev_cube[16],prev_cube[17],prev_cube[18],prev_cube[19],prev_cube[37],prev_cube[31],prev_cube[22],prev_cube[13],prev_cube[7],prev_cube[25],prev_cube[26],prev_cube[27],prev_cube[28],prev_cube[38],prev_cube[32],prev_cube[23],prev_cube[14],prev_cube[8],prev_cube[34],prev_cube[35],prev_cube[33],prev_cube[24],prev_cube[15],prev_cube[39],prev_cube[40],prev_cube[41],prev_cube[42],prev_cube[43],prev_cube[44],prev_cube[45],prev_cube[46],prev_cube[47],prev_cube[48],prev_cube[49],prev_cube[50],prev_cube[51],prev_cube[52],prev_cube[53]]
    print "Working cube after some work"
    print working_cube
    print prev_cube
 


""" Define each position that we will be aiming for """
# Level 1 - Corner 0
# Each face of this corner should be the same the central block of its face
def l1c0():
    if working_cube[0]==original_cube[4] and working_cube[9]==original_cube[19] and working_cube[51]==original_cube[49]:
        print "yes"
    else:
        print "no"
        
# Get system to pick a random number 


# Get system to move cube from random number
def rand_num():
    import random
    rand_number=0
    rand_number=random.randint(1,2)
    print rand_number
    list_moves.append(rand_number)
    print list_moves
    if rand_number==1:
        move_1()
    elif rand_number==2:
        move_2()
    elif rand_number==3:
        move_3()
    elif rand_number==4:
        move_4()
    elif rand_number==5:
        move_5()
    elif rand_number==6:
        move_6()
    elif rand_number==7:
        move_7()
    else:
        move_8()

# Run the solver
# Pick a random number, move the square, check whether it is OK, if yes stop, if no pick a random number - remember to keep a list
def solver():
    print "xxx"
    rand_num()
    print "Working cube at end"
    print working_cube
    print "Previous cube at end"
    prev_cube=list(working_cube)
    print prev_cube
    l1c0()
    print list_moves

solver()
solver()
