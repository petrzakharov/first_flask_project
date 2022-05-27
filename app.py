from distutils.command.config import config
from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
import click
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate: Migrate(app, db)


@click.command(name='add_mockup')
def add_mockup():
    from models import Post, Category, Tag
    import random
    from app import db
    print(Post)
    posts = [
        {'title': 'Post_111', "author": 'ivan', "text": 'OK OK OK POST'},
        {'title': 'Post_222', "author": 'oleg', "text": 'NORM NORM POST'},
        {'title': 'Post_333', "author": 'sergey', "text": 'KEK KEK POST'},
        {'title': 'Post_444', "author": 'egor', "text": 'BLABLABLA POST'},
    ]
    categories = [
        {"name": 'Australia'},
        {"name": 'Russia'},
        {"name": 'Italy'},
    ]
    tags = [
        {"name": 'Oh so gooood tag'},
        {"name": 'So interesting journey'},
        {"name": 'It was amazing'},
        {"name": 'Coolstory'},
    ]

    for post in posts:
        post_object = Post(
            title=post['title'], author=post['author'], text=post['text']
        )
        category = Category(name=random.choice(categories)['name'])
        db.session.add(post_object)
        db.session.add(category)
        db.session.commit()
        post_object.category_id = category.id
        for tag in random.sample(tags, random.randint(0, len(tags))):
            tag_object = Tag(name=tag['name'])
            db.session.add(tag_object)
            db.session.commit()
            post_object.tags.append(tag_object)
        db.session.add(post_object)
        db.session.commit()


app.cli.add_command(add_mockup)
