import random

lists = random.randint(3,10)
random_list = []

for _ in range(lists):
    number = random.randint(1,10)
    random_list.append(number)
print(random_list)
print([random_list[0], random_list[2], random_list[-2]])