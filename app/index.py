import math

from flask import Flask, render_template, request, redirect,session,jsonify
import dao
from app import app,login,controllers
from flask_login import login_user,logout_user
from app.models import Category, Product, User




app.add_url_rule('/', 'index', controllers.index)
app.add_url_rule('/products/<int:id>', 'details', controllers.details)
app.add_url_rule('/admin/login', 'login-admin', controllers.login_admin(), methods=['post'])
app.add_url_rule('/login', 'login-user', controllers.login_my_user, methods=['get', 'post'])





@login.user_loader
def get_user_by_id(user_id):
    return User.query.get(user_id)

if __name__=='__main__':
    from app import admin
    app.run(debug=True)
