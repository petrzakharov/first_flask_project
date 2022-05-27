from flask import Blueprint
from flask import render_template
from models import Post
from .forms import PostForm


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)


@posts.route('/create')
def create_post():
    # Создание поста
    form = PostForm()
    return render_template(
        'posts/add_post.html',
        form=form
    )


@posts.route('/<string:slug>')
def post_detail(slug):
    # если что-то похожее на get_object_or_404 во Flask?
    post = Post.query.filter(Post.id == id).first()
    tags, category = post.tags, post.category
    return render_template(
        'posts/post_detail.html',
        post=post,
        tags=tags,
        cateogy=category
    )


@posts.route('/category/<int:category_id>')
def posts_category(category_id):
    # Получить все посты из одной категории
    posts = Post.query.filter(Post.category_id == category_id)
    return render_template(
        'posts/posts_category.html',
        posts=posts
    )


@posts.route('/tag/<int:tag_id>')
def posts_tag(tag_id):
    # Получить все посты из одного тега
    posts = Post.query.filter(Post.post_tags == tag_id)
    return render_template(
        'posts/posts_tag.html',
        posts=posts
    )


def edit_post(post_id_or_slug):
    # Редактирование поста (может любой)
    pass


def upload():
    # Загрузка изображений
    pass


# Разобраться как выводить и сохранять изображения
# Пересмотреть вебинар по джанге и прочитать по джанге записанные вопросы

# ===Вьюхи
# 1. Все посты на главной
# 2. Все посты по определенной категории
# 3. Просмотр одного поста
# 4. Добавление одного поста


# ===Вьюхи-опционально
# 5. Админка
# 6. Регистрация и авторизация (+модель)
# 7. Просмотр всех постов по определенному тегу


# ===Пагинация!!! Как использовать во Flask?


# ===Шаблоны
# 1. Разделить на логические шаблоны
# 2. Вывести заготовки и протестировать что вьюхи работают корректно
