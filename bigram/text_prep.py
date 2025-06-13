def prep(line):
    """
    prepares single line of text to be compatible with required alphabet (removes all unwanted characters and changes
    the rest to uppercase)
    :param line: single line of text
    :return: single line of text (string) that is compatible with the required alphabet
    """
    prep_dict = {
        'Á': 'A', 'A': 'A', 'B': 'B', 'Č': 'C', 'C': 'C', 'Ď': 'D', 'D': 'D', 'Ě': 'E', 'É': 'E', 'Ę': 'E', 'E': 'E',
        'F': 'F', 'G': 'G', 'H': 'H', 'Í': 'I', 'Î': 'I', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'Ň': 'N',
        'N': 'N', 'Ó': 'O', 'Ö': 'O', 'O': 'O', 'P': 'P', 'Q': 'Q', 'Ř': 'R', 'R': 'R', 'Š': 'S', 'S': 'S', 'Ť': 'T',
        'T': 'T', 'Ú': 'U', 'Ů': 'U', 'Ü': 'U', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Ý': 'Y', 'Y': 'Y', 'Ž': 'Z',
        'Ţ': 'Z', 'Z': 'Z', ' ': '_', '0': '', '1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '',
        '9': '', '\n': '', ',': '', '‚': '', '?': '', '.': '', ':': '', '!': '', '*': '', '(': '', ')': '', '=': '',
        '-': '', '_': '', '%': '', '„': '', '“': '', ';': '', '…': '', '—': '', '"': '', "'": '', '&': '', '°': '',
        '•': '', '‘': '', '’': '', '§': '', '/': '',
    }
    # '': '',
    line = line.upper()
    return "".join(list(map(lambda x: prep_dict[x], line)))