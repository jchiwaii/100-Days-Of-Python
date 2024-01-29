alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(text, shift, direction):
    cipher_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index + shift) % len(alphabet)
            cipher_text += alphabet[new_index]
        else:
            cipher_text += char
    return cipher_text

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    result = cipher(text, shift, direction)
    print(f"The {direction}d text is {result}")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart.lower() != 'yes':
        break
