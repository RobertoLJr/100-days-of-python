import pandas

# Read NATO phonetic alphabet CSV file
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Get user input
word = input("Enter a word: ").upper()

# Create a dictionary from created DataFrame
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# Create a list of NATO codes for each character in word
nato_codes = [nato_dict[char] for char in word]

print(nato_codes)
