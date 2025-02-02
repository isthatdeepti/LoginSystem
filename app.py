from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "your_secret_key"
bcrypt = Bcrypt(app)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["LoginSystem"]
users_collection = db["users"]

# Home Page (Only accessible after login)
@app.route("/")
def home():
    if "username" in session:
        return render_template("home.html", username=session["username"])
    return redirect(url_for("login"))

# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        user = users_collection.find_one({"username": username})
        
        if user and bcrypt.check_password_hash(user["password"], password):
            session["username"] = username
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password", "danger")
    
    return render_template("login.html")

# Register Page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")

        if users_collection.find_one({"username": username}):
            flash("Username already exists!", "danger")
            return redirect(url_for("register"))

        users_collection.insert_one({"username": username, "password": hashed_pw})
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

# Logout
@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("Logged out successfully!", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
