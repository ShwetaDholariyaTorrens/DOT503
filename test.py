def is_palindrome(word):
    # convert the word to lowercase and remove any spaces
    word = word.lower().replace(" ", "")
  
    # check if the word is equal to its reverse
    return word == word[::-1]


# test the is_palindrome function
print(is_palindrome("racecar")) # True
print(is_palindrome("hello"))   # False
print(is_palindrome("A man a plan a canal Panama"))   # True
