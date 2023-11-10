def is_palindrome(word):
  
    word = word.replace(" ", "").lower()
    
    
    start = 0
    end = len(word) - 1
    
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    
    return True

input_word = "nitin"
result = is_palindrome(input_word)
print(result)  
 
