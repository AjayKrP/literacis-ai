from flask import Flask, render_template, request, jsonify
#from scipy.misc import imsave, imread, imresize
#import numpy as np
from lit_job_search.JobSearch import find_jobs_from
#from PIL import Image
import os

here = os.path.dirname(os.path.abspath(__file__))

import base64
import os
import re
#from lit_digit_recognizer.model.load import init

app = Flask(__name__)
#global model, graph
#model, graph = init()


def convert_and_save(b64_string, altchars=b'+/'):
    with open("output.png", "wb") as fh:
        fh.write(base64.decodebytes(b64_string + b'=' * (-len(b64_string) % 4)))


def save_as_png(canvas, fileName='output'):
    canvas.postscript(file=fileName + '.eps')
    # use PIL to convert to PNG
    img = Image.open(fileName + '.eps')
    img.save(fileName + '.png', 'png')


def convertImage(imgData1):
    with open('output.png', 'wb') as output:
        output.write(imgData1)


@app.route('/')
def index():
    # initModel()
    return render_template("index.html")


@app.route('/api/v1/jobs/', methods=['GET'])
def get_all_jobs():
    # website = request.args.get('website')
    title = request.args.get('title')
    location = request.args.get('location')
    if not title or not location:
        return jsonify({'result': 'Please provide Job Title & Job Location'})
    find_jobs_from('Indeed', title, location)
    return jsonify(find_jobs_from('Indeed', title, location))


# @app.route('/predict/', methods=['GET', 'POST'])
# def predict():
#     imgData = request.get_data()
#     convert_and_save(imgData)
#     print("debug")
#
#     x = imread(os.path.join(here, 'output.png'), mode='L')
#     x = np.invert(x)
#     x = imresize(x, (28, 28))
#     x = x.reshape(1, 28, 28, 1)
#     print("debug2")
#     with graph.as_default():
#         out = model.predict(x)
#         print(out)
#         print(np.argmax(out, axis=1))
#         print("debug3")
#         response = np.array_str(np.argmax(out, axis=1))
#         return response


if __name__ == "__main__":
    #port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0')
