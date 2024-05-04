def capitalize(x: str):
    if type(x) != str:
        raise TypeError("Please provide string")
    return x.capitalize()
