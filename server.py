from flask import Flask
from flask_cors import CORS
import humidity-temperature.py


app = Flask(__name__)
CORS(app)

@app.route("/api/humiditytemp")

def humidity_temp():
    return {"humiditytemp": ["humidity", "temperature"]}

if __name__ == "__main__":
    app.run(debug=True)
