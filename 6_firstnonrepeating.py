def first_non_repeating(str1):

    char_count = {}

    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    for char in str1:
        if char_count[char] == 1:
            return char
    return "Every single character repeats"


print(first_non_repeating("aabbcc"))