import secrets
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="A python script for generating random passphrases",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--word_nb",
        type=int,
        default=4,
        help="The number of words in the generated passphrase."
    )
    parser.add_argument(
        "--word_list",
        type=str,
        default="eff_wordlist.txt",
        help="Path to the file containing the list of words used for\
        generating the passphrase. The file should have one word per line."
    )
    args=parser.parse_args()
    with open(args.word_list, 'r') as f:
        words_str = f.read()
        
    wordlist = words_str.split("\n")

    print("Using "+str(len(wordlist))+" words")

    # choose list of words
    for i in range(args.word_nb):
        print(secrets.choice(wordlist))

if __name__ == "__main__":
    main()