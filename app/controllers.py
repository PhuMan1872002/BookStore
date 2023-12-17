from flask import Flask, render_template, request, redirect
from flask_login import login_user, logout_user
import dao
from app import app
from app.decorators import annonymous_user

def index():
    kw= request.args.get('kw')
    cates = dao.load_categories()
    cate_id=request.args.get('cate_id')
    product = dao.load_products(kw=kw,cate_id=cate_id)
    return render_template('index.html', categories=cates, products=product)

def details(id):
    return render_template('detail.html')


def login_admin():
    username = request.form.get('username')
    password = request.form.get('pwd')

    u = dao.auth_user(username=username, password=password)
    if u:
        login_user(user=u)

    return redirect('/admin')


def login_my_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)

            n = request.args.get('next')
            return redirect(n if n else '/')

    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)
