from bigram.text_prep import prep


def get_bigrams(text, bigram_dict):
    """
    Updates the bigram dictionary with bigrams found in the given text.
    :param text: preprocessed string from which bigrams are extracted
    :param bigram_dict: dictionary where bigram frequencies are stored
    :return: updated bigram dictionary
    """
    for i in range(0, len(text) - 1):
        couple = text[i] + text[i + 1]
        if couple in bigram_dict:
            bigram_dict[couple] += 1
        else:
            bigram_dict[couple] = 1
    return bigram_dict


def print_bigram_matrix(bigram_dict, out_file):
    """
    Prints and saves the bigram frequency matrix to a file.
    :param bigram_dict: dictionary with bigram frequencies
    :param out_file: output file path where the matrix will be saved
    """
    with open(out_file, 'w') as out:
        for couple in bigram_dict.keys():
            print(f"{couple}: {bigram_dict[couple]}")
            out.write(f"{couple}:{bigram_dict[couple]}\n")


def main(text_file, *, output_file=None):
    """
    Loads a text file, extracts and counts bigrams using preprocessing.
    Optionally writes the result to a file or returns sorted bigrams.

    :param text_file: path to the input text file
    :param output_file: optional path to save the resulting bigram matrix
    :return: list of bigrams sorted by frequency (if output_file is None)
    """
    bigram_dict = {}
    try:
        with open(text_file, 'r', encoding='windows-1250') as text:
            for line in text:
                if line != "\n":
                    prepared_line = prep(line)
                    bigram_dict = get_bigrams(prepared_line, bigram_dict)

        # Sorts bigrams by frequency in descending order
        bigram_dict = {
            key: value
            for key, value in sorted(bigram_dict.items(), key=lambda item: item[1], reverse=True)
        }

    except FileNotFoundError:
        print(f"Error: Input file not found at '{text_file}'")
        return None

    if output_file is not None:
        print_bigram_matrix(bigram_dict, output_file)
    else:
        return list(bigram_dict.keys())

# if __name__ == '__main__':
#     main('valka s mloky.txt')
