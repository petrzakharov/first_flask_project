import click
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)


db = SQLAlchemy(app)

migrate: Migrate(app, db)


@click.command(name='add_mockup')
def add_mockup():
    import random

    from app import db
    from models import Category, Post, Tag
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
    categories_ids, tags_obj = [], []

    for category in categories:
        category_object = Category(name=category['name'])
        db.session.add(category_object)
        db.session.commit()
        categories_ids.append(category_object.id)
    for tag in tags:
        tag_object = Tag(name=tag['name'])
        db.session.add(tag_object)
        db.session.commit()
        tags_obj.append(tag_object)
    for post in posts:
        post_object = Post(
            title=post['title'], author=post['author'], text=post['text']
        )
        post_object.category_id = random.choice(categories_ids)
        for one_tag in random.sample(
            tags_obj, random.randint(0, len(tags_obj))
        ):
            post_object.tags.append(one_tag)
        db.session.add(post_object)
        db.session.commit()


app.cli.add_command(add_mockup)
