from flask import Flask,render_template
'''
it creat an instance of the flask  class
which will be your WSGI( Web server getway interface) apllication
'''
### WSGI Apllication
app=Flask(__name__) # __name__ to understand file loction when i creted folder to access

# Basic rout  point
@app.route("/")      # "/" basically of home page and hit this and print "wlcome to flask on web home page"
def welcome():
    return "<html> <H1> wlcome to the My Journy </H1> </html>" 

@app.route("/index")   # when you call server to use /index and what any fuction to call use this own name   
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

# Entery point of any.py file
if __name__=="__main__":
    app.run(debug=True)  # debug =True refere befor comment to after changes are save in host