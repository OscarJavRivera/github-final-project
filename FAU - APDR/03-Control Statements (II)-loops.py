## Define the function floor_num_from_binary() , which takes in the  ##
## argument of actual floor number, binary_floor, of the blue tower ## 
## from the 4 bit binary floor number given by binary_floor. ##

import math

def floor_num_from_binary(binary_floor):
    '''(str) --> (int)
    Returns the actual floor number of the blue tower from the
    4 bit binary floor number given by binary_floor.
    '''
    
    ##TODO: Write your code below by removing the None and setting up your 
    # own logic. It would be more than 1 line so think carefully. ##
    #initialize variables
    bit_index=len(binary_floor)-1
    dec_value=0
    #Go through all the bits
    for bit_value in binary_floor:
        dec_value=dec_value+int(bit_value)*pow(2,bit_index)
        bit_index=bit_index-1 #Reduce index
    
    floor_num = dec_value
    print(dec_value)
    return floor_num

""" floor_num_from_binary('0000')
floor_num_from_binary('0001')
floor_num_from_binary('0010')
floor_num_from_binary('0011')
floor_num_from_binary('0100')
floor_num_from_binary('0111') """

## Define the function paint_binary() , which takes in the  ##
## argument of a decimal floor number, floor_num, and returns ## 
## the 4 bit binary equivalent of it. ##

def paint_binary(floor_num):
    '''(int) --> (str)
    Returns the 4-bit binary floor number given the
    actual floor number you are in.
    '''

	##TODO: Write your code below by removing the None and setting up your 
    # own logic. It would be more than 1 line so think carefully. ##
    #assert floor_num>15, "Error"
    binary_num=""
    if floor_num==0:
        binary_num="0000"
    elif floor_num<=15:
        rem_floor_num=floor_num
        while rem_floor_num>0:
            binary_num=str(rem_floor_num%2)+binary_num  #Create the binary strin
            rem_floor_num=int(rem_floor_num/2)          #Calculate the remaining
    
    return binary_num

## Create a second version of the decimal to binary, ## 
## floor_num_from_binary_v2() which takes in the argument ##
## binary_floor (a Python binary number) and convert it ##
## to decimal value using Python in-built functions ##

def floor_num_from_binary_v2(binary_floor):
    '''(binary) --> (int)
    Makes use of Python's in-built function to convert
    binary floor number to int and returns it.
    '''
    ##TODO: Write your code below by removing the None and setting up your 
    # own logic. ##
    
    floor_num = int(binary_floor,2)
    
    return floor_num

#print("Resul of floor_num_from_binary_v2: ",floor_num_from_binary_v2("111"))

## Create a second version of the binary to decimal, ## 
## paint_binary_v2() which takes in the argument ##
## floor_num (an integer value) and convert it ##
## to binary value using Python in-built functions ##

def paint_binary_v2(floor_num):
    '''(int) --> (str)
    Makes use of Python's in-built function to convert
    integer valued floor number you are in and returns
    it.
    '''

	##TODO: Write your code below by removing the None and setting up your 
    # own logic. It would be more than 1 line so think carefully. ##
    assert floor_num<=15, "Error" 
    binary_num_string= bin(floor_num)
    binary_num_string=binary_num_string.split("0b")
    binary_num=binary_num_string[1]
    while len(binary_num)<4:
        binary_num="0"+binary_num
    binary_num =None
    return binary_num

#print("The result of paint_binary_v2 is:",paint_binary_v2(16))
paint_binary_v2(16)

def square(x):
    assert x>=0, 'Only positive numbers are allowed'
    return x*x

# n = square(2) # returns 4
n = square(-2) # raise an AssertionError
