from flask import Flask, render_template, request, redirect, url_for, session
import app
from flask_mysqldb import MySQL
@app.route("/logout")
def logout():
    name = ""
    id = ""
    msg = "Logged out Successfully"
    return render_template("Login.html", msg=msg, name=name, id=id)