def remove_occurrences(lst, value):
    return [x for x in lst if x != value]

list1 = [5, 20, 15, 20, 25, 50, 20]
print(remove_occurrences(list1, 20))