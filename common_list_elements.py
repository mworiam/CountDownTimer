import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

set_a = set(a)
set_b = set(b)

common_elements = set_a.intersection(set_b)
result = list(common_elements)
print(result)



# random_list = random.sample(range(0,50), 5)
# random_list2 = random.sample(range(0,50), 8)
# combined_list = random_list + random_list2

# print(set(combined_list))