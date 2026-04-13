from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template(
        "login.html" , 
        name = "Akash",
        is_topper = True,
        subjects = ["maths","english","science"]
        )