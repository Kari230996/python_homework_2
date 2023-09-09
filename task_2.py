'''
2. Напишите программу, 
которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''
hex_characters = "0123456789abcdef"

while True:
    try:
        num = int(input('Введите целое число: '))
        result = ''  # Обнуляем переменную result перед каждой операцией ввода

        print(hex(num))

        while num > 0:
            remainder = num % 16
            result = hex_characters[remainder] + result
            num //= 16
        
        if result:
            print("0x" + result)
            
        else:
            print("0x0")
            
    except ValueError:
        print('Число должно быть целым!')


