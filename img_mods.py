import wget
import time

# download file
out_filepath = "img_dl/" + str(time.time()).split('.')[0] + ".jpg"
image_link = 'https://upload.wikimedia.org/wikipedia/commons/3/37/Dagestani_man_and_woman.jpg'
down_file = wget.download(image_link, out=out_filepath)

