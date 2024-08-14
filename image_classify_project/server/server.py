from flask import Flask, request, jsonify
import pickle, util
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hi"



@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Starting python Falsk server for house price prediction")
    util.load_saved_artifact()
    app.run(debug=True)
