from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from app import app, db
from app.models import Category, Product

admin = Admin(app=app, name='QUAN TRI BAN HANG', template_mode ='bootstrap4')


class MyProductView(ModelView):
    column_display_pk = True
    column_list = ['name', 'price', 'category']
    column_searchable_list = ['name']
    column_filters = ['price', 'name']
    can_export = True
    can_view_details = True


class MyCategoryView(ModelView):
    column_list = ['name', 'products']

class MyStatsView(BaseView):
    @expose("/")
    def index(self):
        return self.render('admin/stats.html')

admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyStatsView(name='Thong ke bao cao'))