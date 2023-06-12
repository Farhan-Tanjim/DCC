from flask import  Flask, request, jsonify


app = Flask(_name_)


@app.route("/")
def hello():
    n = int(input("Input number n: "))
    a = ""
    for num in range(2, 2*n+1, 2):
        if (num%2 == 0) :
            a = a + " "+ str(num)
    return a

if _name_ == "_main_":
    app.run(host="127.0.0.1", port=8082, debug=True)
