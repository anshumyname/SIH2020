import os
from flask import Flask, request, Response, jsonify, render_template
import cv2
from FaceAction import FaceAction
from PIL import Image
import numpy

app = Flask(__name__)

c1 = 0
c2 = 0
c3 = 0


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response


@app.route('/')
def index():
    return Response(open('./static/local.html').read(), mimetype="text/html")


@app.route('/image', methods=['POST'])
def image():

    image_file = request.files['image']
    image_object = numpy.array(Image.open(image_file).convert('RGB'))
    image_object = image_object[:, :, ::-1].copy()
    drow, yawn, pos = FaceAction().run_frame(image_object)
    print(drow, yawn, pos)
    pos_str = "Looking at screen"
    yawn_str = "Not yawning"
    drow_str = "Not sleeping"

    global c1, c2, c3
    if (pos != 1):
        c3 += 1
    else:
        c3 = 0
    if (c3 > 5):
        pos_str = "Not looking at screen"

    if (yawn > 0.3):
        c2 += 1
    else:
        c2 = 0
    if (c2 > 3):
        yawn_str = "Yawning"

    if (drow < 0.2):
        c1 += 1
    else:
        c1 = 0
    if (c1 > 3):
        drow_str = "Sleeping"

    d = {"drow": drow_str, "yawn": yawn_str, "pos": pos_str}
    return jsonify(d)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',ssl_context='adhoc')
