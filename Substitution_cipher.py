def get_key_dict(encoded, decode):
    """
    Creates a dictionary of alphabets for encoding
    :param encoded: alphabet of the original text
    :param decode: alphabet for encoding the text
    :return: dictionary representing the change of alphabet
    """
    alphabet_dict = {}
    for i in range(len(encoded)):
        alphabet_dict[encoded[i]] = decode[i]
    return alphabet_dict


def transform(alphabet_dict, text_line):
    """
    using map function to apply an alphabet dictionary to the whole line of text and join it into a string
    :param alphabet_dict: dictionary representing the change in alphabet
    :param text_line: single line of text read from a file to be encoded or decoded
    :return: string of encoded text
    """
    return "".join(list(map(lambda x: alphabet_dict[x], text_line)))


def output(line, output_file):
    """
    writes the encoded line into an output file
    :param line: encoded line to be writen into the output file
    :param output_file: name of a file for the output
    """
    with open(output_file, 'a') as out:
        out.write(line)


def en_decipher(cipher_file, text_file, encode, output_file, default_alphabet):
    """
    main function that reads both file with a cipher key and text file that is to be encoded, afterwards uses other
    functions to create desired outcome
    :param cipher_file: name of a file with a new alphabet for encoding a text
    :param text_file: name of a file with text to be encoded
    :param encode: a boolean determining if the code encodes or decodes the text True for encoding False for decoding
    :param output_file: name of a file for new transformed text
    :param default_alphabet: alphabet, it is included only for the purpose of extending the original 27 letter alphabet
    """
    with open(cipher_file) as ciph_file:
        for line in ciph_file:
            key = line
    if len(key) != len(default_alphabet):
        raise ValueError(f'Length of the cipher ({len(key)}) differs from default alphabet {len(default_alphabet)}!')
    if encode:
        alphabet_dict = get_key_dict(default_alphabet, key)
    else:
        alphabet_dict = get_key_dict(key, default_alphabet)
    with open(text_file) as text:
        for line in text:
            coded_line = transform(alphabet_dict, line)
            output(coded_line, output_file)


def substitute_encrypt(plaintext, key, *, output_file='output.txt', default_alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ_'):
    """
    function for encrypting text, created to be imported by external file
    :param plaintext: name of a file with a new alphabet for encoding a text
    :param key: name of a file with text to be encoded
    :param output_file: optional argument, name of a file for new transformed text
    :param default_alphabet: optional argument, basic alphabet
    """
    en_decipher(plaintext, key, True, output_file, default_alphabet)


def substitute_decrypt(ciphertext, key, *, output_file='output.txt', default_alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ_'):
    """
    function for decrypting text, created to be imported by external file
    :param ciphertext: name of a file with a new alphabet for encoding a text
    :param key: name of a file with text to be encoded
    :param output_file: optional argument, name of a file for new transformed text
    :param default_alphabet: optional argument, basic alphabet
    """
    en_decipher(ciphertext, key, False, output_file, default_alphabet)
