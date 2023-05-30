'''Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.'''

def reverseWord():
  w = input('Enter sentence: ')
  return ' '.join(w.split()[::-1])
print(reverseWord())
