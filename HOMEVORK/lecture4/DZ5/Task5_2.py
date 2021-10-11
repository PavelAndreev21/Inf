arr = input('Enter the list items separated by a space').split()


def bol(arr: list) -> list:
    bi = []
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            bi.append(arr[i])
    else:
        print(bi)


bol(arr)
