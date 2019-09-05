from PIL import Image, ImageDraw

def draw_border(img_name, top, left, width, height):
    img_path = 'static/img_dl/' + img_name + '.jpg'
    img_file = Image.open(img_path)
    output_image = img_file.copy()
    img_border = ImageDraw.Draw(output_image)
    # the coordinate system is x1, y1, x2, y2 
    # where x1 y1 are coods of top left and x2 y2 are bottom right
    img_border.rectangle((left, top, left + width, top + height), fill=None, outline=(255, 0, 0), width=20)
    output_image.save('static/img_out/' + img_name + '.jpg')
    

# So sample application is 
# draw_border('1567705138', 100, 100, 500, 700)