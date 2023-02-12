from flask import Flask, render_template, request, redirect
from flask_app.models.users import User
from flask_app import app

@app.route('/display_all', methods=['GET'])
def display():
    users = User.get_all()
    print(users)
    return render_template("read.html", users=users)

@app.route('/new_user', methods=['GET'])
def form():
    return render_template("create.html")

@app.route('/create_user', methods=['POST'])
def user():
    User.save(request.form)
    return redirect('/display_all')