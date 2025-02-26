def longestword_in_asentence(sentence):
    
    words = sentence.split()
    return max(words, key=len)
    
print(longestword_in_asentence("Minha felicidade é ver você felizzzz"))
        
