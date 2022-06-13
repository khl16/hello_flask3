import numbers
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/Play')
def index1():
    
    return render_template("index.html")
    
    
@app.route('/Play/<number>')
def index2(number):
    
    return render_template("index1.html",num_times=int(number) )	# notice the 2 new named arguments!











if __name__=="__main__":
    app.run(debug=True)