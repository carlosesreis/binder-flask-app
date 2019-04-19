from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Flask App in MyBindeer"

app.run(port=5030)