from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def addition():
    """Adds a and b."""
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    
    return str(add(a, b))

@app.route('/sub', methods=['GET'])
def subtraction():
    """Subtracts b from a."""
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    
    return str(sub(a, b))

@app.route('/mult', methods=['GET'])
def multiplication():
    """Multiplies a and b."""
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    
    return str(mult(a, b))

@app.route('/div', methods=['GET'])
def division():
    """Divides a by b."""
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)

    return str(div(a, b))

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)





