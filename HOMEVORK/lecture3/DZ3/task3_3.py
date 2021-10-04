# Задание №3
print('---------- 3 ----------')
print('Please enter the number of steps of the ladder')
print('Please enter n - ', sep='', end='')


def lesenca(n) -> float:
    c = 0
    while n > 0:
        c += 1
        n -= 1
        s = ''
        for j in range(1, c + 1):
            s += str(j)
        else:
            print(s)


n = int(input())
if n <= 0:
    print('Error')
else:
    lesenca(n)

