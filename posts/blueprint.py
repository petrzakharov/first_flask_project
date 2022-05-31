from flask import Blueprint
from flask import render_template, abort, Response, request, redirect, url_for
from models import Post, Tag, Category
from .forms import PostForm, TagForm
from app import db

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    posts = Post.query
    page_number = request.args.get('page')
    if page_number and page_number.isdigit():
        page_number = int(page_number)
    else:
        page_number = 1
    part_posts = posts.paginate(page=page_number, per_page=4)
    categories = Category.query.all()
    return render_template(
        'posts/index.html', posts=part_posts, categories=categories
    )


@posts.route('/add_tag', methods=['POST', 'GET'])
def create_tag():
    if request.method == 'POST':
        name = request.form.get('name')
        try:
            tag = Tag(name=name)
            db.session.add(tag)
            db.session.commit()
        except:
            abort(Response('Возникла ошибка при создании тега', 400))
        return redirect(url_for('posts.index'))
    form = TagForm()
    categories = Category.query.all()
    return render_template(
        'posts/add_tag.html',
        form=form,
        categories=categories
    )


@posts.route('/add_post', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        text = request.form.get('text')
        author = request.form.get('author')
        category_id = request.form.get('category_id')
        tags = request.form.getlist('tag')
        image_url = request.form.get('image_url')
        try:
            post = Post(
                title=title, text=text, author=author, category_id=category_id,
                image_url=image_url
            )
            tag_objects = Tag.query.filter(Tag.id.in_(tags)).all()
            post.tags = tag_objects
            db.session.add(post)
            db.session.commit()
        except:
            abort(Response('Возникла ошибка при создании поста', 400))
        return redirect(url_for('posts.index'))
    form = PostForm()
    categories = Category.query.all()
    return render_template(
        'posts/add_post.html',
        form=form,
        categories=categories
    )


@posts.route('/<string:slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    if not post:
        abort(Response('Страница не найдена', 404))
    categories = Category.query.all()
    return render_template(
        'posts/post.html',
        post=post,
        tags=post.tags,
        category=post.category,
        categories=categories
    )


@posts.route('/category/<int:category_id>')
def posts_category(category_id):
    # Получить все посты из одной категории
    category = Tag.query.get_or_404(category_id, 'Страница не найдена')
    posts = Post.query.filter(Post.category_id == category.id)
    categories = Category.query.all()
    return render_template(
        'posts/category.html',
        posts=posts,
        type='category',
        categories=categories
    )


@posts.route('/tag/<int:tag_id>')
def posts_tag(tag_id):
    # Получить все посты из одного тега
    tag = Tag.query.get_or_404(tag_id, 'Страница не найдена')
    posts = Post.query.filter(Post.tags.contains(tag))
    categories = Category.query.all()
    return render_template(
        'posts/category.html',
        posts=posts,
        type='tag',
        categories=categories
    )


@posts.route('/<string:slug>/edit/', methods=['POST', 'GET'])
def edit_post(slug):
    # Редактирование поста (может любой)
    post = Post.query.filter(Post.slug == slug).first()
    if not post:
        abort(Response('Пост не найден', 404))
    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        tags = request.form.getlist('tag')
        post.tags = Tag.query.filter(Tag.id.in_(tags)).all()
        db.session.commit()
        return redirect(url_for('posts.post_detail', slug=post.slug))
    form = PostForm(obj=post)
    categories = Category.query.all()
    return render_template(
        'posts/edit_post.html', post=post, form=form, categories=categories
    )


# 6. Регистрация и авторизация опционально (+модель)
# Можно добавить пагинацию в категории
# Добавить валидаторы в форму, чтобы без обязательных полей ее нельзя было отправить
# Вывести теги на странице поста
# Уменьшить отступ от названия поста до текста
# Обрезать длинный текст постов при овервью
# Проверить pep8, отсортировать импорты
# Запушить на гитхаб
# Контейнеры, докер
