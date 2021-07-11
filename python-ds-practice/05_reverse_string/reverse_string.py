def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    phrase_li = list(phrase)
    phrase_li.reverse()
    return "".join(phrase_li)
