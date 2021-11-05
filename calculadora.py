while (1):
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    q for exit
    ''')
    if operation=='q':
        break
    x = int(input('First number: '))
    y = int(input('Second number: '))

    if operation == '+':
        print('{} + {} = '.format(x, y))
        print(x + y)

    elif operation == '-':
        print('{} - {} = '.format(x, y))
        print(x - y)

    elif operation == '*':
        print('{} * {} = '.format(x, y))
        print(x * y)

    elif operation == '/':
        print('{} / {} = '.format(x, y))
        print(x / y)

    else:
        print('You have not typed a valid operator, please run the program again.')

