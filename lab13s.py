"""
A module with several recursive functions on sequences

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


# IMPLEMENT ALL OF THESE FUNCTIONS

def sum_list(thelist):
    """
    Returns the sum of the integers in list thelist.

        Example: sum_list([34]) is 34
        Example: sum_list([7,34,1,2,2]) is 46

    Parameter thelist: the list to sum
    Precondition: thelist is a list of ints
    """
    
    #Base case for list length 0 and 1
    if len(thelist) == 0:
        return 0
    elif len(thelist) == 1:
        return thelist[0]

    #Find mid of list to break it into 2 parts
    list_mid = len(thelist)//2

    #Calling recursive functions for both the lists
    return sum_list(thelist[:list_mid]) + sum_list(thelist[list_mid:])


def numberof(thelist, v):
    """
    Returns the number of times v occurs in thelist.

    Parameter thelist: The list to count from
    Precondition: thelist is a list of ints

    Parameter v: The value to count
    Precondition: v is an int
    """
    # HINT: Divide and conquer only applies to one of the arguments, not both

    #Base case for list length 0 and 1
    if len(thelist) == 0:
        return 0
    elif len(thelist) == 1:
        if thelist[0] == v:
            return 1
        else:
            return 0

    #Find mid of list to break it into 2 parts
    list_mid = len(thelist)//2

    #Calling recursive functions for both the lists
    return numberof(thelist[:list_mid], v) + numberof(thelist[list_mid:], v)


# OPTIONAL EXERCISES

def remove_dups(thelist):
    """
    Returns a COPY of thelist with adjacent duplicates removed.

    Example: for thelist = [1,2,2,3,3,3,4,5,1,1,1]
    the answer is [1,2,3,4,5,1]

    Parameter thelist: The list to modify
    Precondition: thelist is a list of ints
    """
    # HINT: You can still do this with divide-and-conquer
    # The tricky part is combining the answers
    return [] # Stub return.  Replace this.


def number_not(thelist, v):
    """
    Returns the number of elements in thelist that are NOT v.

    Parameter thelist: the list to search
    Precondition: thelist is a list of ints

    Parameter v: the value to search for
    Precondition: v is an int
    """
    return 0 # Stub return.  Replace this.


def remove_first(thelist, v):
    """
    Returns a COPY of thelist but with the FIRST occurrence of v removed (if present).

    Note: This can be done easily using the method index. Don't do that.
    Do it recursively.

    Parameter thelist: the list to search
    Precondition: thelist is a list of ints

    Parameter v: the value to search for
    Precondition: v is an int
    """
    return [] # Stub return.  Replace this.