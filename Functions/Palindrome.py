def palindrome(word):
    return word[::-1] == word



def palindrome(word):
    return word[::-1] == word

wording = input("Please type in the word : ")

if palindrome(wording):
    print(f"Yes, the word : {wording} is a palindrome.")
else:
    print(f"No, the word you typed is not a palindrome. ")
