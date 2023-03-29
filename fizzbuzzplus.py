#Write a program that prints the numbers from 1 to 100, but...

#numbers that are exact multiples of 3, or that contain 3, must print a string containing "Fizz"
   #For example 9 -> "...Fizz..."
   #For example 31 -> "...Fizz..."

#numbers that are exact multiples of 5, or that contain 5, must print a string containing "Buzz"
   #For example 10 -> "...Buzz..."
   #For example 52 -> "...Buzz..."


for num in range(1,101):
    if num % 3 == 0 or '3' in str(num):
        if num % 5 == 0 or '5' in str(num):
            print(f'fizzbuzz, {num}')
        else:
            print(f'fizz, {num}')
    if num % 5 == 0 or '5' in str(num):
        print(f'buzz, {num}')
    else:
        print(num)
