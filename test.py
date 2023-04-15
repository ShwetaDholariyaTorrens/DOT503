def is_palindrome(word):
    # convert the word to lowercase and remove any spaces
    word = word.lower().replace(" ", "")
  
    # check if the word is equal to its reverse
    return word == word[::-1]


