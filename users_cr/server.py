import imp
from flask import Flask, redirect, session, render_template, request
from user import User
app = Flask(__name__)
app.secret_key = "boingBoing"

@app.route('/')
def index():
    users = User.get_all()
    return render_template("index.html", all_users = users)

@app.route('/adduser')
def addUser():
    return render_template('adduser.html')

@app.route('/submit', methods=["POST"])
def submitUser():
    print(request.form)
    User.save(request.form)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)