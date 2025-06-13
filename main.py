from Substitution_cipher import substitute_encrypt, substitute_decrypt
from bigram.bigram import get_bigram as bigram_main
from mHAlgorithmCypherCrack import main as crack_main


def main():
    fileNameToDecrypt = 'bigram/Testovaci_soubory/text_1000_sample_20_ciphertext.txt'
    # alphabet = 'UDOBNLGSZPEFHRYWVKJTAIXQ_MC'
    # encrypt(fileNameToDecrypt, fileNameToDecrypt)
    # decrypt(fileNameToDecrypt, "output.txt", output_file="decrypted_output.txt")
    bigram_main("bigram_out.txt")
    crack_main("bigram_out.txt", 20000, fileNameToDecrypt)

if __name__ == "__main__":
    main()
