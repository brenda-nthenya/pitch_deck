from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    @property
    def  password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_passowrd(self, password):
        return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        return f'User {self.username}'
class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(), nullable = False)

    def __repr__(self):
        return f'User {self.name}'
