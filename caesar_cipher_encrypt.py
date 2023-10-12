def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

def main():
    while True:
        print("Caesar Cipher Encryption and Decryption")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            plaintext = input("Enter the plaintext: ")
            shift = int(input("Enter the shift value (0-25): "))
            encrypted_text = caesar_cipher_encrypt(plaintext, shift)
            print("Encrypted Text:", encrypted_text)
        elif choice == "2":
            ciphertext = input("Enter the ciphertext: ")
            shift = int(input("Enter the shift value (0-25): "))
            decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
            print("Decrypted Text:", decrypted_text)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()




