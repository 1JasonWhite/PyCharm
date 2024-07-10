'''Задача No35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
'''

def issimple_number(num)
    kol = 0
    for i in range(1, num + 1):
        if num % i == 0:
            kol += 1
        if kol == 2:
            return (f'Число {num} простое')
        else:
            return (f'Число {num} составное')
print(issimple_number(5))