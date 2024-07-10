from random import randint

count = int(input('Введите количество арбузов: '))

for i in range(count):
    print(randint(0, 30000))

max = 0
min = 100


for i in range(count):
    melon = randint(0, 100)
    print(melon)
    if melon > max:
        max = melon
    if melon < min:
        min = melon
print()
print(max)
print(min)