# def f(x):
#     return x*x # возвращение квадрат числа Х
#
# print(type(f)) # <class 'function'>
# print(f'Ответ: ', f(5))  # Ответ:  25


# калькулятор

# def calk1(a, b):
#     return a + b
#
# def calk2(a, b):
#     return a * b
#
# def math(op, x, y):
#     print(op(x, y))
#
# math(calk1, 5, 45)


# =================================================================

# def calk2(a, b):
#     return a * b
#
# def math(op, x, y):
#     print(op(x, y))

# 31 и 32 = 34 строке
# def calk1(a, b):
#     return a + b

'''
lambda =============
'''

# 36 и 37 = 39
# calk1 = lambda a, b: a + b
# math(calk1, 5, 45)

# math(lambda a, b: a + b, 5, 45)

# =================================================================
'''
list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
res = list()
for i in list_1: # проходим по всем элементам списка list_1
    if i % 2 == 0: # если элемент i четное, то есть делится на 2
        res.append((i, i**2)) # то в список res добавляем (i, i**2)
print(res)
'''

# def select(f, col):
#     return [f(x) for x in col] # возвращает список элементов функции f
#
# def where(f, col):
#     return [x for x in col if f(x)] # возвращает только то значения, которые прошли проверку условия f(x)
#
# list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, list_1)
# print(res)
# res = where(lambda x: x % 2 == 0, list_1)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# =================================================================

'''функция map. Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и
возвращает итератор с новыми объектами.'''

# list_1 = [x for x in range(1, 20)]
# print(list_1)
#
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# .split преобразует строку в список

# data = '12 45 32 65 67'
# print(data)
#
# data = data.split() # преобразует строку в список
# print(data)


# data = '12 45 32 65 67'
# data = list(map(int, data.split()))
# print(data)

'''ФУНКЦИЯ filter. Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для которых функция вернула True.'''

# list_1 = [15, 65, 5, 44, 75, 95]
# res = list(filter(lambda x: x % 10 == 5, list_1))
# print(res)



'''
Функция ZIP Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами
из элементов входных данных
'''
'''
users = ['pavel', 'olya', 'mama', 'vitalya', 'papa']
ids = [4, 2, 6, 9, 13]
salary = [1000, 2000, 3000, 4000, 5000]
data = list(zip(users, ids, salary))
print(data)
'''

# функция ENUMERATE. Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с
# кортежами из индекса и элементов входных данных.

users = (['pavel', 'olya','mama', 'vitalya', 'papa'])
data = list(enumerate(users))
print(data) # [(0, 'pavel'), (1, 'olya'), (2,'mama')]









