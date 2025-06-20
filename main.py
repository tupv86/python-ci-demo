from flask import Flask

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route("/")
def homepage():
    return f"Tổng là: {add(2, 5)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
