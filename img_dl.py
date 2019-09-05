import wget
import time

def download_image(image_link):
    img_name = str(time.time()).split('.')[0]
    out_filepath = "static/img_dl/" + img_name + ".jpg"
    down_file = wget.download(image_link, out=out_filepath)
    return img_name

# Usage
# print(download_image('https://upload.wikimedia.org/wikipedia/commons/3/37/Dagestani_man_and_woman.jpg'))
# Returns just the filename without path or extension