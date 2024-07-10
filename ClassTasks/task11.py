num = int(input("Введите число А "))
fib1 = 0
fib2 = 1
count = 2
while fib2 < num:
    fsumm = fib1 + fib2
    fib1 = fib2
    fib2 = fsumm
    count += 1
if fib2 == num:
    print(count)
else:
    print("-1")