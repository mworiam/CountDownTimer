'''Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)'''

string = input("Please enter string: ")

reversed_string = string[::-1]

if string == reversed_string:
    print("string is a palindrome")
else:
    print("string is not a palindrome")

