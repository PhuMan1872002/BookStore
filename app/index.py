from flask import Flask, render_template, request, redirect
import dao
from app import app

@app.route('/')
def index():
    kw= request.args.get('kw')
    cates = dao.load_categories()
    product = dao.load_products(kw=kw)

    return render_template('index.html',categories=cates, products=product)
@app.route('/products/<id>')
def details(id):
    return render_template('detail.html')

if __name__=='__main__':
    app.run(debug=True)
