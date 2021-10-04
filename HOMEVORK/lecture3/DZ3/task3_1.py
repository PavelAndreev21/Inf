# Task №1
print('---------- 1 ----------')
a = []
n = 10
print('This program is designed to calculate the sum of 10 array elements')
print('Please enter the array elements line by line')
for i in range(1, n + 1):
    print('a[', i, '] - ', sep='', end='')
    a.append(int(input()))
    print('Intermediate array value')
    print(a)
    print('----------')


def massive_sum(a: list) -> int:
    c = 0
    for i in a:
        c += i
    return c


b = massive_sum(a)
print('The result of the program -', b)
