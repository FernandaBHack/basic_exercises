import unicodedata

def counts_upper_case(str1):
    count_char = 0
    
    for char in str1:
        if char.isupper() and unicodedata.category(char).startswith("L"):
            count_char += 1
            
    return count_char

print(counts_upper_case("Fernanda Brognoli Hack - Coder"))