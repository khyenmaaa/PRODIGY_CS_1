def encrypt(text, shift):
    """Encrypt the text using Caesar Cipher."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            if char.isupper():
                new_char = new_char.upper()
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    """Decrypt the text using Caesar Cipher."""
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? (e/d): ").lower()
        if choice in ['e', 'd']:
            message = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'e':
                result = encrypt(message, shift)
                print(f"Encrypted message: {result}")
            else:
                result = decrypt(message, shift)
                print(f"Decrypted message: {result}")
        else:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
        
        another = input("Do you want to perform another operation? (y/n): ").lower()
        if another != 'y':
            break

main()
