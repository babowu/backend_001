from flask import Flask, jsonify, send_from_directory
import json
import random

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/poem')
def get_poem():
    with open('poem.json', 'r', encoding='utf-8') as f:
        poem_list = json.load(f)
    return jsonify(random.choice(poem_list))


@app.route('/audio/<filename>')
def get_audio(filename):
    return send_from_directory('static', filename)


if __name__ == '__main__':
    app.run(port=80)
