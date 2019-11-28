def selection(lst):
    i = 0
    for i in range(len(lst)-1):
        j = i+1
        while j < len(lst):
            if lst[i]>lst[j]:
                temp = lst[j]
                lst[j] = lst[i]
                lst[i] = temp
            j += 1

    return lst
