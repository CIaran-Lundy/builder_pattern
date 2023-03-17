# a module for holding all methods that manage the sorting of characters in a string

def reverse(text: str) -> str:
    return text[::-1]


def alphabetical(text: str) -> str:
    return ''.join(sorted(text))
