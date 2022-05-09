from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    comment_id = db.Column(db.Integer,db.ForeignKey('comment.id'))

    def __repr__ (self):
        return f'User {self.username}'

class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name}'
