# Задача 4.
#
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

n = input('Введите общее количество журавликов: ')
n = int(n)

if n > 0:
    x = n // 3  # равное количество журавликов на 3х
    sergey = x // 2
    petya = x // 2
    katya = (sergey + petya) * 2
    print(f'Катя сделала: {katya} журавликов')
    print(f'Сережа сделал: {sergey} журавликов')
    print(f'Петя сделал: {petya} журавликов')

