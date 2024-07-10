# from random import randint
#
# list_1 = list()
# lens = int(input("Enter the length of the list: "))
# for i in range(lens):
#     list_1.append(randint(0, 10))
# # print(type(lis))
#
# print(f'1st version of list: {list_1}')
# list_1.sort()
# print(f'Sorted list: {list_1}')
# lis_1 = list(set(list_1))
# print(f'Removed duplicate: {lis_1}')

# 2ой вариант ниже:

# list_1 = {2, 3, 5, 23, 45, 12, 41, 1, 21, 24, 14}
# list_2 = {23, 46, 2, 57, 98, 66, 41, 68, }
# print(f'1st list: {list_1}')
# print(f'2nd list: {list_2}')
# list_copy = list_1.copy()
# list_3 = list_1.union(list_2)
# print(f'Union lists: {list_3}')


# 3ий вариант

from random import randint

list_1 = list()
lens = int(input("Enter the length of the 1st list: "))
for i in range(lens):
    list_1.append(randint(0, 10))

list_2 = list()
lens = int(input("Enter the length of the 2nd list: "))
for i in range(lens):
    list_2.append(randint(0, 10))

print(f'1st list: {list_1}')
print(f'2nd list: {list_2}')

list_3 = list_1 + list_2  # объединяем в один список
print(f'Union lists: {list_3}')
list_3.sort()  # сортировка
print(f'Sorted list: {list_3}')
# ниже убирает повторяющиеся значения
temp = []
for x in list_3:
    if x not in temp:
        temp.append(x)
list_3 = temp
print(f'Cleaned List: {temp}')
