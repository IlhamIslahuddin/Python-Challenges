def caesar_cipher_encode(text, shift):
    global encrypted_text
    encrypted_text = ""
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # Ignore non-alphabetic characters
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decode(text, shift):
    global decrypted_text
    decrypted_text = caesar_cipher_encode(text, -shift)
    return decrypted_text

if __name__ == "__main__":
    shift = 3
    caesar_cipher_encode("xavier.", shift)
    print ("After encryption: "+encrypted_text)
    caesar_cipher_decode(encrypted_text, shift)
    print ("After decryption: "+decrypted_text)
