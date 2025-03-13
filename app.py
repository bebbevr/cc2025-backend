from flask import Flask, request, jsonify
import pickle

app = Flask (__name__)

# lataa sentimenttimalli
with open("sentiment_model.pkl", "rb") as file:
    model = pickle.load(file)

# sentimenttianalyysi-API
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    sentiment = model.predict([text])[0]
    return jsonify({"sentiment": sentiment})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)
