import time, sys

indent = 0 #How manyspace to indent.
indentIncreasing = True


try:
    while True:
        print(" "* indent, end="")
        print("*******")
        time.sleep(0.1) #Pause for 1 / 10 of a second
        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
