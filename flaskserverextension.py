from subprocess import Popen


def load_jupyter_server_extension(nbapp):
    """serve the flask-app directory with flask server"""
    Popen(["python", "./flask-app/main.py"])