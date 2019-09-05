from img_dl import download_image
from img_mods import draw_border
from faceinfo import get_face_data, organize_data

def all_image_details(image_url):
    file_dl = download_image(image_url) # also contains image name
    print('\n' + file_dl + '\n')
    # organize_data is the function and organized_data is the dictionary that stores it
    organized_data = organize_data(get_face_data(image_url)) 
    draw_border(file_dl, organized_data['face_top'], organized_data['face_left'], organized_data['face_w'], organized_data['face_h'])
    return (file_dl, organized_data)
