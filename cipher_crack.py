def print_cracked_cipher(cipher_output_file, alphabet_dict):
    bigram = []
    with open(cipher_output_file, "w") as matrix:
        for line in matrix:
            bigram.append(line[0]+line[1])
    return bigram

"""
def trd_crack(alphabet_dict, book_bigram, book_bigram_index, encoded_bigram, encoded_bigram_index):
    matrix = []
    for book_pair in book_bigram:
        alphabet_dict[]
"""


def recursive_crack(alphabet_dict, book_bigram, book_bigram_index, encoded_bigram, encoded_bigram_index):
    # book_bigram =    [E_, A_, I_, _S, _P, O_, ...]
    # encoded_bigram = [DA, VA, AY, MA, AR, PA, ...]
    # what should i do if first pairs are wrong??
    if book_bigram[book_bigram_index][0] in alphabet_dict.keys():
        if alphabet_dict[book_bigram[book_bigram_index][0]] == encoded_bigram[encoded_bigram_index][0] and \
                book_bigram_index != len(book_bigram)-1:
            if book_bigram[book_bigram_index][1] in alphabet_dict.keys():
                if alphabet_dict[book_bigram[book_bigram_index][1]] == encoded_bigram[encoded_bigram_index][1] and \
                        encoded_bigram_index != len(encoded_bigram)-1:
                    return recursive_crack(alphabet_dict,
                                           book_bigram, book_bigram_index+1,
                                           encoded_bigram, 0)
                elif encoded_bigram_index == len(encoded_bigram)-1:
                    if book_bigram_index == len(book_bigram)-1 and len(alphabet_dict) == 27:
                        return alphabet_dict
                    elif book_bigram_index == len(book_bigram)-1 and len(alphabet_dict) != 27:
                        return recursive_crack({},
                                               book_bigram[1:], 0,
                                               encoded_bigram, 0)
                    else:
                        return recursive_crack(alphabet_dict,
                                               book_bigram, book_bigram_index+1,
                                               encoded_bigram, 0)
                else:
                    return None
            else:
                if encoded_bigram[encoded_bigram_index][1] not in alphabet_dict.values():
                    alphabet_dict[book_bigram[book_bigram_index][1]] = encoded_bigram[encoded_bigram_index][1]
                    return recursive_crack(alphabet_dict,
                                           book_bigram, book_bigram_index+1,
                                           encoded_bigram, encoded_bigram_index+1)
                                            # not necessary to compare to previous pair
                else:
                    pass # ?????
        elif book_bigram_index == len(book_bigram)-1:
            return alphabet_dict  ##
        else:
            return recursive_crack(alphabet_dict,
                                   book_bigram, book_bigram_index+1,
                                   encoded_bigram, encoded_bigram_index)
    else:
        alphabet_dict[book_bigram[book_bigram_index][0]] = encoded_bigram[encoded_bigram_index][0]  #
        return recursive_crack(alphabet_dict, book_bigram, book_bigram_index, encoded_bigram, encoded_bigram_index)    #



def crack(alphabet_dict, book_bigram, encoded_bigram):
    for book_pair in book_bigram:
        for encoded_pair in encoded_bigram:
            if book_pair[0] in alphabet_dict.keys():
                if alphabet_dict[book_pair[0]] == encoded_pair[0]:
                    continue
                else:
                    break
            else:
                alphabet_dict[book_pair[0]] = encoded_pair[0]
            if book_pair[1] in alphabet_dict.keys():
                if alphabet_dict[book_pair[1]] == encoded_pair[1]:
                    continue
                else:
                    break
            else:
                alphabet_dict[book_pair[1]] = encoded_pair[1]
    return alphabet_dict


def main(book_bigram, encoded_bigram, cracked_cifer_file):
    alphabet_dict = {}
    alphabet_dict = crack(alphabet_dict, book_bigram, encoded_bigram)
    print_cracked_cipher(cracked_cifer_file, alphabet_dict)


# if __name__ == "__main__":
#     main("bigram_out.txt", "output.txt")
