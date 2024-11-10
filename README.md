# Pixel Manipulation: Image Encryption and Decryption

This project provides basic image manipulation scripts using Python's PIL (Pillow) library to simulate image encryption and decryption.

## Overview

The code offers two main functionalities:

1\. **Encrypting an Image** - By setting all pixel values to black, an image is visually "encrypted," appearing as a blank image.

2\. **Decrypting an Image** - Restores the original pixel values using the original image, thereby "decrypting" the previously encrypted image.

## Requirements

- Python 3.x

- Pillow library

You can install the required library using:

```bash

pip install pillow

```

## Usage

### Encrypting an Image

To encrypt an image, call the `encrypt_image` function with the path to the input image and specify an output path for the encrypted image.

```python

from pixel_manipulation import encrypt_image

# Example usage

encrypt_image("input_image.jpg", "encrypted_image.jpg")

```

### Decrypting an Image

To decrypt an image, call the `decrypt_image` function with paths to the original image, the encrypted image, and an output path for the decrypted image.

```python

from pixel_manipulation import decrypt_image

# Example usage

decrypt_image("original_image.jpg", "encrypted_image.jpg", "decrypted_image.jpg")

```

## Functions

- **encrypt_image(input_path, output_path)**: Encrypts an image by setting all pixel values to black, simulating a visually blank image.

- **decrypt_image(original_path, encrypted_path, output_path)**: Decrypts an image by restoring the pixel values from the original image to the encrypted image.

## Notes

- The `decrypt_image` function requires both the original and encrypted images to work correctly.

- Both functions handle image paths and use the PIL library for pixel-level manipulation.

## License

This project is open-source and available under the MIT License.
