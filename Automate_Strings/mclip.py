import pyperclip
import sys
#Python 3
#mclip.py - A multi clip program

TEXT = {"agree": """Yes, i agree. That sounds fine to me.""",
        "busy": "Sorry, can we do that later or next week?",
        "upsell": "Would you consider making this a monthly donation?"
        }

#The arguemet must have no less then 2 arguements.

if len(sys.argv) < 2:
        print("Usage.python mclip.py[keypharse] - copy phrase text")
        print("You have not entered the correct amount of argument.")
        sys.exit()

keyphrase = sys.argv[1] #First command lines in argv.

if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase])
        print(f"The text {keyphrase} -> Copied to clipboard")

else:
        print(f"There is no text for this keyphrase")

