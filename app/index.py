from flask import Flask, render_template, request, redirect
import dao
from app import app, login
from flask_login import login_user,logout_user

from app.models import User


@app.route('/')
def index():
    kw= request.args.get('kw')
    cates = dao.load_categories()
    product = dao.load_products(kw=kw)

    return render_template('index.html',categories=cates, products=product)

@app.route('/admin/login',methods=['post'])
def login_admin():
    username = request.form.get('username')
    password = request.form.get('pwd')

    u = dao.auth_user(username=username, password=password)
    if u:
        login_user(user=u)

    return redirect('/admin')

@login.user_loader
def get_user_by_id(user_id):
    return User.query.get(user_id)

@app.route('/products/<id>')
def details(id):
    return render_template('detail.html')

if __name__=='__main__':
    app.run(debug=True)
