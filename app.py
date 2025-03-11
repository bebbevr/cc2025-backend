from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world from cc backend</>"

@app.route('/data', methods=['POST'])
def get_data():
    data = request.json
    print(data["name"])
    return {"message": "Data received", "data": data}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)