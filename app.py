from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is a simple Python Web for Demo Use'


if __name__ == '__main__':
    app.run()
