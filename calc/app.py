# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def use_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = add(a, b)
    return str(answer)

@app.route('/sub')
def use_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = sub(a,b)
    return str(answer)

@app.route('/mult')
def use_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = mult(a,b)
    return str(answer)

@app.route('/div')
def use_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = div(a,b)
    return str(answer)

operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}    

@app.route('/math/<equate>')
def use_operation(equate):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = operations[equate](a,b)
    return str(answer)

