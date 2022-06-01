from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app import app, db
from models import Category, Post, Tag
from posts.blueprint import posts

app.register_blueprint(posts, url_prefix='/blog')
admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Tag, db.session))
admin.add_view(ModelView(Category, db.session))

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run()
