def password_generator():
    import random

    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+'


while True:
    print('''-- Password Generator --
          Choose option:
          1. Generate Password
          2. Exit the program''')
    choice = input('Your choice: ')

    if choice == '1':
        try:
            length = int(input('Provide password length: '))
            uppercase_letter = input('Use uppercase letters? (y/n): ')
            password_generator()
        except ValueError:
            print('Please enter a valid number!')
    elif choice == '2':
        print('Bye!')
        break
    else:
        print('Please enter a correct value!')


