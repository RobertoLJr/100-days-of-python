from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(text_input, key, encryption_operation):
    text_output = ""

    if encryption_operation == "decode":
        key *= -1

    for char in text_input:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + key
            text_output += alphabet[new_position]
        else:
            text_output += char

    print(f"Here's the {encryption_operation}d result: {text_output}")


print(logo)
should_end = False
while not should_end:
    operation = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    user_text = input("Type your message:\n").lower()
    shift_key = int(input("Type the shift number:\n"))
    shift_key %= len(alphabet)

    caesar(user_text, shift_key, operation)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
