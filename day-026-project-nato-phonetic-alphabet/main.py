import pandas

# Read NATO phonetic alphabet CSV file
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        nato_codes = [nato_dict[char] for char in word]
    except KeyError:
        print("Sorry, only letters in the alphabet, please.")
        generate_phonetic()
    else:
        print(nato_codes)


generate_phonetic()
