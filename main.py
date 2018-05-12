import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
#cursor.execute('Create table users (login text,password text,email text,last_name text,first_name text, birthday text)')
#cursor.execute('Insert into users values("arys","arys123","arys@gmail.com","arystan","berdykul","05.05.1919")')
#result = cursor.execute('Select * from users')
#print(result.fetchall())
print('Добро пожаловать в систему регистрации')
print('Введите 1-авторизация, 2-регистрация')
num_change = int(input())
if num_change == 1:
    login=input('LOGIN: ')
    password=input('PASSWORD: ')
    res = cursor.execute('Select * from users where login = "%s" and password = "%s"'%(login,password)).fetchone()
    if res is not None:
        print('Welcome')
    else:
        print('Ooops!')
if num_change == 2:
    pass
else:
    print('error')
conn.commit()
conn.close()
