def insertion_sort(lst):

    for sorted_element in range(len(lst)-1):
        i = 0
        current_element = sorted_element+1
        if lst[current_element] < lst[sorted_element]:
            while i < current_element:
                s = lst[current_element]
                if s <= lst[i]:
                    s = lst.pop(current_element)
                    lst = lst[:i] + [s] + lst[i:]
                i += 1
    return lst
