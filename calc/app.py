from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def handle_add():
    a = float(request.args.get('a', 0))  # Get 'a' from query parameters, default to 0 if not present
    b = float(request.args.get('b', 0))  # Get 'b' from query parameters, default to 0 if not present
    return str(add(a, b))  # Perform addition and return result as a string

@app.route('/sub')
def handle_sub():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return str(sub(a, b))  # Perform subtraction and return result as a string

@app.route('/mult')
def handle_mult():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return str(mult(a, b))  # Perform multiplication and return result as a string

@app.route('/div')
def handle_div():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 1))  # Default to 1 to avoid division by zero
    if b == 0:
        return "Error: Division by zero"
    return str(div(a, b))  # Perform division and return result as a string

if __name__ == '__main__':
    app.run(debug=True)
