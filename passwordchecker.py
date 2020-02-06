#Created by bobby233.Github:https://github.com/bobby233/learnpython
#Version:V1.0.0
def main():
    count = 0
    while count < 3: #You can set the wrong time here. 
        username = str(input('Enter username: '))
        password = str(input('Enter password: '))
        if username == 'bobby' and password == '000000': #You can set the username and password here. 
            print('Welcome')
        else:
            if (2 - count) == 0:
                print('ERR')
                break
            print('Wrong')
            print('You have %d times to enter' % (2 - count))
        count += 1
if __name__ == '__main__':
    main()