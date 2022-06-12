from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging
import mlib

app = Flask(__name__)
LOG = create_logger(app)
LOG.set_level(logging.INFO)

@app.route("/")
def home():
    html = f"<h3>Predict the Height From Weight of MLB Players</h3>"
    return html.format(format)

@app.route("/predict", methods=["POST"])
def predict():
    """Predicts the height of MLB Players"""

    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")
    prediction = mlib.predict(json_payload["weight"])
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)