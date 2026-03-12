# building url
# Variable
# jinja2 Template Engine

'''
{{ }} Expression to print output in html file
{% .. %} Condition statement, loop
{# ... #} comment
'''

from flask import Flask, render_template, request, redirect, url_for

# WSGI Application
app = Flask(__name__)

# Home page
@app.route("/")
def welcome():
    return "<html><h1>Welcome to My Journey</h1></html>"


@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


# Form page
@app.route("/submi", methods=['GET','POST'])
def submi():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


# Result page using dictionary
@app.route('/successers/<int:score>')
def successers(score):
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"

    exp = {'score': score, 'res': res}
    return render_template('result1.html', results=exp)


# if condition example
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html', results=score)


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', results=score)


# Calculate average marks
@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score = 0

    if request.method == 'POST':
        science = float(request.form['science'])
        math = float(request.form['math'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + math + c + data_science) / 4

    return redirect(url_for('successers', score=total_score))


# Entry point
if __name__ == "__main__":
    app.run(debug=True)