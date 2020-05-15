""" User models """
import datetime as dt
from ..database import Column, Model, SurrogatePK, db
from ..extensions import bcrypt
from sqlalchemy.orm import relationship


class Account(SurrogatePK, Model):
    __tablename__ = 'account'
    username = Column(db.String(35), nullable=False, unique=True)
    password = Column(db.String(200), nullable=False)
    name = Column(db.String(50))
    roles = relationship('Role', secondary='user_roles')
    
    def __repr__(self):
        return f"User('{self.username}', '{self.password}', '{self.name}', '{self.group_id}')"

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'username': x.username,
                'password': x.password,
                'name': x.name
            }
        return {'users': list(map(lambda x: to_json(x), Account.query.all()))}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(
        'account.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey(
        'roles.id', ondelete='CASCADE'))


class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklist(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
