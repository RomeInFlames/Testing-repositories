Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = int(input("Введите первое число: "))
... num2 = int(input("Введите второе число: "))
... 
... print("Первое число:", num1)
... print("Второе число:",  num2)
... 
... message = '''
... Выберете математическую операцию:
... 
... + : Сложение
... - : Вычитание
... / : Деление
... * : Умножение
... 
... Ваш выбор:
... '''
... 
... # спрашиваем у пользователя, какую операцию он хочет выбрать
... operation = input(message)
... 
... # выводим выбранную операцию (или сообщение об ошибке)
... if operation == '+':
...     print('Сложение')
...     result = num1 + num2
... elif operation == '-':
...     print('Вычитание')
...     result = num1 - num2
... elif operation == '/':
...     print('Деление')
...     result = num1 / num2
... elif operation == '*':
...     print('Умножение')
...     result = num1 * num2
... else:
...     print('Неизвестная операция')
... 
... 
