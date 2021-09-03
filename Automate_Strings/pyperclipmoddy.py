import pyperclip3

x = pyperclip3.copy("Hello World")

print(pyperclip3.paste(x).decode())
