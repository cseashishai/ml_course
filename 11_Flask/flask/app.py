from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form submit route
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"Hello {name}, your form was submitted!"

# About page
@app.route('/about')
def about():
    return "This is the about page"

# Run app
if __name__ == '__main__':
    app.run(debug=True)