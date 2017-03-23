def encrypt(text,rot):
    """Encrypts a text by rotation assignment"""

    enc_text = ""

    for l in str(text):
        new_letter = rotate_character(l, rot)
        enc_text += new_letter

    return enc_text


def alphabet_position(char):
    "Assigns character a position of 1-26."

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    char = char.lower()
    if char.isalpha() and char in alphabet:
        return alphabet.index(char)

    else: return char



def rotate_character(char, rot):
    """Re-assigns a new character to a character."""

    encrypted = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if char.isalpha() and char in alphabet:
        rotated_index = alphabet_position(char)+ rot
        if rotated_index < 26:
            encrypted = encrypted + alphabet[rotated_index]
        else:
            encrypted = encrypted + alphabet[rotated_index % 26]
    elif char.isalpha() and char in upper_alphabet:
        rotated_index = alphabet_position(char) + rot
        if rotated_index < 26:
            encrypted = encrypted + upper_alphabet[rotated_index]
        else:
            encrypted = encrypted + upper_alphabet[rotated_index % 26]
    else:
        encrypted = encrypted + char

    return encrypted
