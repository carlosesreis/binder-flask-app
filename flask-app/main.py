from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Flask App in MyBinder"

app.run(port=5030)