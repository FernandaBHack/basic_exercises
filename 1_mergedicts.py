def merged_dicts(dict1, dict2):
    
    merged = dict1|dict2
    
    return merged

print(merged_dicts({'a': 1, 'b' : 2},{'b': 3, 'c' : 4}))
