def find_common(lst1, lst2):
    
    common_elements = list(set(lst1) & set(lst2))
    return common_elements

print(find_common([1, 2, 3, 4], [3, 4, 5, 6]))