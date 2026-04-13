from flask import Flask , render_template, redirect,request,url_for ,flash

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/",methods = ["POST","GET"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        if not name:
            flash("name can't be empty")
            return redirect(url_for("home"))
        flash(f"Thank you {name}, your feedback is saved")
        return redirect(url_for("home"))
    return render_template ("home.html")        


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")





