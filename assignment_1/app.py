from flask import Flask, jsonify

app = Flask(__name__, static_folder="public", static_url_path="/public")

@app.route("/")
def home():
    return "Hello, world! Flask is running 🚀"

@app.route("/api/v1/cat")
def get_cat():
    cat = {
        "cat_id": "507f1f77bcf86cd799439011",
        "name": "Mittens",
        "birthdate": "2022-03-01",
        "weight": 4.3,
        "owner": "64fa1e7df9b22cd11234890a",
        "image": "https://place-hold.it/320x240&text=Cat"
    }
    return jsonify(cat)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)
