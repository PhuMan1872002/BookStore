from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin,BaseView,expose
from app import app,db
from app.models import Category, Product

class MyProductView(ModelView):
    column_list = ['id', 'name', 'price', 'active']
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    column_editable_list = ['name', 'price']
    edit_modal = True


class MyCategoryView(ModelView):
    column_list = ['id', 'name', 'products']


class StatsView(BaseView):
    @expose("/")
    def index(self):
        return self.render('admin/stats.html')

admin = Admin(app=app, name='Quản trị bán hàng', template_mode='bootstrap3')
admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(StatsView(name='Thông kê báo cáo'))