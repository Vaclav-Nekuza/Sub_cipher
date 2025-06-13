import random
import math

def load_bigram_matrix(filename):
    """
    Loads a bigram frequency matrix from a file into a nested dictionary.
    :param filename: name of the file containing bigram frequencies in the format "XY:count"
    :return: dictionary representing the bigram frequency matrix
    """
    TM_ref = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            pair, count = line.strip().split(":")
            count = int(count)
            a, b = pair[0], pair[1]
            if a not in TM_ref:
                TM_ref[a] = {}
            TM_ref[a][b] = count
    return TM_ref

def normalize_matrix(TM_ref):
    """
    Converts a frequency-based bigram matrix into a relative probability matrix.
    :param TM_ref: frequency-based bigram matrix (dictionary)
    :return: normalized matrix with relative probabilities
    """
    TM_rel = {}
    for a in TM_ref:
        total = sum(TM_ref[a].values())
        TM_rel[a] = {}
        for b in TM_ref[a]:
            TM_rel[a][b] = TM_ref[a][b] / total
    return TM_rel

def substitute_decrypt(ciphertext, key, alphabet):
    """
    Substitutes characters in the ciphertext according to the given key.
    :param ciphertext: text to be decrypted
    :param key: list representing a permutation of the alphabet
    :param alphabet: original alphabet (used for mapping)
    :return: decrypted text string
    """
    char_map = {key[i]: alphabet[i] for i in range(len(key))}
    return ''.join(char_map.get(char, char) for char in ciphertext)

def plausibility_calculation(TM_ref):
    """
    Converts a bigram frequency matrix to a log-probability matrix.
    :param TM_ref: relative bigram frequency matrix
    :return: tuple of log-probability matrix and minimum log probability
    """
    log_probs = {}
    min_log_prob = math.log(1e-10)
    for a in TM_ref:
        log_probs[a] = {}
        for b in TM_ref[a]:
            log_probs[a][b] = math.log(TM_ref[a][b])
    return log_probs, min_log_prob

def plausibility(text, log_probs, min_log_prob):
    """
    Calculates a plausibility score for a given text based on bigram log-probabilities.
    :param text: text to be evaluated
    :param log_probs: bigram log-probability matrix
    :param min_log_prob: minimal fallback probability for unseen bigrams
    :return: float value representing total plausibility score
    """
    score = 0.0
    for i in range(len(text) - 1):
        a, b = text[i], text[i + 1]
        score += log_probs.get(a, {}).get(b, min_log_prob)
    return score

def prolom_substitute(text, TM_ref, iter_count, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ_', start_key=None):
    """
    Performs probabilistic hill-climbing search to break a substitution cipher.
    :param text: ciphertext to be decrypted
    :param TM_ref: bigram relative frequency matrix
    :param iter_count: number of iterations to perform
    :param alphabet: original alphabet used for mapping
    :param start_key: optional starting permutation of the alphabet
    :return: tuple containing the best decryption key and decrypted text
    """
    key = list(alphabet) if start_key is None else start_key[:]
    if start_key is None:
        random.shuffle(key)

    log_probs, min_log_prob = plausibility_calculation(TM_ref)

    decrypted = substitute_decrypt(text, key, alphabet)
    best_score = plausibility(decrypted, log_probs, min_log_prob)
    best_key = key[:]

    current_score = best_score
    no_improvement_count = 0

    EARLY_STOP_THRESHOLD = 5000
    RESET_THRESHOLD = 1000

    for i in range(iter_count):
        temperature = (1.0 - (i / iter_count)) ** 2

        candidate = key[:]
        i1, i2 = random.sample(range(len(alphabet)), 2)
        candidate[i1], candidate[i2] = candidate[i2], candidate[i1]

        decrypted_candidate = substitute_decrypt(text, candidate, alphabet)
        score = plausibility(decrypted_candidate, log_probs, min_log_prob)

        if score > current_score:
            current_score = score
            key = candidate[:]
            if current_score > best_score:
                best_score = current_score
                best_key = key[:]
                no_improvement_count = 0
                print(f"Iter {i}: New best score -> {best_score:.2f}")
            else:
                no_improvement_count += 1
        elif temperature > 0 and random.random() < math.exp((score - current_score) / temperature):
            current_score = score
            key = candidate[:]
            no_improvement_count += 1
        else:
            no_improvement_count += 1

        if no_improvement_count > RESET_THRESHOLD:
            key = best_key[:]
            current_score = best_score

        if no_improvement_count > EARLY_STOP_THRESHOLD:
            print(f"Early stopping at iteration {i} due to no improvement in best_score.")
            break

    return best_key, substitute_decrypt(text, best_key, alphabet)

def open_file(Text):
    """
    Opens and reads the full content of a given text file.
    :param Text: name of the file to be read
    :return: string containing the full file content
    """
    output = ''
    with open(Text) as text:
        for line in text:
            output += line
    return output

def save_key_to_file(key):
    """
    Saves the decryption key to a file named 'key.txt'.
    :param key: string representing the final decryption key
    """
    with open("key.txt", "w") as keyfile:
        keyfile.write(key)

def save_decrypted_text_to_file(decrypted_text):
    """
    Saves the decrypted text to a file named 'decrypted.txt'.
    :param decrypted_text: string containing the final decrypted output
    """
    with open("decrypted.txt", "w") as decryptedfile:
        decryptedfile.write(decrypted_text)

def main(tm_ref_name, iter, Text):
    """
    Main function for decrypting substitution cipher using a bigram model and heuristic search.
    :param tm_ref_name: name of the file containing bigram frequency matrix
    :param iter: number of iterations for heuristic search
    :param Text: name of the file containing the ciphertext
    """
    tm_ref = load_bigram_matrix(tm_ref_name)
    tm_rel = normalize_matrix(tm_ref)
    ciphertext = open_file(Text)
    print(f"Loaded ciphertext: {ciphertext[:100]}...")
    key, plaintext = prolom_substitute(ciphertext, tm_rel, iter)
    print("\n----------RESULTS----------")
    print(f"Found Key: {''.join(key)}")
    print(f"Decrypted Text: {plaintext}")

    print("Saving decrypted text to file...")
    save_decrypted_text_to_file(plaintext)
    print("Saving key to file...")
    save_key_to_file(key)
    print("Done.")
