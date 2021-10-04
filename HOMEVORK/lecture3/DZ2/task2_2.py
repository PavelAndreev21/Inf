def min():
    a = int(input('The first number: '))
    b = int(input('The second number: '))
    c = int(input('The third number: '))

    if a == b == c:
        print(a, '=', b, '=', c)
    elif a < b and a < c:
        print('Min: ', a)
    elif b < a and b < c:
        print('Min: ', b)
    else:
        print('Min: ', c)


min()
