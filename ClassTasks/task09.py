# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

print("Введите число: ")
a = int(input())
print(f'Вы ввели нахождение {a}!')

factorial = 1
while a > 1:
    factorial = factorial * a
    a = a - 1

print(f'Произведение чисел = {factorial}')