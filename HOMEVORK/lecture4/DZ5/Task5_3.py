arr = input('Enter the list items separated by a space').split()


def mm(arr: list) -> list:
    mini = arr.index(max(arr))
    maxi = arr.index(min(arr))
    arr[maxi], arr[mini] = arr[mini], arr[maxi]
    print(arr)


mm(arr)
