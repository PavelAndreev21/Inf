def ob(arr_1, arr_2):
    s_1, s_2 = set(arr_1), set(arr_2)
    t = s_1 & s_2
    print(len(t))


arr_1 = [3, 10, 2, 6, 8, 89, 99]
arr_2 = [0, 76, 10, 2, 98, 99, 5, 12]


ob(arr_1, arr_2)
