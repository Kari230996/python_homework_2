'''
3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. 
Для проверки своего кода используйте модуль fractions.
'''

from fractions import Fraction


str1 = input('Введите первую дробь (в формате a/b): ')
str2 = input('Введите вторую дробь (в формате a/b): ')


numerator1, denominator1 = map(int, str1.split('/'))
numerator2, denominator2 = map(int, str2.split('/'))

# Вычисляем НОД (наибольший общий делитель) для знаменателей
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Находим общий знаменатель
common_denominator = (denominator1 * denominator2) // gcd(denominator1, denominator2)


# Приводим дроби к общему знаменателю
numerator1 *= common_denominator // denominator1
numerator2 *= common_denominator // denominator2

# Вычисляем сумму и произведение
sum_result = numerator1 + numerator2
product_result = numerator1 * numerator2

print("Сумма дробей:", sum_result, "/", common_denominator)
print("Произведение дробей:", product_result, "/", (common_denominator ** 2))


# Проверка с помощью функцией Fraction

frac1 = Fraction(numerator1, denominator1)
frac2 = Fraction(numerator2, denominator2)

sum_result2 = frac1 + frac2
product_result2 = frac1 * frac2

print(sum_result2)
print(product_result2)

# Результаты, полученные с использованием модуля fractions, отличаются от результатов, 
# полученных вручную, потому что вручную мы выполняем операции над числителями и знаменателями, 
# не упрощая дроби, 
# в то время как модуль fractions автоматически упрощает дроби к их наименьшему знаменателю.








