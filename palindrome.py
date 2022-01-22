def is_palindrome(word):
    word=word.lower()
    if(word==word[::-1]):
        return True
    else:
        return False

result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
