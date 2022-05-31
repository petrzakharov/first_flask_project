from wtforms import Form, StringField, TextAreaField, FormField, SelectField, SelectMultipleField, FieldList
from models import Category, Tag
from wtforms import URLField


# class PostForm(Form):
#     title = StringField('Название поста')
#     text = TextAreaField('Текст поста')
#     author = StringField('Автор')


class CategoryForm(Form):
    name = StringField()


class TagForm(Form):
    name = StringField('Название тега')


class PostForm(Form):
    author = StringField('Юзернейм автора')
    title = StringField('Название поста')
    text = TextAreaField('Текст')
    category_id = SelectField(
        'Категория', choices=[(g.id, g.name) for g in Category.query.all()]
    )
    tag = SelectMultipleField(
        'Теги', choices=[(g.id, g.name) for g in Tag.query.all()]
    )
    image_url = URLField(
        'Ссылка на изображение'
    )
