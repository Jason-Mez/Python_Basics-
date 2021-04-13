#Script that shows if what you are typing in is a palindrom or not. 
def palindrome(word):
    return word[::-1] == word #Evaluates to True or False. 

wording = input("Please type in the word : ")

if palindrome(wording):
    print(f"Yes, the word : {wording} is a palindrome.")
else:
    print(f"No, the word you typed is not a palindrome. ")
