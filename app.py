from flask import Flask, request,session 
from flask import render_template
import random

app = Flask(__name__)
app.secret_key="something"


@app.route("/")
def index():
    return render_template('index.html', title='HomePage')


@app.route("/css2")
def css2():
    return render_template("level_two.html")

@app.route("/css3")
def css3():
    return render_template("level_three.html")

@app.route("/css4")
def css4():
    return render_template("level_four.html")

@app.route("/css5")
def css5():
    return render_template("level_five.html")


#older stuff below ===========================

@app.route("/rand")
def randomnumber():
  i = random.randrange(100)
  return render_template("lucky.html",number = i)

# example of static content
# like an image or including css
@app.route("/image")
def image_css():
  return render_template("image.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/test")
def test():
    return "<h1>This is a test page </h1>"

@app.route("/blog")
def blog():
    user = {'username': 'Miguel'}
    posts =[
    {
      'author': {'username': 'John'},
       'book':'Beautiful Day in Portland!'
    }
           ]
    return render_template('blog.html', title='HomePage', user=user, posts=posts)
'''
@app.route("/login")
def login():
    return render_template('login.html', title='Sign In', form=form)
'''


@app.route("/login",methods=['GET','POST'])
def form_demo():
  # GET is when we just load the page in our browser
  # POST is when we click the button 
  if request.method=="GET":
    return render_template("login.html")
  else:
    # here we clicked the button
    # so we can check the form data
    name = request.form['username']
    pw = request.form['password']
    print(name,pw)
    if pw != "12345":
      error = "Password unknown. Try again"
      name=""
    else: 
      error = ""
    return render_template("login.html",error=error, name=name)

@app.route("/session")
def session_demo():
  print(session)
  if 'count' not in session:
    session['count'] = 1
  else:
    session['count'] = session['count'] + 1

  return render_template('session.html',count = session['count'])


    
app.run(host="0.0.0.0",port=5000,debug=True)