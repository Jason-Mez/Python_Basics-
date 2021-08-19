#Write a program that lets the users type in an integer
#That keeps calling collartz() on the number until that functions returns to the value 1


def collartz(number):
    """
    :param number:
    :return: value of number // 2
    :return: if number entered is odd. (3 * number +1)
    """
    try:
        if number % 2 == 0:
            even = number // 2
            print(even)
            return even
        else:
            odd = (3 * number) + 1
            print(odd)
            return odd
    except ValueError:
        print("Please enter a valid integer")

try:
    user_input = int(input("Enter the number: "))
except ValueError:
    print("Please enter a valid input.")

try:
    while user_input != 1:
        collartz(user_input)
        user_input = collartz(user_input)
except Exception:
    print("An error occured.")






