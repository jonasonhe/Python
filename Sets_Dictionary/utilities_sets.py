#Jonason He 

set_1 = {"apple", "banana", "orange", "peach"}
set_2 = {"banana", "pineapple", "peach", "watermelon"}

#1
def get_total_items(input_set = set_1):
    '''
    Returns the total number of items for the given set "Number of elements = X"

    :param substring: given set 
    :type substring: string
    :return: number of elements within the string
    :rtype: int
    '''

    print(input_set)
    numb_of_elements = len(input_set)
    print(numb_of_elements)
    return numb_of_elements



def display_all_items(input_set = set_1): 
    '''
    Prints all the elements for the given set using iteration. Returns list ["x1", "x2", ...]

    :param substring: given set
    :type substring: string
    :return: all elements converted to list format
    :rtype: string
    '''
    for items in input_set: 
        print(items)

    list_1 = list(input_set)
    print(list_1)
    return list_1

def add_item(item = None, input_set = set_1):
    '''
    Adds the given item to the set Returns list ["x1", "x2", ...]

    :param substring: item the user wants to add, given set
    :type substring: string
    :return: set of strings after user has added an additional element
    :rtype: string 
    '''
    if item == None: 
        while True: 
            item = input(f"Enter an item from the set that you want to add to this set {input_set}: ")
            break
    
    input_set.add(item)
    new_list = list(input_set)
    print(new_list)

    return new_list


def remove_item(item = None, input_set = set_1):
    '''
    Removes the given item from the set Returns list ["x1", "x2", ...]

    :param substring: Item the user wants to remove, given set
    :type substring: string
    :return: set of strings after user removed element
    :rtype: string 
    '''
    if item == None: 
        while True: 
            item = input(f"Enter an item from the set that you want to remove from this set {input_set}: ")
            if item not in input_set: 
                print("Error - item does not exist in the set")
                continue
            else: 
                break
    
    input_set.remove(item)
    new_list = list(input_set)
    print(new_list)
    
    return new_list



def get_the_union_of(my_set1 = set_1, my_set2 = set_2):
    '''
    Returns the uniton of the given sets; set_1 and set_2
    :type substring: string
    :return: combined set of elements entered by the users
    :rtype: string 
    '''
    
    new_set = my_set1.union(my_set2)
    new_set_list = list(new_set)
    print(new_set_list)
    
    return new_set_list

# set_1 = {"apple", "banana", "orange", "peach"}
# set_2 = {"banana", "pineapple", "peach", "watermelon"}
def test_function_set():
    '''
    Test for all functions
    return: whether the functions pass/failed the test
    '''
    # Get total items Test
    print("Get Total Items Tests")
    total_items = get_total_items({"apple", "banana", "orange", "peach"})
    if total_items == 4:
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    # Display All Items Test
    print("Display All Items Tests")
    all_items = display_all_items(["apple", "banana", "orange", "peach"])
    if all_items == (["apple", "banana", "orange", "peach"]):
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    # Add Item
    print("Add Items Test (grape)")
    add_set = add_item("grape")
    if len(add_set) == 5:
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    # Remove Item
    print("Remove Item Test (grape))")
    remove_set = remove_item("grape")
    if len(remove_set) == 4:
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    # Union Set
    print("Union Set Test (Set_1/Set_2)")
    union_set = get_the_union_of()
    if len(union_set) == 6:
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")






    
