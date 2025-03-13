from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle

# flask - web kehys (luoda palvelin)
app = Flask(__name__, static_folder="static")
CORS(app, resources={r"/*": {"origins": "*"}})

# lataa sentimenttimalli
with open("sentiment_model.pkl", "rb") as file:
    model = pickle.load(file)

# palauta staattinen HTML-etusivu
@app.route('/')
def home():
    return send_from_directory(app.static_folder, "index.html")

# sentimenttianalyysi-API
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        text = data.get("text", "")

        if not text:
            return jsonify({"error": "No text provided"}), 400

        sentiment = model.predict([text])[0]
        return jsonify({"sentiment": sentiment})

    except Exception as e:
        print(f"Error in prediction: {e}") 
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)
