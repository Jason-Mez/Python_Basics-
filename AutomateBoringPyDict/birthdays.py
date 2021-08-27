
birthdays = {"Alice": "Apr 1",
             "Bob": "Dec 12",
             "Carol": "Mar 4",
             }

while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == "":
        break

    if name in birthdays:
         print(f"{name} birthday is on {birthdays[name]}")
    else:
        print(f"I do not have bithday information of : {name}")
        print("What is their Birthday")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated.")


