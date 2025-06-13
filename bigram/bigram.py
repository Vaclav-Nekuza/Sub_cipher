from bigram.text_prep import prep


def bigram(prepared_line, bigram_dict):
    """
    analyses single line of text and dissects it into a dictionary of pairs of letters as key and records number of
    occurrences as a value
    :param prepared_line: single line of text, that has been reduced to contain only required letters
    :param bigram_dict: dictionary of bigrams and number of their occurrences
    :return: cumulative dictionary record of bigram occurrences
    """
    for i in range(0, len(prepared_line)-1):
        couple = prepared_line[i] + prepared_line[i+1]
        if couple in bigram_dict:
            bigram_dict[couple] = bigram_dict[couple] + 1
        else:
            bigram_dict[couple] = 1
    return bigram_dict


def print_bigram_matrix(bigram_dict, out_file):
    """
    Optional function for keeping records
    Writes down bigram occurrence dictionary into a file
    :param bigram_dict: dictionary of bigrams and number of their occurrences
    :param out_file: filename of the file for the dictionary of bigrams
    """
    with open(out_file, 'w') as out:
        for couple in bigram_dict.keys():
            print(f"{couple}: {bigram_dict[couple]}")
            out.write(f"{couple}:{bigram_dict[couple]}\n")


def main(text_file, *, output_file=None):
    """
    main function for creating a dictionary of bigrams and number of their occurrences
    reads the required file and uses other functions to process it
    :param text_file: filename of the file with text for processing into bigrams
    :param output_file: filename of the file for the dictionary of bigrams
    :return: list of bigrams in descending order by their occurrence
    """
    bigram_dict = {}
    # UTF-8
    # windows-1252
    with open(f"{text_file}", encoding='windows-1250') as text:
        for line in text:
            if line != "\n":
                prepared_line = prep(line)
                bigram_dict = bigram(prepared_line, bigram_dict)
    # sorts the dictionary by the number of uses of bigrams in descending order
    bigram_dict = {key: value for key, value in sorted(bigram_dict.items(), key=lambda item: item[1], reverse=True)}
    if output_file is not None:
        print_bigram_matrix(bigram_dict, output_file)
    return list(bigram_dict.keys())


