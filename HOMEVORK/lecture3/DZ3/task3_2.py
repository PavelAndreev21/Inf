# Задание №2
print('---------- 2 ----------')
a = []
print('This program is designed to count zero elements')
print('Please enter the number of array elements')
n = int(input())
print('Please enter the array elements line by line')
for i in range(1, n + 1):
    print('a[', i, '] - ', sep='', end='')
    a.append(int(input()))
    print('Intermediate array value')
    print(a)
    print('----------')


def calc_zeros(a) -> float:
    n = 0
    for i in a:
        if i == 0:
            n += 1
    return n


b = calc_zeros(a)
print('The result of the program -', b)
