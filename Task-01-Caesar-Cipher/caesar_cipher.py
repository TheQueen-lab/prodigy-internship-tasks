def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():  # Only shift letters
            base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decrypt":
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char  # Keep spaces, punctuation unchanged
    return result

# Run the program
print("Welcome to Caesar Cipher")
message = input("Enter your message: ")
shift = int(input("Enter shift value (number): "))
mode = input("Choose mode - encrypt or decrypt: ").lower()

if mode not in ["encrypt", "decrypt"]:
    print("Invalid mode selected.")
else:
    result = caesar_cipher(message, shift, mode)
    print(f"\n{mode.capitalize()}ed message: {result}")
