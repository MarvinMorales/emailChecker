from math import degrees
from flask import Flask
from flask_cors import CORS
from controllers.emailChecker import checker
from utils.encrypter import generateKeys

# generateKeys()
app = Flask(__name__)
CORS(app)

app.register_blueprint(checker)

if __name__ == "__main__":
   app.run(host="127.0.0.1", port=10000, debug=True)
