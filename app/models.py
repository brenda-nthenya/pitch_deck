from . import db,login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



class User(UserMixin,db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)
    pass_secure = db.Column(db.String(255))


    def save_u(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def  password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        return f'User {self.username}'
class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(), nullable = False)

    def __repr__(self):
        return f'User {self.name}'



class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls,id):
        upvote = Upvote.query.filter_by(pitch_id=id).all()
        return upvote


    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'


@login_manager
def load_user(user_id):
    return User.query.get(int(user_id))

