def bubble(lst):
    len_lst = len(lst)
    i = 1
    while i < len_lst:
        j = 0

        while j < i:

            a = lst[i]
            b = lst[j]

            if a < b:
                lst[i] = b
                lst[j] = a
            j+=1
        i+=1

    return lst
