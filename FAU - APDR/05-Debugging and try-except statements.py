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

        #TODO: 1. Write a try statement
        #TODO: 2. Write an except statement where if there is some division by zero then nan value will be the result
        #TODO: 3. Write an except statement where if there is any type problem then None value will be the result
        for i in list_1:#,list_2:
            try:
                new_list[i]= list_1[i]/list_2[i]
            
            except NameError:
                print ("Error:Division by zero")

                return new_list

#Testing the assertion (when the list is the same)
list_1=[0.0, 5.0, 6.0]
list_2=[0.0, 5.0, 6.0]
#print(list_ratios(list_1,list_2))

list_1=[1.0, '2.', 3.0]
list_2=[0.0, 5.0, 6.0]
print(list_ratios(list_1,list_2))