import requests # imports the requests library that allows us to send HTTP requests in Python and its useful for interacting with web APIs

from flask import redirect, render_template, session, flash
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    # the escape function, assigned a variable s,
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """
    # is a functiontools module that helps preserve the original function's metadata
    @wraps(f)
    # defines a new function that takes any no:of arguments and keyword arguments
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            flash("Please login or register to access the quiz and quiz scores.")
            return redirect("/login")
        # if the user is logged in, the original function f, is called with its arguments
        return f(*args, **kwargs)

    return decorated_function
