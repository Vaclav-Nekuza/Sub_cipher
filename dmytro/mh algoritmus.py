import random
from substitute_decrypt import substitute_decrypt
from plausability import plausibility


def prolom_substitute(text, TM_ref, iter_count, alphabet, start_key=None):
    # výchozí klíč
    key = list(alphabet) if start_key is None else start_key[:]

    # dešifrování a výpočet skóre
    decrypted = substitute_decrypt(text, key)
    best_score = plausibility(decrypted, TM_ref, alphabet)
    print("Výchozí dešifrovaný text:", decrypted)
    print("Výchozí skóre:", best_score)

    # hledání lepšího klíče
    for i in range(iter_count):
        candidate = key[:]
        i1, i2 = random.sample(range(len(alphabet)), 2)
        candidate[i1], candidate[i2] = candidate[i2], candidate[i1]

        decrypted_candidate = substitute_decrypt(text, candidate)
        score = plausibility(decrypted_candidate, TM_ref, alphabet)

        if score > best_score or random.random() < 0.3:
            key = candidate
            best_score = score

        # výpis
        if i % 50 == 0:
            print("Iterace", i, "Věrohodnost:", best_score)

    # Výstup - nejlepší klíč a jeho dešifrovaný text
    return key, substitute_decrypt(text, key)