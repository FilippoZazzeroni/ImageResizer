import os
from PIL import Image

def resize_images(input_folder, output_folder, target_size, quality=95):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Check if the file is a valid image
        try:
            with Image.open(input_path) as img:
                # Check if image size matches the target size
                if img.size != target_size:
                    resized_img = img.resize(target_size)
                    resized_img.save(output_path, quality=quality)
                    print(f"Resized: {filename}")
                else:
                    print(f"Ignored (already correct size): {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

def generate_output_folder(input_folder):
    path_parts = input_folder.split(os.path.sep)
    input_folder_name = path_parts[-1]
    path_parts.pop()
    path_parts.append(input_folder_name + "output")
    return os.path.sep.join(path_parts)

def main():
    input_folder = input("Enter the path to the input folder containing images: ")
    output_folder = generate_output_folder(input_folder)
    width = int(input("Enter the target width for resizing: "))
    height = int(input("Enter the target height for resizing: "))
    target_size = (width, height)
    resize_images(input_folder.strip(), output_folder, target_size, 100)
    
    

if __name__ == "__main__":
    main()
