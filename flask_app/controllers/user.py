from flask import Flask, render_template, request, redirect
from flask_app.models.users import User
from flask_app import app

# ALL USERS/READ
@app.route('/', methods=['GET'])
def display():
    all_users = User.get_all()
    print(all_users)
    return render_template("read.html", users=all_users)

# READ ONE
@app.route('/user/show/<int:id>', methods=['GET'])
def one(id):
    user = User.get_one(id)
    print(user)
    return render_template("one_user.html", user=user)

# UPDATE
@app.route('/edit/<int:id>', methods=['GET'])
def update(id):
    user = User.get_one(id)
    return render_template("edit_user.html", user=user)

@app.route('/edit_user/<int:id>', methods=['POST']) #work on this
def edit(id):
    data = {"id":id, "first_name":request.form['first_name'], "last_name":request.form['last_name'], "email":request.form['email']}
    User.update(data)
    return redirect('/')

# DELETE
@app.route('/remove_user/<int:id>')
def delete(id):
    User.delete(id)
    return redirect('/')

# CREATE
@app.route('/new_user', methods=['GET'])
def form():
    return render_template("create.html")

@app.route('/create_user', methods=['POST'])
def user():
    User.save(request.form)
    return redirect('/')