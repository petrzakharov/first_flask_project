from datetime import datetime

from slugify import slugify

from app import db

post_tags = db.Table('post_tags',
                     db.Column('post_id', db.Integer,
                               db.ForeignKey('post.id'), primary_key=True),
                     db.Column('tag_id', db.Integer, db.ForeignKey(
                         'tag.id'), primary_key=True)
                     )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(140), nullable=False, unique=True)
    text = db.Column(db.Text, unique=True)
    slug = db.Column(db.String(140), unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    created_on = db.Column(db.DateTime, default=datetime.now())
    updated_on = db.Column(
        db.DateTime, default=datetime.now(), onupdate=datetime.now()
    )
    tags = db.relationship(
        'Tag', secondary=post_tags, backref=db.backref(
            'posts_tag', lazy='dynamic'
        )
    )
    image_url = db.Column(db.String(300))

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.get_slug()

    def get_slug(self):
        self.slug = slugify(self.title)

    def __repr__(self):
        return f'Post id: {self.id}, title: {self.title}'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    created_on = db.Column(db.DateTime, default=datetime.now())
    posts = db.relationship('Post', backref='category')

    def __repr__(self):
        return f'Category id: {self.id} Category name: {self.name}'


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    posts = db.relationship('Post', secondary=post_tags, backref='tags_posts')
    created_on = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'Tag id: {self.id} Tag name: {self.name}'
