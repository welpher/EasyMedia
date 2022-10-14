from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<div>hello.world!asdfas</div>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
