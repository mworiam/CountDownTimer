'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list. For practice,
write this code inside a function.'''

a = [56, 2, 5, 10, 15, 20, 25, 40, 65, 43]
b = []

def list_end():
    b.append(a[0])
    b.append(a[-1])
    return b
print(list_end())
