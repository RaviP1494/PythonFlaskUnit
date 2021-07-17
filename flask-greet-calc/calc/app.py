from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_view_func():
    """Adds two numbers passed in query string as 'a' and 'b'"""
    try:
        #extracts operands from query string
        num1 = request.args['a']
        num2 = request.args['b']

        #converts operands from string to int
        num1 = int(num1)
        num2 = int(num2)

        #adds operands together using function in operations.py
        ans = add(num1,num2)

        #returns final answer converted to string
        return str(ans)

    except Exception as err:
        return str(err)


@app.route('/sub')
def sub_view_func():
    """Subtracts two numbers passed in query string as 'a' and 'b'"""
    try:
        #extracts operands from query string
        num1 = request.args['a']
        num2 = request.args['b']

        #converts operands from string to int
        num1 = int(num1)
        num2 = int(num2)

        #subtracts operands together using function in operations.py
        ans = sub(num1,num2)

        #returns final answer converted to string
        return str(ans)

    except Exception as err:
        return str(err)


@app.route('/mult')
def mult_view_func():
    """Multiplies two numbers passed in query string as 'a' and 'b'"""
    try:
        #extracts operands from query string
        num1 = request.args['a']
        num2 = request.args['b']

        #converts operands from string to int
        num1 = int(num1)
        num2 = int(num2)

        #multiplies operands together using function in operations.py
        ans = mult(num1,num2)

        #returns final answer converted to string
        return str(ans)

    except Exception as err:
        return str(err)


@app.route('/div')
def div_view_func():
    """Divides two numbers passed in query string as 'a' and 'b'"""
    try:
        #extracts operands from query string
        num1 = request.args['a']
        num2 = request.args['b']

        #converts operands from string to int
        num1 = int(num1)
        num2 = int(num2)

        #divides operands together using function in operations.py
        ans = div(num1,num2)

        #returns final answer converted to string
        return str(ans)

    except Exception as err:
        return str(err)


@app.route('/math/<oper>')
def math_view_func(oper):
    """Generalized view function that uses path variable to respond dynamically to different routes of add, sub, mult, and div"""
    try:
        #extracts operands from query string
        num1 = request.args['a']
        num2 = request.args['b']

        #converts operands from string to int
        num1 = int(num1)
        num2 = int(num2)

        #divides operands together using function in operations.py
        ans = eval(f"{oper}({num1},{num2})")

        return str(ans)

    except Exception as err:
        return str(err)