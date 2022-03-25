from flask import Flask, jsonify, request
from classifier import get_prediction
app = Flask(__name__)
@app.route("/predict-alphabet", methods = ["POST"])
def classify():
  return jsonify({"prediction": get_prediction(request.files.get("alphabet")),}),200

if __name__ == "__main__":
  app.run(debug=True)