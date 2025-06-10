from Substitution_cipher import encrypt, decrypt
from bigram.bigram import main as bigram_main
from mHAlgorithmCypherCrack import main as crack_main


def main():
    book_bigram = bigram_main('valka s mloky.txt')
    encoded_bigram = bigram_main('output.txt')
    crack_main(book_bigram, encoded_bigram, 'output.txt')
    # bigram_main('valka s mloky.txt', output_file="bigram_out.txt")
    # encrypt("text_1000_sample_1_key.txt", "text_1000_sample_1_plaintext.txt")
    # decrypt("text_1000_sample_1_key.txt", "output.txt", output_file="decrypted_output.txt")


if __name__ == "__main__":
    main()
