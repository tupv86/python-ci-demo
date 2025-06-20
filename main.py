from flask import Flask
import os

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route("/")
def homepage():
    return f"Tổng là: {add(2, 5)}"

if __name__ == "__main__":
    # Railway cấp PORT qua biến môi trường (VD: 8080, 5112, ...)
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
