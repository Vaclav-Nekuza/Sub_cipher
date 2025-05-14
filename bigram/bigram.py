from bigram.text_prep import prep


def bigram(prepared_line, bigram_dict):
    for i in range(0, len(prepared_line)-1):
        couple = prepared_line[i] + prepared_line[i+1]
        if couple in bigram_dict:
            bigram_dict[couple] = bigram_dict[couple] + 1
        else:
            bigram_dict[couple] = 1
    return bigram_dict


def print_bigram_matrix(bigram_dict, out_file):
    with open(out_file, 'w') as out:
        for couple in bigram_dict.keys():
            print(f"{couple}: {bigram_dict[couple]}")
            out.write(f"{couple}:{bigram_dict[couple]}\n")


def main(text_file, *, output_file=None):
    bigram_dict = {}
    with open(f"{text_file}", encoding='UTF-8') as text:
        for line in text:
            if line != "\n":
                prepared_line = prep(line)
                bigram_dict = bigram(prepared_line, bigram_dict)
    # sorts the dictionary by the number of uses of bigrams in descending order
    bigram_dict = {key: value for key, value in sorted(bigram_dict.items(), key=lambda item: item[1], reverse=True)}
    if output_file is not None:
        print_bigram_matrix(bigram_dict, output_file)
    else:
        return list(bigram_dict.keys())

# if __name__ == '__main__':
#     main('valka s mloky.txt')

