#Write a function called collartz()
#THat has parameter, called number
#print number // 2
#return value
# if the value is odd, the collartz should print return (3 * number +1)d

def collartz(number: int):
    """
    :param number:
    :return: value of number // 2
    :return: if number entered is odd. (3 * number +1)
    """
    if number % 2 == 0:
        even = number // 2
        print(even)
        return even
    else:
        odd = (3*number) + 1
        print(odd)
        return odd


first_try = collartz(3) #trying with an odd number
print(first_try)

second_try = collartz(2) #Trying with an even number
print(second_try)

