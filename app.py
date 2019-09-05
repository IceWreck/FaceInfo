from flask import Flask, render_template, request
from wrap_up import all_image_details
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == "POST":
        try:
            image_url = request.form.get("imagelink")
            img_loc = 'img_out/' + all_image_details(image_url)[0] + '.jpg'
            print(img_loc)
            return render_template('output.html', img_loc=img_loc)
        except Exception as e:
            print(e)
    else:
        return render_template('input.html')

