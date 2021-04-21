def banner_test(text):
    """
    Return text that user enters.

    :param text:
    :return:Text you entered in a neatly formatted banner
    """
    screen_width = 80
    if len(text) > screen_width:
        print("EEK!")
        print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = f"**{text.center(screen_width - 4)}**"
        print(output_string)
