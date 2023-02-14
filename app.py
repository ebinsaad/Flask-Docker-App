from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello COMP4110 from Jenkins, Flask, and Docker at Git 11</h1>'


if __name__ == "__main__":
    app.run(debug=True)
