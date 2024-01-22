PLACEHOLDER = "[name]"

# Get the names from invited_names.txt file as a list
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Replace every PLACEHOLDER value from the original list with each name from the 'names' list and write a new file
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/Letter-to-{stripped_name}.txt", "w") as invitation_file:
            invitation_file.write(new_letter)
