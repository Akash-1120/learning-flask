from flask import Flask, redirect,request,session ,url_for,Response
app = Flask(__name__)
app.secret_key = "Password123"

@app.route("/" , methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        Password = request.form.get("Password")

        if username == "admin" and Password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))

        else:
            return Response ("In-valid credentials",mimetype="text/plain")
    return ''' 
            <h2>Login Page</h2>
            <form method = "POST">
            Username : <input type = "text" name = "username"><br>
            Password : <input type = "text" name = "Password"><br>
            <input type= "submit" value= "login">
            </form>

'''
#wellcome page after login 

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>welcome {session["user"]} !</h2>
        <a href= {url_for("logout")}>logout</a>
    '''
    return redirect (url_for("login"))


#logout page

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))


