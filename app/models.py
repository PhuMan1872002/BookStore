import enum
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from app import db
from sqlalchemy import Column,Integer,String,ForeignKey,Float,Boolean,Enum
class UserRoleEnum(enum.Enum):
    Employee = 1
    Customer=2
    ADMIN = 3



class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100),
                    default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.Customer)

    def __str__(self):
        return self.name

class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    price = Column(Float, default=0)
    image = Column(String(100),
                   default='https://reviewmaydocsach.com/wp-content/uploads/2022/08/cai-dung-cua-thanh-nhan-nguyen-duy-can.jpg')
    active = Column(Boolean, default=True)
    quantity=Column(Integer, default=0)
    author_name=Column(String(50), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

if __name__=='__main__':
    from app import app
    with app.app_context():
        db.create_all()
        c1 = Category(name='Sách tâm lý')
        c2 = Category(name='Sách giáo dục')
        c3 = Category(name='Sách tài chính')
        p1 = Product(name='Predictably Irrational', price=210000,quantity=10, author_name='Dan Ariely',category_id=1)
        p2 = Product(name='How Pschycology Works', price=250000,quantity=12,author_name='Jo Hemmings', category_id=1)
        # # # p3 = Product(name='Cái dũng của thánh nhân', auhor='Nguyễn Duy Cần',price=240000, category_id=2)
        # # # p4 = Product(name='Toán học cao cấp', auhor='Trần Trung Kiệt',price=290000, category_id=2)
        p5 = Product(name='Finance Wheel', price=25000,quantity=12,author_name='Johnson Nick', category_id=3)
        # db.session.add_all([p1,p2,p5])
        # db.session.commit()
        import hashlib
        u = User(name='Admin', username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),user_role=UserRoleEnum.ADMIN)
        db.session.add(u)
        db.session.commit()
        # db.session.add_all([c1,c2,c3])
        # db.session.commit()
