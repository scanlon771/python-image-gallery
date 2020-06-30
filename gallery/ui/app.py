from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

from ..data.user import User
from ..data.postgres_user_dao import PostgresUserDAO
from ..data.db import connect

app = Flask(__name__)

connect()


def get_user_dao():
    return PostgresUserDAO()

@app.route('/admin/deleteUser/<username>')
def executeDeleteUser(username):
    get_user_dao().delete_user(username)
    return  redirect('admin/users')

@app.route('/admin/deleteUser/<username>')
def deleteUser(username):
    return render_template("confirm.html", title="Confirm delete", message="Are you sure you want to delete this user", on_yes="/admin/executeDeleteUser/"+username, on_no="/admin/users")

@app.route('/users')
def users():
    return render_template('users.html', users=get_user_dao().get_users())
