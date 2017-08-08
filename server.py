import base64
import tf.convert
import tf.recognize
from flask import Flask, render_template, request

APP = Flask(__name__, static_folder='static', static_url_path="")

variables = tf.recognize.load()

@APP.route('/', methods=['GET', 'POST'])
def index():
    """index"""
    if request.method == 'GET':
        return render_template('index.html')
    else:
        image_data = request.json['image'].replace("data:image/png;base64,", "")
        t = open("image.png", "wb")
        convert = base64.b64decode(image_data)
        t.write(convert)
        t.close()
        tf.convert.convert()
        result = tf.recognize.recognize(x = variables[0], y = variables[1], keep_prob = variables[2], sess = variables[3])
        return result
