from random import randint

class User:
    user_name = 'Ivan'
    email = 'Ivan_Ivanov_8_088@ya.ru'
    password = '654321'

class RandomUser:
    user_name = f'TestName{randint(0, 999)}'
    email = f'mailtest{randint(0, 999)}@gmail.com'
    password = f'qw{randint(1000, 9999)}rty'