from flask import flask,jsonify,request
from clasifier import get_prediction
app = Flask(__name__)

@approute("predict-digit", method=["POST"])
def predict_data():
    image = request.files.get("digits")