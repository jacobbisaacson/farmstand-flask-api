from flask import Flask, jsonify
from resources.foods import foods
import models
from flask_cors import CORS

DEBUG=True
PORT=8000

app = Flask(__name__)

CORS(foods, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(foods, url_prefix='/api/v1/foods')

@app.route('/')
def test_route():
  return "Let's fuggin do this!"

@app.route('/test_json')
def get_json():
  return jsonify(
    data="test",
    message="this is a test",
    status=200
  ), 200

@app.route('/test2_json')
def get_json2():
  jacob = {
    'name': 'Jacob',
    'what?': "this is a test on nested json data",
    'number': 30,
    'cute': True
  }
  return jsonify(
    name="Erin",
    what="wife",
    husband=jacob
  )

if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)