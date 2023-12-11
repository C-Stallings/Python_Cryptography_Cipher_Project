import string


## function passing two variables - 'message' and 'key'
## create translation table
## shift each character three to the left down the alphabet (26 letters in alphabet)
def caesar_encrypt(message, key):
    shift = key % 26
    cipher = str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift],
    )

    encrypted_message = message.lower().translate(cipher)

    return encrypted_message


## function is doing the same as the above one but in reverse and with using 'encrypted_message' and 'key' variables
def caesar_decrypt(encrypted_message, key):
    shift = 26 - (key % 26)
    cipher = str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift],
    )

    message = encrypted_message.translate(cipher)
    return message


message = "Hello My Name Is Charda Stallings"
key = 3


encrypted_message = caesar_encrypt(message, key)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")
