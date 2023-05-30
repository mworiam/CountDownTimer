def reverse_words(string):
    # Split the string into individual words
    words = string.split()

    # Reverse the order of words
    reversed_words = words[::-1]

    # Join the reversed words into a new string
    reversed_string = ' '.join(reversed_words)

    return reversed_string

# Ask the user for a long string
user_string = input("Enter a long string containing multiple words: ")

# Reverse the words and print the result
reversed_string = reverse_words(user_string)
print("Reversed string:")
print(reversed_string)
