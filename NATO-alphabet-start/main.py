import pandas as pd
from pprint import pprint

if __name__ == "__main__":
    nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

    nato_code = {row.letter: row.code for (index, row) in nato_df.iterrows()}

    while True:
        word_to_spell = input("Enter a word to get its NATO phonetic code: ").upper()
        if word_to_spell == "EXIT":
            break
        word_nato_code = [nato_code[letter] for letter in word_to_spell]
        print(word_nato_code)
    print("Exit Program!")
