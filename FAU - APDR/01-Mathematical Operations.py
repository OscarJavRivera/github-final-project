from datetime import datetime
from operator import truediv
import string


# ## Excersice 1.1""" 
# - [ ] Take input of the current time from the user in the format HH:MM:SS. Store it in the variable current_time
# - [ ] Extract the Hours, Minutes and Seconds from current_time.

# Hint: Check out the functionality of string.split() method of the string datatype.

# - [ ] Typecast Hours, Minutes and Seconds into integers.
# - [ ] Take input of the user's current timezone and the target timezone. Store them as float values in the variables  current_timezone  and target_timezone respectively.

# Hint: Python's input() method takes in string values. Don't forget to typecast them to float. """

def get_time_timezone():
    """(None) --> (int,int,int,float,float)
    Returns the current time trisected in hours, minutes, seconds. Along with that also returns the timezone1 and
    timezone2 as given by the user.
    """

    ## Take input from the user the current time in the format: HH:MM:SS ##
    current_time = input("In the format HH:MM:SS, please insert your time here: ")
    ## State to the user to give a valid time with the 24 hour clock ##
    if current_time==' ' or current_time.lenght() <6 :
        print("Invalid Input: Please insert the time in the format HH:MM:SS") 

    ## Extract the hour, minutes and seconds from the current time ##
    time_x = current_time.split(":")
           

    ## Typecast hours, minutes and seconds to integer for using it later on ##
    hours, minutes, seconds = int(time_x[0]) , int(time_x[1]) , int(time_x[2])

    ## Get the UTC ofset for the current place and the target place ##
    #TODO
    current_location = int(print("Insert your current location (1) --> Iceland or (2)--> India"))
    
    if current_location == 1: ##Iceland
        UTC_Offset_hour = 0
        UTC_Offset_min=0
        target_timezone_aux=(current_time)+UTC_Offset_hour+UTC_Offset_min
    elif current_location == 2: ##India
        UTC_Offset_hour = 5
        UTC_Offset_min = 30
        target_timezone_aux=(current_time)+UTC_Offset_hour+UTC_Offset_min

    current_timezone = current_time
    target_timezone = target_timezone_aux

    return hours, minutes, seconds, current_timezone, target_timezone

target_time_in_sec = 19530
remaining_sec = target_time_in_sec%3600
print(remaining_sec)
#get_time_timezone()