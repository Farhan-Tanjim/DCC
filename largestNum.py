from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    print("Input Your List:(space seperated): ")
    numbers = [int(x) for x in input().split()]
    
    print("Input Number n:")
    n = int(input())
    
    if(n-1 >= len(numbers)):
        return "Wrong Input entered"
    else:
        numbers.sort()
        return str(n)+"th largest number from the given list is " + str(numbers[~n])
   

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)