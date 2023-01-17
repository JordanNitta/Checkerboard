from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", rows=8, cols=8, color_one='red', color_two='black')

@app.route('/<int:x>')
def row(x):
    return render_template("index.html", rows=x, cols=8, color_one='red', color_two='black')

@app.route('/<int:x>/<int:y>')
def row_col(x, y):
    return render_template("index.html", rows=x, cols=y, color_one='red', color_two='black')

@app.route('/<int:x>/<int:y>/<string:one>')
def change_color_one(x, y, one):
    return render_template("index.html", rows=x, cols=y, color_one=one, color_two='black')

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def change_all_color(x, y, one, two):
    return render_template("index.html", rows=x, cols=y, color_one=one, color_two=two)

if __name__=="__main__":
    app.run(debug=True)