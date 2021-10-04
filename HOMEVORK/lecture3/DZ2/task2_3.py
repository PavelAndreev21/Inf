def min():
    a = int(input('The first number: '))
    b = int(input('The second number: '))
    c = int(input('The third number: '))
    if a == b == c:
        print('3')
    elif a == b or b == c:
        print('2')
    else:
        print('0')


min()
