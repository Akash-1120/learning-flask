from flask import Flask, render_template , request
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit" , methods = ["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    valid_user = {
        "admin" : "password",
        "akash" : "yadav",
        "sanskriti" : "yadav"
       }
    if username in valid_user  and password == valid_user[username] :
        return render_template("welcome.html",name = username)
    else:
        return "fuck you motherfucker"


