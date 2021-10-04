# Задание №3
print('---------- 4 ----------')
print('Please enter the number of steps of the triangle: [1,9]')
print('Please enter n - ', sep='', end='')


def tr(n) -> float:
    for i in range(1, n + 1):
        s = ' ' * (n - i)
        for j in range(1, i + 1):
            s += str(j)
        else:
            print(s + s[::-1])


n = int(input())
if n > 9 or n <= 0:
    print('Error')
else:
    tr(n)
