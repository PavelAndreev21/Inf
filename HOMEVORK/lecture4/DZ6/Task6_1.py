def DICTIONARY(dir, key):
    print(dir.get(key))


dir = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7
}

key = str(input())
DICTIONARY(dir, key)
