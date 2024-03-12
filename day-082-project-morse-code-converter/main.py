MORSE_CHART = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": '-', "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.", "0": "-----"
}


def encode(string):
    """Convert a String into morse code and return the encoded message also as a String."""
    encoded_message = ""
    words = [word for word in string.split()]
    for word in words:
        for char in word:
            if char in MORSE_CHART:
                encoded_message += MORSE_CHART[char]
            else:
                encoded_message += char

            if word.index(char) != len(word) - 1:
                encoded_message += "   "
        if words.index(word) != len(words) - 1:
            encoded_message += "       "
    return encoded_message


def decode(string):
    """Take a morse code as a String and return the decoded message also as a String."""
    message = ""
    encoded_words = string.split("       ")
    for word in encoded_words:
        chars = word.split("   ")
        for char in chars:
            for key, value in MORSE_CHART.items():
                if char == value:
                    message += key
                    break
        if encoded_words.index(word) != len(encoded_words) - 1:
            message += " "
    return message


if __name__ == "__main__":
    print("================= MORSE CODE CONVERTER =================")
    operation = input("Choose an operation (1. Encode | 2. Decode | 3. Exit): ")

    if operation == "1":
        text = input("Enter text to encode: ").upper()
        print(encode(text))
    elif operation == "2":
        print(">> Use . and - for the code only\n>> Use 3 spaces between characters\n>> Use 7 spaces between words")
        text = input("Enter morse code to decipher (use . or - and a space between letters/numbers): ")
        print(decode(text))
    else:
        print("Exiting program...")