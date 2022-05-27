from app import db
from datetime import datetime
from slugify import slugify

post_tags = db.Table('post_tags',
                     db.Column('post_id', db.Integer,
                               db.ForeignKey('post.id'), primary_key=True),
                     db.Column('tag_id', db.Integer, db.ForeignKey(
                         'tag.id'), primary_key=True)
                     )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50))
    title = db.Column(db.String(140))
    text = db.Column(db.Text)
    slug = db.Column(db.String(140))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    created_on = db.Column(db.DateTime, default=datetime.now())
    updated_on = db.Column(
        db.DateTime, default=datetime.now(), onupdate=datetime.now()
    )

    def get_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f'Post id: {self.id}, title: {self.title}'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    created_on = db.Column(db.DateTime, default=datetime.now())
    posts = db.relationship('Post', backref='category')

    def __repr__(self):
        return f'Category id: {self.id} Category name: {self.name}'


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    posts = db.relationship('Post', secondary=post_tags, backref='tags')
    created_on = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'Tag id: {self.id} Tag name: {self.name}'


# создание форм фласк https://www.youtube.com/watch?v=lg1k2klqkdQ
# https://flask.palletsprojects.com/en/2.1.x/patterns/fileuploads/

# Для загрузки и показа изображений необходимо как-то использовать Flask-Uploads
# Похоже, что отдельное поле в БД для изображения ненужно
