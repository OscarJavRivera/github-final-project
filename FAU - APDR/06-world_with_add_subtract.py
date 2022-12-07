
import sys

#TODO: Create a function add() which adds two numbers. 
def add(a1,a2):
    '''(floar , float) -> float
    Calculate the addition of two variables
    '''
    return a1+a2

#TODO: Create a function subtract() which subtracts two numbers.
def subtract(a1,a2):
    '''(floar , float) -> float
    Calculate the substration of two variables
    '''
    return a1-a2

#TODO: Create multiplication,multiply(), of two natural numbers using addition and our friend recursion..
def multiply(a,b):
    '''(int, int) -> int 
        calculate the multiplication of two factors using recursion
    '''
    
   #Rise exceptions
    if type(a)!=int or type(b)!=int:
        raise AssertionError('Only integers are accepted')
    
    #Base Conditions 
    if a<=0 or b<=0:
        return 0
    if b==1:
        return a
    #Calculate iterative multiplication
    else:
        return a + multiply(a,b-1)
    

#Testing the multiply function
#print(multiply(3,2))
#print(multiply(-1,-10))
#print(multiply(-1,10))
#print(multiply(1,-10))
#print(multiply(50000000,200000))
#print (type(50000000*200000)," ",50000000*200000)
    
#TODO: Create division,division(), of two natural numbers using addition, subtraction and our friend recursion..
def division(num1,num2):
    '''(int,int) -> int
        Calculate the division of two numbers using only addition, substration and recursion.
    '''
   #Raise exceptions 
    if type(num1)!=int or type(num2)!=int:
        raise AssertionError('Only integers are accepted')
    #Base conditions
    if num1<=1:
        return 0
    if num2==0:
        raise ZeroDivisionError('Division by Zero')
    
    #Calculate division
    else:
        res_sub=subtract(num1,num2)
        return add(division(res_sub,num2),1)
    
#Test Division
#print(division(13,3))

