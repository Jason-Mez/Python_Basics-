#Aims at building a functions that can determine if a sentence is a palindrome or not.
#Ignore whitespace, commas
#Must only include ----> Alphanumeric char

#examples of palindrome sentences.
# ------> was it a car, or a cat, I saw.
# ------> Do geese see god?
# ------> Desnes not far, Tafton sensed.

def sentence_palindrome(sentence):
    empty_list = []
    for i in sentence:
        if i.isalpha() == True:
            empty_list.append(i.casefold())
    sentence = "".join(empty_list)
    return sentence[::-1] == sentence

print("You will need to create your own palindrome")
pal = input("> ")

if sentence_palindrome(pal):
    print("Yes, you sentence is a palindrome")
else:
    print("No, what you supplied is not a palindrome")

