num3 = [0, 0, 0, 1, 2]

lst_num = num3

for i in num3:
    if i == 0:
        lst_num.remove(0)
        lst_num.append(0)
print(lst_num)

# это второй вариант подумал пусть тоже будет все два вроде работают

# num3 = [0,0,0,0,22,3,4,564,32,0,0,4,0]

# for i in range(num3.count(0)):
#     num3.remove(0)
#     num3.append(0)
# print(num3)














