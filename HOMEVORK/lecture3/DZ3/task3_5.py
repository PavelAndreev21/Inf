# Задание №5
print('---------- 5 ----------')
print('Please enter the number of steps of the rhomb: [1,9]')
print('Please enter n - ', sep='', end='')


def rhom(n: int) -> str:
    for i in range(1, n + 1):
        s = ' ' * (n - i)
        for j in range(1, i + 1):
            s += str(j)
        else:
            print(s + s[::-1])
    for i in range(n - 1, 0, -1):
        s = ' ' * (n - i)
        for j in range(1, i + 1):
            s += str(j)
        else:
            print(s + s[::-1])


n = int(input())
if n > 9:
    print('Error')
else:
    rhom(n)
