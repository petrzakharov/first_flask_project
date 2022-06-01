from wtforms import (
    Form,
    SelectField,
    SelectMultipleField,
    StringField,
    TextAreaField,
    URLField,
)
from wtforms.validators import InputRequired

from models import Category, Tag


class CategoryForm(Form):
    name = StringField()


class TagForm(Form):
    name = StringField('Название тега', [InputRequired()])


class PostForm(Form):
    author = StringField('Юзернейм автора', [InputRequired()])
    title = StringField('Название поста', [InputRequired()])
    text = TextAreaField('Текст', [InputRequired()])
    category_id = SelectField(
        'Категория',
        choices=[(g.id, g.name) for g in Category.query.all()],
        validators=[InputRequired()]
    )
    tag = SelectMultipleField(
        'Теги', choices=[(g.id, g.name) for g in Tag.query.all()]
    )
    image_url = URLField(
        'Ссылка на изображение'
    )
