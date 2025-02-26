def is_palindrome(str1):
    
    str1 = str1.lower().replace(" ", "")
    str_reversed = str1[::-1]
    
    if str1 == str_reversed:
        return True
    return False
    
print(is_palindrome("Arara"))