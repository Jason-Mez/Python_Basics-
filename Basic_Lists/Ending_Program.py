import sys

while True:
    print("Type exit to exit")
    response = input()
    if response == "exit":
        sys.exit() #Just doing to get out of the program early.
    print(f"You typed {response}")
