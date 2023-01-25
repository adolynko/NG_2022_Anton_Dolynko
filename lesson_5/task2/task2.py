from flask import Flask, render_template, request

app = Flask("Calculator")


def result( number1:int, number2:int, sign:str):
    match sign:
        case "+":
            result = number1 + number2
        case "-":
            result = number1 - number2
        case "*":
            result = number1 * number2
        case "/":
            result = number1 / number2
        case "^":
            result = number1 ** number2
        case "sqrt":
            result = number1 ** (1/number2)
        case _:
            result = 'Error'
    return result

@app.route('/')
def start():
    try:
        if request.method == "GET":
            number1 = int(request.args.get("first_num"))
            number2 = int(request.args.get("second_num"))
            operation = request.args.get("operation")
    except:
        number1 = 0
        number2 = 0
        operation = "-"
    return render_template("index.html", result=result(number1, number2, operation))

app.run(port=8080)