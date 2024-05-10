def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.

    If the sentence is empty, the first character should be None.
    """
    if sentence:
        length = len(sentence)
        first_char = sentence[0]
    else:
        length = 0
        first_char = None
    
    return (length, first_char)
