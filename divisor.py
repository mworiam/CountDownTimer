'''Create a program that asks the user for a number and then prints out a list of all the divisors of
that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number.'''

num = int(input("Enter num: "))

list_range = list(range(1, num+1))

divisor = []

for number in list_range:
    if num % number == 0:
        divisor.append(number)

print(divisor)

