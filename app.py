from flask import Flask, request

app = Flask(__name__)


@app.route('/healthCheck')
def health_check():
    return "running"


if __name__ == "__main__":
    app.run(debug=True)
