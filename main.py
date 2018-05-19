import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
#cursor.execute('Create table users (login text,password text,email text,last_name text,first_name text, birthday text)')
#cursor.execute('Insert into users values("arys","arys123","arys@gmail.com","arystan","berdykul","05.05.1919")')
#result = cursor.execute('Select * from users')
#print(result.fetchall())
while True:    
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
    elif num_change == 2:
        login_cr=input('Login: ')
        check_login = cursor.execute('Select * from users where login = "%s"'%(login_cr)).fetchone()
        while check_login is not None:
            print('Try again')
            login_cr=input('Login: ')
            check_login = cursor.execute('Select * from users where login = "%s"'%(login_cr)).fetchone()
        password_cr=input('Password: ')
        email_cr=input('Email: ')
        last_name_cr=input('Last Name: ')
        first_name_cr=input('First name: ')
        birthday_cr=input('Birthday: ')         
        cursor.execute('Insert into users values("%s","%s","%s","%s","%s","%s")'%(login_cr,password_cr,email_cr,last_name_cr,first_name_cr,birthday_cr))
    conn.commit()
    conn.close()


