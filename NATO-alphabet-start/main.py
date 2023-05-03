import pandas as pd

NATO_PHONETIC_ALPHABET = "nato_phonetic_alphabet.csv"


def generate_phonetic():
    nato_df = pd.read_csv(NATO_PHONETIC_ALPHABET)
    nato_code = {row.letter: row.code for (index, row) in nato_df.iterrows()}
    word_to_spell = input("Enter a word to get its NATO phonetic code: ").upper()
    try:
        word_nato_code = [nato_code[letter] for letter in word_to_spell]
    except KeyError:
        print("Sorry, the word to spell must only contain letters in the English alphabet!")
        generate_phonetic()
    else:
        print(word_nato_code)


if __name__ == "__main__":
    generate_phonetic()
