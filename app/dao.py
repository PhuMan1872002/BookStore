from app.models import Category,Product,User
import hashlib
from app import db
from sqlalchemy import func
def load_categories():
    return Category.query.all()


def load_products(kw=None,cate_id=None):
     products=Product.query

     if kw:
        products=products.filter(Product.name.contains(kw))

     if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

     return products.all()

def get_product_by_id(product_id):
    return Product.query.get(product_id)


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()

def count_product_by_cate():
    return db.session.query(Category.id, Category.name, func.count(Product.id))\
             .join(Product, Product.category_id.__eq__(Category.id), isouter=True)\
             .group_by(Category.id).all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

if __name__ == '__main__':
    from app import app
    with app.app_context():
        print(count_product_by_cate())
