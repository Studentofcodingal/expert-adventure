import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, render_template, request, redirect, url_for, session

from flask_mysqldb import MySQL

import MySQLdb.cursors

import app

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST" and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        mydb = MySQLdb.connect(
            host="remotemyql.com",
            user="Rz8hqnldk4",
            password="nd0wK03xe0",
            database="Rz8hqnldk4")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM LoginDetails WHERE Name = %s and Password = %s", (username, password))
        account = mycursor.fetchone()
        if account:
            print("Login Success")
            name = account[1]
            id = account[0]
            msg = "Logged in Successfully"
            print("Login Success")
            return render_template("Login.html", msg=msg, name=name, id=id)
        else:
            msg = "Incorrect Credentials. Kindly check your Credentials"
            return render_template("Login.html", msg=msg)
    else:
        return render_template("Login.html", msg=msg)