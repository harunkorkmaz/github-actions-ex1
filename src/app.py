import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'hello world', 200

if __name__ == "__main__":
    app.run()
