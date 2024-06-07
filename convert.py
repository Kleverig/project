from PIL import Image
import os

def convert_png_to_jpg(input_path, output_path):
    with Image.open(input_path) as img:
        rgb_img = img.convert('RGB')
        rgb_img.save(output_path, format='JPEG')

def find_and_convert_image(file_name):
    current_directory = os.getcwd()
    for root, _, files in os.walk(current_directory):
        if file_name in files:
            input_path = os.path.join(root, file_name)
            output_path = os.path.splitext(input_path)[0] + '.jpg'
            convert_png_to_jpg(input_path, output_path)
            print(f"Конвертація завершена! Зображення збережено за адресою {output_path}")
            return
    print(f"Файл {file_name} не знайдено у директорії {current_directory}.")

if __name__ == "__main__":
    file_name = input("Введіть назву файлу (включно з .png розширенням), який потрібно конвертувати: ")
    find_and_convert_image(file_name)