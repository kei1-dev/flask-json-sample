from flask import *

app = Flask(__name__)
app.debug = True 

@app.route("/", methods=["POST"])
def odd_even():
    print(request.json["num"])
    return jsonify({"num": request.json["num"]}), 200


if __name__ == "__main__":
    app.run(debug=True)