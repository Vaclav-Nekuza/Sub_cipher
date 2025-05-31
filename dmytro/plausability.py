import math


def plausibility(text, TM_ref, alphabet):
    score = 0
    for i in range(len(text) - 1):
        a, b = text[i], text[i + 1]
        if a in alphabet and b in alphabet:
            score += math.log(TM_ref[a][b])
    return score
