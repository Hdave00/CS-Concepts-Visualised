# external imports 
import sqlite3
from flask import Flask, flash, redirect, url_for, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_wtf import CSRFProtect
from flask_wtf.csrf import generate_csrf, CSRFError

# local imports 
from helpers import apology, login_required
from forms import LoginForm, RegisterForm
import os
from dotenv import load_dotenv

# Configure application
app = Flask(__name__)

load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Configure session to use filesystem, instead of signed cookies (dont really need cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = False  # True for HTTPS
Session(app)


# TODO- use Flask-WTF for CSRF protection, for all forms using CRUD, refer to npp
app.config['WTF_CSRF_ENABLED'] = True
csrf = CSRFProtect(app)


# disabling caching of responses, to handle the event in case we make a change to save file and the browser does not notice
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return apology(f"CSRF Error: {e.description}", 403)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id, delete the user_id or any other login-specific keys
    session.pop("user_id", None)

    db = sqlite3.connect('project.db')
    db_app = db.cursor()


    form = LoginForm()
    if form.validate_on_submit():
        
        # Ensure username was submitted
            if not form.username.data:
                return apology("must provide username", 400)
            
            elif not form.password.data:
                return apology("must provide password", 400)

            # Query database for username
            # with this query, we will get back is a list of all of the rows that matched out select query
            rows = db_app.execute("SELECT * FROM users WHERE username = ?", (form.username.data,),).fetchall()

            # when we run select query from the dbase, we get back a list of all of the rows that matched our select query
            # Ensure username exists and password is correct
            # remember that rows is a list of tuples, not a list of dictionaries so use rows[0][2] to access the correct column (check schema)
            if len(rows) != 1 or not check_password_hash(
                rows[0][2], form.password.data
            ):
                return apology("invalid username and/or password", 403)

            # Remember which user has logged in
            # user had typed in valid username and password, and we have verified the validity of those values
            # then we can log the user in by using the session variable to keep track of info about current user
            # int [0] to access the id column of the row, since rows is a list of tuples
            session["user_id"] = rows[0][0]
            db.close()

            # Redirect user to home page
            flash("You are logged in!")
            return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html", form=form)
    

# TODO- use flask-wtf on backend change registration form to use Flask-WTF
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # creating new connection to dbase and a new cursor object for multithreading, removes single threading clashes
    db = sqlite3.connect('project.db')
    db_app = db.cursor()

    form = RegisterForm()

    if request.method == "GET":
        # render the registration form
        return render_template("register.html", form=form)

    elif request.method == "POST":

        if form.validate_on_submit():
        
            # delete the user_id or any other login-specific keys
            session.pop("user_id", None)

            # get form data
            # handle username, password and confirm password
            if not form.username.data:
                return apology("Please provide a username", 400)

            elif not form.password.data:
                return apology("Please provide a password", 400)

            elif not form.confirm_password.data:
                return apology("Please confirm password", 400)
            

            # handle an already existing username
            # first check the dbase for usernames that already exist and then compare the user given username with the dbase
            rows = db_app.execute("SELECT * FROM users WHERE username = ?", (form.username.data,),)

            # return apology if "username already exists"
            if len(rows.fetchall()) != 0:
                return apology("username already taken", 400)

            # insert user into dbase
            # we need to access what the user typed in the fields on html page
            username = form.username.data
            password = form.password.data
            hashed_password = generate_password_hash(password)

            # insert a new row into the db with their values
            db_app.execute("INSERT INTO users (username, hash) VALUES (?, ?)", (form.username.data, hashed_password))

            # commit database changes 
            db.commit()

            # log user in: first select the newest user who registered in the dbase, then log them in via session["user_id]
            rows = db_app.execute("SELECT * FROM users WHERE username = ?", (form.username.data,),)
            # in SQLite, the default row factory returns rows as tuples, so we need to use integer indices to access the elements
            # if the id column is the first column in the users table, access it using [0] instead of ["id"]
            session["user_id"] = rows.fetchall()[0][0]

            # close database cursor
            db.close()
            flash("Registered Successfully!")
            return redirect("/")
        
        # form did not validate
        return render_template("register.html", form=form)


@app.route("/logout")
def logout():
    """Log user out"""

    # log out 
    session.pop("user_id", None)

    # Redirect user to login form
    flash("You have logged out!")
    return redirect("/")


@app.route("/")
def index():
    """Show the homepage"""
    return render_template("index.html")

@app.route("/algorithms")
def algorithms():
    """show the algorithms page"""
    return render_template("algorithms.html")

@app.route("/arrays")
def arrays():
    """show the arrays page"""
    return render_template("arrays.html")

@app.route("/commands")
def commands():
    """show the commands page"""
    return render_template("commands.html")

@app.route("/rubberducking")
def rubberducking():
    """ shows rubberducking template """
    return render_template("rubberducking.html")

@app.route("/conditionals")
def conditionals():
    """show the conditionals page"""
    return render_template("conditionals.html")


@app.route("/functions")
def functions():
    """show the functions page"""
    return render_template("functions.html")

@app.route("/loops")
def loops():
    """show the loops page"""
    return render_template("loops.html")

@app.route("/operators")
def operators():
    """show the operators page and handle operators application logic"""

    csrf_token = generate_csrf()
    return render_template("operators.html", csrf_token=csrf_token)

@app.route("/evaluate", methods=["POST"])
def evaluate():
    """handle the operation parameteres"""

    data = request.get_json()
    operand1 = int(data["operand1"])
    operand2 = int(data["operand2"])
    operator = data["operator"]

    if not data["operand1"] or not data["operand2"] or not data["operator"]:
        return jsonify({"error": "nuh uh, dont leave the field empty"}), 400

    # performing the operations
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        if operand2 == 0:
            return jsonify({"error": "Division by zero is not allowed"}), 400
        result = operand1 / operand2
    elif operator == "%":
        result = operand1 % operand2
    elif operator == "==":
        result = operand1 == operand2
    elif operator == "!=":
        result = operand1 != operand2
    elif operator == ">":
        result = operand1 > operand2
    elif operator == "<":
        result = operand1 < operand2
    return jsonify({"result": result})
    

@app.route("/recursion")
def recursion():
    """show the recursion page"""
    return render_template("recursion.html")

@app.route("/types")
def types():
    """show the types page"""
    return render_template("types.html")

@app.route("/variables")
def variables():
    """show the variables page"""
    return render_template("variables.html")


# access the quiz page and handle login requirement
@app.route("/quiz")
@login_required
def quiz():
    return render_template("quiz.html")


# variable visualiser
@app.route('/update_variables', methods=['POST'])
def update_variables():
    data = request.json
    # Log the received variables (or process them further)
    print(f"Received variables: {data}")
    return jsonify({"status": "success", "message": "Variables received!", "data": data})


# submit and process the score
@app.route('/submit_score', methods=['POST'])
@login_required
def submit_score():

    db = sqlite3.connect('project.db')
    db_app = db.cursor()

    data = request.get_json()
    score = data.get('score')
    user_id = session["user_id"]
    db_app.execute("INSERT INTO scores (user_id, score) VALUES (?, ?)", (user_id, score))
    db.commit()
    db.close()
    return redirect(url_for('scores'))


# display the score and also handle login requirement else user cant see scores
# In sqlite3, the parameters for the query are passed as a tuple, which is why user_id is in brackets
@app.route('/scores')
@login_required
def scores():

    db = sqlite3.connect('project.db')
    db_app = db.cursor()

    user_id = session["user_id"]
    scores = db_app.execute("SELECT score FROM scores WHERE user_id = ?", (user_id,))
    scores = db_app.fetchall()
    db.close()
    return render_template("scores.html", scores=scores)



@app.route("/cipher", methods=["GET", "POST"])
def cipher():
    if request.method == "POST":
        key = request.form.get("key")
        plaintext = request.form.get("plaintext")

        # validating that user inputs a key
        if not key:
            error = "Key is required"
            return render_template("cipher.html", error=error)
        if not key.isdigit():
            error = "Key must be a positive integer"
            return render_template("cipher.html", error=error)

        # making sure user inputs plaintext
        if not plaintext:
            error = "Plaintext is required."
            return render_template("cipher.html", error=error)
        k = int(key)

        # generating the cipher text
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                ciphertext += chr(((ord(char) - offset + k) % 26) + offset)
            else:
                ciphertext += char
        return render_template("cipher.html", ciphertext=ciphertext)
    return render_template("cipher.html")


@app.route('/sort')
def sort():
    return render_template('sort.html')



