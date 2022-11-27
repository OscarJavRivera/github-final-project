def factorial(num):
    '''(num) -> (num)
    Calculates the factorial of a number, given by the variable num.
    '''

    #TODO: Check for the errors in the below code and fix them.

    output = 1

    while num > 0:
        output *= num
        num = num - 1

    return output

## print(factorial(5))

def list_ratios(list_1 , list_2):
    '''(list , list) -> list
    Returns a new list which has the elements list_1 / list_2.
    '''

    #TODO: Use an assertion statement which checks if the lists are same.
    assert list_1!=list_2, "The same list"
    new_list = []
    
    for i in range(len(list_1)):
        
        try:
            new_list.append(list_1[i]/list_2[i])
        
        except ZeroDivisionError:
            print ("Error: Division by zero")
            new_list.append("nan")
            
        except TypeError:
            print("Wrong input type. Values should be integer.")
            new_list.append(None)
        else:
            print("The operation",list_1[i],"/",list_2[2],"was done.")

    return new_list

#Testing the assertion (when the list is the same)
list_1=[0.0, 5.0, 6.0]
list_2=[0.0, 5.0, 6.0]
#print(list_ratios(list_1,list_2))

#Testing the TODO 2 & 3
list_1=[1.0, '2.', 3.0]
list_2=[0.0, 5.0, 6.0]
#print(list_ratios(list_1,list_2))

#Testing the good case
list_1=[4.0, 5, 7]
list_2=[8.0, 10.0, 10.0]
print(list_ratios(list_1,list_2))