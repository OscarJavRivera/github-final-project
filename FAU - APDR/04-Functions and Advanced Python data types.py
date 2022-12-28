##TODO: Setup your add_dvd_to_stack(dvd_stack , lying_dvd) below ##

def add_dvd_to_stack(dvd_stack , lying_dvd):
    '''(list , str) --> updated_list
    Adds lying_dvd at the end of the dvd_stack.
    '''

    ## TODO: Update the dvd_stack
    dvd_stack.append(lying_dvd)   

    return dvd_stack


dvd_stack=["disk1","disk1","disk3"]
print("State add_dvd_to_stack",dvd_stack)
lying_dvd="disk4"
add_dvd_to_stack(dvd_stack,lying_dvd)
print("Result of add_dvd_to_stack",dvd_stack)


##TODO: Setup your remove_duplicates(display_stack) below ##

def remove_duplicates(display_stack):
    '''(list) --> list
    Removes duplicate dvd from the stack, display_stack.
    '''

    ## TODO: Remove duplicate from the display_stack
    unique_stack=set(display_stack)
    updated_display_stack = list(unique_stack)

    return updated_display_stack

print("Initial list:",dvd_stack)
print("Result of remove_duplicates: ",remove_duplicates(dvd_stack))


##TODO: Setup your category_sort(movie_name) below ##
movie_name = {'Harry Potter and the Chamber of the secrets': 'Fantasy', 'Lord of the Rings: The Fellowship of the Ring': 'Fantasy', 'Fast and Furious': 'Action', 'James Bond : Skyfall': 'Action', 'Deep Water': 'Mystery'}
print(movie_name)
def category_sort(movie_name):
    '''(dic)-->dic
    categorize the movies by category; the category would be the dictionary key
    '''
    #[ ] Given the dictionary, movie_name, which contains each movie names as 
    # a key and its category as the value, create another dictionary which has
    # the categories as its keys and the movies with the same categories as the values (stored in a list).
    
    category_based_movies={}
    for mov,cat in movie_name.items():

        if cat in category_based_movies:
            mov_list=category_based_movies[cat]

        elif cat not in category_based_movies:
            mov_list=[]
            
        mov_list.append(mov)
        category_based_movies[cat]=mov_list
        
    return category_based_movies

category_based_movies=category_sort(movie_name)
print(category_based_movies)

##TODO: Setup your find_a_movie(category_based_movies , movie) below ##
def find_a_movie(category_based_movies, movie):
    '''(dict, str)-->boolean
    Check if the 'movie' is available on the 'category_based_movies' dictionary
    '''
    for cat,mov in category_based_movies.items():
        if movie in mov:
            movie_available=True
            break
        else:
            movie_available=False
    
    return movie_available

print(find_a_movie(category_based_movies,'Harry Potter and the Chamber of the secrets'))
print(find_a_movie(category_based_movies,'Deep Water'))
print(find_a_movie(category_based_movies,'Spiderman'))

##TODO: Setup your all_movies_in_category(category_based_movies , category) below ##
def all_movies_in_category(category_based_movies, category):
	    
    
    for cat,mov in category_based_movies.items():
        
        if category in cat:
            
            return mov
        else:
            cat_found=False
    
    assert cat_found!=False, "The category "+category+" does not have any movies."
        

print(all_movies_in_category(category_based_movies, 'Fantasy'))
print(all_movies_in_category(category_based_movies, 'Horror'))
    