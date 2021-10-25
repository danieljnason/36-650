# question 9 - palindrome
def ispalindrome(word):
    if (not isinstance(word, str)):
        return("Invalid Input")
    if len(word) < 2: 
        return True
    if word[0] != word[-1]: 
        return False
    return ispalindrome(word[1:-1])

print(ispalindrome("kayak"))
print(ispalindrome("hello"))