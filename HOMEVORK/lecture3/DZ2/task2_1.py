def min():
    a = int(input('The first number: '))
    b = int(input('The second number: '))
    if a == b:
        print(a, '=', b)
    elif a > b:
        print('Min: ', b)
    else:
        print('Min: ', a)


min()
