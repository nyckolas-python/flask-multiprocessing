from app import db
from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Announcements(db.Model):
    __tablename__ = 'announcements'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(1024), nullable=False)
    price = db.Column(db.String(255), nullable=False)


def _init_db():
    
    """Инициализирует БД"""
    db.create_all()
    for i in range(1,4):
        name = 'admin'+str(i)
        new_user = User(username=name, password_hash=generate_password_hash(name))
        db.session.add(new_user)
        db.session.commit()
    return

def check_db_exists():
    
    """Проверяет, инициализирована ли БД, если нет — инициализирует"""
    try:
        users = User.query.all()
        if users:
            return

        _init_db()
    except Exception as e:
        print(e)

check_db_exists()
