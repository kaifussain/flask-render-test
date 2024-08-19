from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def count_letters():
    data = request.get_json()
    user_input = data.get('userinput', '')
    letter_count = len(user_input)
    return str(letter_count)

if __name__ == '__main__':
    app.run()
