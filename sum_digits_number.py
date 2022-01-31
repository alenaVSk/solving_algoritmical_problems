''' Сумма цифр числа
Дано натуральное число N. Вычислите сумму его цифр.
При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы,
разумеется). 
'''

def sum_digits_number(n):
    if n < 10:
        return n
    else:
        right = n % 10
        left = n // 10
        return right + sum_digits_number(left)
 
     
print(sum_digits_number(92179))
