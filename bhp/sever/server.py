# from flask import Flask, request, jsonify
# app = Flask(__name__)






# if __name__ == "__main__":
#     print("Starting python Falsk server for house price prediction")
#     app.run()

from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# # Load your trained model
# with open('model.pkl', 'rb') as model_file:
#     model = pickle.load(model_file)

@app.route('/predict')
def predict():
    # data = request.json
    # features = [data['feature1'], data['feature2'], data['feature3']]  # Adjust based on your features
    # prediction = model.predict([features])
    # return jsonify({'prediction': prediction[0]})
    return "hi"

if __name__ == '__main__':
    app.run()
