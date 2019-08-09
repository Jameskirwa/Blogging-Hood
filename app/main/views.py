from flask import render_template,redirect,url_for,abort, request
from . import main
from ..models import User,Blog, Comment
from .forms import BlogForm,AddAuthor, CommentForm
from .. import db
from flask.views import View, MethodView
from flask_login import login_required, current_user
import requests
import json


@main.route('/')
def index():
    
    blog = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    return render_template('index.html', blog = blog )

@main.route('/blog/new/', methods=['GET', 'POST'])
@login_required
def new_blog():
    '''
    Function that creates new bloges
    '''
    form = BlogForm()

    if form.validate_on_submit():
        title = form.title.data
        owner_id=current_user
        description = form.description.data
        
        
        new_blog = Blog(owner_id=current_user._get_current_object().id, title=title, description=description)

        new_blog.save_blog()
        return redirect(url_for('main.blog'))

    return render_template('new_blog.html', new_blog_form=form)

@main.route('/blog')
def blog():
    blogs = Blog.query.order_by(Blog.date_posted.desc())
    random = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()

    return render_template('blogs.html', blogs=blogs, random=random)


@main.route('/blogs/<int:blog_id>',methods = ["GET","POST"])
def view_blog(blog_id):
    blog = Blog.query.filter_by(id=blog_id).first()
    random = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    form = CommentForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        new_comment = Comment(name=name, description=description,blog_id=blog_id)
        new_comment.save_comment()
        return redirect(url_for('main.view_blog', blog_id=blog_id))
    comments = Comment.query.filter_by(blog_id=blog_id)
    
    return render_template("blog.html", blog_form=form, blog=blog, random = random, comments=comments)

@main.route("/delete/<blog_id>",methods = ['GET','POST'])
def delete(blog_id):
    blog = Blog.query.filter_by(id=blog_id).first()
    db.session.delete(blog)
    db.session.commit()

    return redirect(url_for('main.blog'))

@main.route('/<int:blog_id>/delete comments')
@login_required
def delete_comment(blog_id):
    comment = Comment.query.filter_by(blog_id=blog_id).first()
    blog_id = comment.blog_id

    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('main.view_blog', blog_id=blog_id))



    