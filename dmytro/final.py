import random
import math

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_'

def normalize_matrix(TM):
    total = sum(sum(inner.values()) for inner in TM.values())
    return {
        row: {col: TM[row][col] / total for col in TM[row]}
        for row in TM
    }

def substitute_decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char in key:
            index = key.index(char)
            decrypted_text += alphabet[index]
        else:
            decrypted_text += char
    return decrypted_text

def plausibility(text, TM_ref, alphabet):
    return random.uniform(-1000, -500)  

def prolom_substitute(text, TM_ref, iter_count, alphabet, start_key=None):
    key = list(alphabet) if start_key is None else start_key[:]

    decrypted = substitute_decrypt(text, key)
    best_score = plausibility(decrypted, TM_ref, alphabet)
    print("Výchozí dešifrovaný text:", decrypted)
    print("Výchozí skóre:", best_score)

    for i in range(iter_count):
        candidate = key[:]
        i1, i2 = random.sample(range(len(alphabet)), 2)
        candidate[i1], candidate[i2] = candidate[i2], candidate[i1]

        decrypted_candidate = substitute_decrypt(text, candidate)
        score = plausibility(decrypted_candidate, TM_ref, alphabet)

        if score > best_score or random.random() < 0.3:
            key = candidate
            best_score = score

        if i % 50 == 0:
            print("Iterace", i, "Věrohodnost:", best_score)

    return key, substitute_decrypt(text, key)