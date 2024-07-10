# Функции, рекурсия, алгоритмы, модули

# def sum_numbers(n): # в скобках аргумент который хотим передать
#     summa = 0
#     for i in range(1, n+1): # сумму считаем с 1го элемента, поэтому (1, n+1)
#         summa += i
#     print(summa) # 1+2+3+4+5=15
# sum_numbers(5) # вызов суммы


# ВОЗВРАЩЕНИЕ ЗНАЧЕНИЯ
# def sum_numbers(n): # в скобках аргумент который хотим передать
#     summa = 0
#     for i in range(1, n+1): # сумму считаем с 1го элемента, поэтому (1, n+1)
#         summa += i
#         print(i) # вывел на экран цифры 1 до 5
#     return summa # если прога увидела return, то она завершает работу нашей функции
#
# a = sum_numbers(5)
# print(a)
# print(sum_numbers(5))

# def sum_str(*args):  # * - передать неограниченное количество аргументов(переменная args)
#     res = ''
#     for i in args:  # пройдемся по всем элементам переменной args
#         res += i
#     return res
# print(sum_str('q', 'e', 'l'))
# print(sum_str('q', 'e', 'l','r','f'))
# print(sum_str('1','8','9'))


'''МОДУЛЬНОСТЬ'''
# смотри в файлах main.py и modul1.py

'''РЕКУРСИЯ'''
'''ФУНКЦИЯ КОТОРАЯ ВЫЗЫВАЕТ САМА СЕБЯ'''

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)
# list_1 = []
# for i in range(1,10):
#     list_1.append(fib(i))
# print(list_1)


'''АЛГОРИТМЫ'''
'''быстрая сортировка'''


# def quick_sort(array):
#     if len(array) <= 1: # если длина(len) нашего массива <= 1 , то мы его возвращаем(return)
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
# print(quick_sort([12,34,3,23,6,66,34,12,78,0]))


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2 # делим список на 2 до тех пор, пока не останется по 1 элементу
        left = nums[:mid]    # делим список на 2 до тех пор, пока не останется по 1 элементу
        right = nums[mid:]   # делим список на 2 до тех пор, пока не останется по 1 элементу
        merge_sort(left)     # делим список на 2 до тех пор, пока не останется по 1 элементу
        merge_sort(right)    # делим список на 2 до тех пор, пока не останется по 1 элементу
        i = j = k = 0
        while i < len(left) and j < len(right): # создаем пары
            if left[i] < right[i]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


list1 = [2, 5, 3, 6, 7, 9, 0, 6, 4, 7, 9, 3, 6, 7, 8]
merge_sort(list1)
print(list1)