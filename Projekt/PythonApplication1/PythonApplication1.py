from PIL import Image
import os


current_directory = os.getcwd()


folder_name = "attack"


folder_path = os.path.join(current_directory, folder_name)


target_folder_name = "attackv1"
target_folder_path = os.path.join(current_directory, target_folder_name)
if not os.path.exists(target_folder_path):
    os.makedirs(target_folder_path)


file_list = os.listdir(folder_path)


target_width = 115
target_height = 65


for file_name in file_list:
    if file_name.endswith('.jpg') or file_name.endswith('.png') or file_name.endswith('.jpeg'):
        
        image_path = os.path.join(folder_path, file_name)
        image = Image.open(image_path)
        
       
        current_width, current_height = image.size
        
        left = (current_width - target_width) // 2 + 13
        top = (current_height - target_height) // 2
        right = left + target_width
        bottom = top + target_height
        
        cropped_image = image.crop((left, top, right, bottom))
        

        cropped_image.save(os.path.join(target_folder_path, file_name))

print("Za")
