import datetime
today = datetime.date.today()
year = today.year

birth_year = int(input("The Year you were born: "))

age = year - birth_year
year_to_100 = (year - age) + 100


print(f'You are {age} years old')
print(f'You will turn 100 in the year {year_to_100}')