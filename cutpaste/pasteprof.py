import cv2
from PIL import Image

def pastef(profile_path, passport_path, output_path):
    # Load images
    profile_image = Image.open(profile_path)
    passport_image = Image.open(passport_path)

    # Get dimensions of the images
    profile_width, profile_height = profile_image.size
    passport_width, passport_height = passport_image.size

    # Calculate the new height to maintain the aspect ratio
    new_height = min(profile_height, passport_height)

    # Resize images
    profile_image = profile_image.resize((int(profile_width * (new_height / profile_height)), new_height))
    passport_image = passport_image.resize((int(passport_width * (new_height / passport_height)), new_height))

    # Create a new image with the combined width and the maximum height
    combined_width = profile_image.width + passport_image.width
    combined_height = new_height
    combined_image = Image.new('RGB', (combined_width, combined_height))

    # Paste profile image on the left
    combined_image.paste(profile_image, (0, 0))

    # Paste passport image on the right
    combined_image.paste(passport_image, (profile_image.width, 0))

    # Save the result
    combined_image.save(output_path)
