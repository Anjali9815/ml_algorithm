from flask import Flask, request, jsonify
import pickle, util
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hi"


@app.route("/get_locations_names")
def get_locations_names():
    response = jsonify({
        'locations' : util.get_location_name()
    })
    response.headers.add("Access-Control-Allow-Origin", '*')
    return response

@app.route("/predict_house_price", methods = ['POST'])
def predict_house_price():
    total_sqft = float(request.form['total_sqft'])
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    loaction = request.form['location']
    response = jsonify({'estimated_price' : util.get_estimated_price(total_sqft, bath, bhk, loaction)})
    response.headers.add("Access-Control-Allow-Origin", '*')
    return response

if __name__ == '__main__':
    print("Starting python Falsk server for house price prediction")
    util.load_saved_artifact()
    app.run(debug=True)

