from Substitution_cipher import encrypt, decrypt
from bigram.bigram import main as bigram_main
from mHAlgorithmCypherCrack import main as crack_main


def main():
    encrypt("text_1000_sample_1_key.txt", "text_1000_sample_1_plaintext.txt")
    decrypt("text_1000_sample_1_key.txt", "output.txt", output_file="decrypted_output.txt")
    bigram_main("bigram_out.txt")
    crack_main("bigram_out.txt", 20000, 'output.txt')
    # bigram_main('krakatit.txt', output_file="bigram_out.txt")
    # print(f'book_bigram ({book_bigram})')
    # print(f'encoded_bigram ({encoded_bigram})')
    # crack_main(book_bigram, encoded_bigram, 'output.txt')
    # decrypt("text_1000_sample_1_key.txt", "output.txt", output_file="decrypted_output.txt")

if __name__ == "__main__":
    main()
