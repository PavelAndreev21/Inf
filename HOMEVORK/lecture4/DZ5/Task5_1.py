arr = input('Enter the list items separated by a space').split()


def chet(arr: list) -> list:
    mas = []
    for i in range(1, len(arr), 2):
        mas.append(arr[i])
    else:
        print(mas)


chet(arr)
