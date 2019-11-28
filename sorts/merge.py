from math import floor


def merge(array):
    length = len(array)
    result_array = []
    if length > 1:
        a = merge(array[:floor(length/2)])
        b = merge(array[floor(length/2):])

        len_a = len(a)
        len_b = len(b)

        i = 0
        j = 0

        while i < len_a and j < len_b:
            current_element_a = a[i]
            current_element_b = b[j]
            if current_element_a < current_element_b:
                result_array.append(current_element_a)
                i += 1
            else:
                result_array.append(current_element_b)
                j += 1
        for t in range(i, len_a):
            result_array.append(a[t])

        for r in range(j, len_b):
            result_array.append(b[r])

        return result_array
    else:
        return array
