from PIL import Image
import numpy as np

def encode_image_to_pixels(image_path, key, file_name, file_format):
    # Open the input image
    img = Image.open(image_path).convert('RGB')
    width, height = img.size

    # Convert image to numpy array
    img_array = np.array(img)

    key= np.resize(key, img_array.shape)

    encoded_array = np.bitwise_xor(img_array.reshape(-1, 3), key.reshape(-1, 3))

    # Create new image with a single row of pixels
    encoded_img = Image.new('RGB', (encoded_array.shape[0], encoded_array.shape[1]))
    encoded_img.putdata([tuple(pixel) for pixel in encoded_array])

    # Save encoded image
    encoded_img.save (f"encoded_{file_name}.{file_format}")
    print(f"Encoded image saved to encoded_{file_name}.{file_format}")
    return f"encoded_{file_name}.{file_format}"    


def decode_pixels_to_image(encoded_image_path, key, file_name, file_format):
    # Open the encoded image
    encoded_img = Image.open(encoded_image_path).convert('RGB')

    # Convert image to numpy array
    encoded_array = np.array(encoded_img)
    
    decoded_array = np.bitwise_xor(encoded_array.reshape(-1, 3), key)

    # Create a new image from the decoded array
    decoded_img = Image.fromarray(decoded_array.astype('uint8'), 'RGB')

    # Save the decoded image
    decoded_img.save(f"decoded_{file_name}.{file_format}")
    print(f"Decoded image saved to decoded_{file_name}.{file_format}")    


def main():
    print("Pixel-level Image Encoder/Decoder")
    image_path = input("Enter the path of the image to encode: ")
    key_value = int(input("Enter an integer key for encoding/decoding: "))
    file_name = input("Choose name for the encoded image: ")
    file_format = input("Choose format for the encoded image (e.g., png, jpg, jpeg): ").lower()
    
    key = np.random.randint(0, 256, size=(1, 1, 3)) * key_value

    encoded_path = encode_image_to_pixels(image_path, key, file_name, file_format)
    decode_pixels_to_image(encoded_path, key, file_name, file_format)


key=125

main()
