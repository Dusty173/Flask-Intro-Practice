# Put your app in here.

from operations import mult, div, add, sub
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add_nums():
    """Add two input nums"""

    x= int(request.args.get('x'))
    y= int(request.args.get('y'))
    output = add(x,y)

    return str(output)

@app.route('/subtract')
def sub_nums():
    """Subtract two input nums"""

    x= int(request.args.get('x'))
    y= int(request.args.get('y'))
    output = sub(x,y)

    return str(output)

@app.route('/divide')
def divide_nums():
    """Divide two input nums"""

    x= int(request.args.get('x'))
    y= int(request.args.get('y'))
    output = div(x,y)

    return str(output)

@app.route('/multiply')
def multiply_nums():
    """Multiply two input nums"""

    x= int(request.args.get('x'))
    y= int(request.args.get('y'))
    output = mult(x,y)

    return str(output)

# Below is the further study section ---

mathfuncs = {
    'add': add,
    'subtract': sub,
    'divide': div,
    'multiply': mult,
}

@app.route('/calc/<operation>')
def do_math(operation):
    """Simpler way to get to mathfuncs and do math"""

    x= int(request.args.get('x'))
    y= int(request.args.get('y'))
    output = mathfuncs[operation](x,y)

    return str(output)