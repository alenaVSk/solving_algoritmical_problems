''' Цифры числа слева направо
Дано натуральное число N. Выведите все его цифры по одной, в обычном порядке, разделяя 
их пробелами или новыми строками.
При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы, 
разумеется). Разрешена только рекурсия и целочисленная арифметика. 
Пример: 179  --->  1 7 9
'''

def numbers_with_spaces(n):
    if n < 10:
        print(n, end=' ')
    else:
        right = n % 10
        left = n // 10
        numbers_with_spaces(left)  
        print(right, end=' ')


numbers_with_spaces(179)
print()