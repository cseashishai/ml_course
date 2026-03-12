from flask import Flask,render_template,request
'''
rander_tamplate are use to the creat a tamplte folder and inner creat a html
file and run on the web
'''
### WSGI Apllication
app=Flask(__name__) 

# Basic rout  point
@app.route("/")      # "/" basically of home page and hit this and print "wlcome to flask on web home page"
def welcome():
    return "<html> <H1> wlcome to the My Journy </H1> </html>" 

@app.route("/index",methods=['GET'])    
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form",methods=['GET','POST']) # here 'POST' is use to send to server request
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name} ! '
    return render_template('form.html')

# Entery point of any.py file
if __name__=="__main__":
    app.run(debug=True)  
