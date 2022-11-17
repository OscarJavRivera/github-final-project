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

paint_binary(0)
