from flask import  Flask, request, jsonify


app = Flask(__name__)


@app.route("/")
def hello():
    n = int(input("Input number n: "))
    a = ""
    for num in range(2, 2*n+1, 2):
        if (num%2 == 0) :
            a = a + " "+ str(num)
    return a

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8082, debug=True)
