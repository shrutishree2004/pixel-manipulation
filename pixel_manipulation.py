from PIL import Image

# Helper function to ensure RGB values remain within [0, 255]
def clamp(value):
    return max(0, min(255, value))

# Encryption function that sets all pixels to black (for visual encryption)
def encrypt_image(input_path, output_path):
    try:
        # Open the image
        img = Image.open(input_path)
        pixels = img.load()  # Load the pixel data
        
        # Get image dimensions
        width, height = img.size
        
        # Traverse through each pixel and set it to black
        for x in range(width):
            for y in range(height):
                # Set every pixel to black (0, 0, 0)
                pixels[x, y] = (0, 0, 0)
        
        # Save the encrypted image
        img.save(output_path)
        print(f"Image encrypted and saved as {output_path}. It will appear as a blank image until decrypted.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Decryption function to restore the original pixel values from the encrypted image
def decrypt_image(original_path, encrypted_path, output_path):
    try:
        # Open the original and encrypted images
        original_img = Image.open(original_path)
        encrypted_img = Image.open(encrypted_path)
        original_pixels = original_img.load()  # Load the pixel data of the original image
        encrypted_pixels = encrypted_img.load()  # Load the pixel data of the encrypted image
        
        # Get image dimensions
        width, height = encrypted_img.size
        
        # Traverse through each pixel and restore the original pixel values
        for x in range(width):
            for y in range(height):
                # Restore original pixel values from the original image
                encrypted_pixels[x, y] = original_pixels[x, y]
        
        # Save the decrypted image
        encrypted_img.save(output_path)
        print(f"Image decrypted and saved as {output_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to get user input
def main():
    try:
        # Get input from the user
        original_image_path = input("Enter the path of the original image to encrypt: ")
        encrypted_output_path = input("Enter the output path for the encrypted image: ")
        decrypted_output_path = input("Enter the output path for the decrypted image: ")
        
        # Encrypt the image by setting it to black
        encrypt_image(original_image_path, encrypted_output_path)
        
        # Decrypt the image by restoring the original pixel values
        decrypt_image(original_image_path, encrypted_output_path, decrypted_output_path)
    
    except ValueError as e:
        print(f"Error: {e}. Please enter valid input.")

# Run the main function
if __name__ == "__main__":
    main()
