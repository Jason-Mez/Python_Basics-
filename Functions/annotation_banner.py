def banner(text: str = " ", screen_width: int = 80) -> None:  # Do not leave spaces when creating default parameters.
    """

    :param text: Enter text within banner
    :param screen_width: Enter an `int`, widht of banner.
    :return: None
    """
    if len(text) > screen_width - 4:
        raise ValueError(f"The {text} is larger than the specified width {screen_width}")

    if text == "*":
        print("*" * screen_width)
    else:
        cetenred_text = text.center(screen_width - 4)
        output_string = f"**{cetenred_text}**"
        print(output_string)


banner("The text in here is valid")
