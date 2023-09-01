"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

# import SQLAlchemy and connect it to flask app
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    """Model for users"""
 
    __tablename__ = 'users'

    def __repr__(self):
        """dunder. method that shows better info about pet, as defined by 
        the f statement below"""
        u = self
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name} image_url={u.image_url}>"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.String,
                           nullable=False)
    
    last_name = db.Column(db.String,
                          nullable=False)
    
    image_url = db.Column(db.String,
                          default="default_image.png")
    
    posts = db.relationship('Post') #this list of post objects that correspond to this user
    
class Post(db.Model):
    """Model for posts"""
    __tablename__ = 'posts'

    def __repr__(self):
        p = self
        return f"id={p.id} title={p.title} content={p.content} created_at={p.created_at} user_id={p.user_id}"

    id = db.Column(db.Integer,
                   primary_key=True)
    
    title = db.Column(db.String,
                      nullable=False)
    
    content = db.Column(db.String,
                        nullable=False)
    
    created_at = db.Column(db.Date,
                            default='today')
    
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'))
    
    # relationship allows SQLAlchemy to 'navigate' this relationship

    user = db.relationship('User', backref='postie')

def get_posts():
    all_posts = Post.query.all()

    for post in all_posts:
        if post.user is not None:
            print(post.title, post.content, post.user.first_name)
        else:
            print(post.title)