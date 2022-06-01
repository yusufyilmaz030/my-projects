from flask import Flask, render_template
from numpy import var

app = Flask(__name__)



@app.route("/")
def head():
    return render_template("index.html", number1=30, number2=55)

@app.route("/mult")
def number():
    var1, var2 = 30, 70
    return render_template("body.html", num1 = var1, num2 = var2, multiplication = var1*var2)



if __name__== "__main__":
    app.run(debug=True)