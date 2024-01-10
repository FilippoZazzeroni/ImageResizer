import os
from PIL import Image

def resize_images(input_folder: str, output_folder: str, target_width: int, target_height: int, quality=100):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            img = Image.open(input_path)
            # Calculate new dimensions while maintaining the aspect ratio
            width, height = img.size
            aspect_ratio = width / height

            # Calculate new dimensions based on the target width and height
            new_width = target_width
            new_height = int(target_width / aspect_ratio)

            # Check if the new height is less than the target height
            if new_height < target_height:
                new_height = target_height
                new_width = int(target_height * aspect_ratio)

            resized_img = img.resize((new_width, new_height))
            
            # Calculate cropping box to center the resized image
            left = (new_width - target_width) / 2
            top = (new_height - target_height) / 2
            right = (new_width + target_width) / 2
            bottom = (new_height + target_height) / 2
            
            # Crop the image to the calculated box
            cropped_img = resized_img.crop((left, top, right, bottom))
            
            cropped_img.save(output_path, quality=quality)
            print(f"Resized: {filename} - Original Size: {width}x{height}, New Size: {target_width}x{target_height}")

        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")


def generate_output_folder(input_folder):
    path_parts = input_folder.split(os.path.sep)
    input_folder_name = path_parts[-1]
    path_parts.pop()
    path_parts.append(input_folder_name + "output")
    return os.path.sep.join(path_parts)

def main_pipeline():
    input_folder = input("Enter the path to the input folder containing images: ")
    output_folder = generate_output_folder(input_folder)
    width = int(input("Enter the target width for resizing: "))
    height = int(input("Enter the target height for resizing: "))
    resize_images(input_folder.strip(), output_folder, width, height, 100)
    want_to_continure = input("do you want to load another directory? (y/n) ")
    if want_to_continure == "y":
        main_pipeline()

def main():
    main_pipeline()


    
    

if __name__ == "__main__":
    main()
