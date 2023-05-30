'''Write a program (function!) that takes a list and returns a new list that contains
all the elements of the first list minus all the duplicates.'''

a = [1,1,2,3,3,4,4,5,6,7]

def remove_dups():
    b = list(set(a))
    return b
print(remove_dups())