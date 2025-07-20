from PIL import Image

def encrypt_image(input_path, output_path, key=50):
    img = Image.open(input_path)
    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            # Simple encryption: shift RGB values by key
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, key=50):
    img = Image.open(input_path)
    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            # Decrypt by reversing the encryption
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

# Example usage:
# encrypt_image("original.jpg", "encrypted.png")
# decrypt_image("encrypted.png", "decrypted.png")
