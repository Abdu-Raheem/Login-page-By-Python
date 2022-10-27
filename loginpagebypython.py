import fontstyle


details = []


def create():
    n = 1

    while n != 0:
        i = 0
        dic = {}
        dic['name'] = input('name: ')
        dic['username'] = input('Username: ')
        password1 = input('Password: ')
        dic['password'] = input('Re-enter the Password: ')
        details.append(dic)
        i = i + 1
        if dic['password'] == password1:
            print('You have created the Account successfully...!')
            home()
        else:
            print(fontstyle.apply('Doesnt Match', 'bold/red'))
            continue


def home():
    print('1)Create a account\n2)login\n3)exit')
    opt = int(input())

    if opt == 1:
        create()
    if opt == 2:
        login()
    if opt == 3:
        exit()


def login():
    if len(details) == 0:
        print(fontstyle.apply('Acount not exist', 'bold/red'))
    user = input('Enter your username: ')
    size = len(details)
    flag1 = 0
    flag3 = 0
    for x in range(size):

        if user == details[x]['username']:
            flag3 = 3
            flag = x
        else:
            flag1 = 1

        if flag3 == 3:
            pas = input('Enter your password: ')
            if pas == details[flag]['password']:
                a = details[flag]['name']
                print(fontstyle.apply(f'{a} Entered successfully', 'bold/green'))
                home()
            else:
                print(fontstyle.apply('wrong password', 'bold/red'))
                login()

    if flag1 == 1:
        print(fontstyle.apply('wrong username', 'bold/red'))
        login()

home()