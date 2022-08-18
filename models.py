from app import db
from flask_login import LoginManager, UserMixin, current_user
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
        return "<User {}:{}>".format(self.id, self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Announcements(db.Model):
    __tablename__ = 'announcements'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255))
    name = db.Column(db.String(1024), nullable=False)
    price = db.Column(db.String(255), nullable=False)
    vendor_name = db.Column(db.String(255))
        
    def __repr__(self):
        return "<Announcements {}:{}>".format(self.name, self.price)


def add_announcements(items):
    for item in items:
        new_announcement = Announcements(name=item.get('name'), price=item.get('price'), image=item.get('image'), vendor_name=item.get('vendor_name'))
        try:
            db.session.add(new_announcement)
            db.session.commit()
        except Exception as e:
            print(e)
    


def _init_db():
    
    """Инициализирует БД"""
    db.create_all()
    for i in range(1,4):
        name = 'admin'+str(i)
        new_user = User(username=name, password_hash=generate_password_hash(name))
        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            print(e)

def check_db_exists():
    
    """Проверяет, инициализирована ли БД, если нет — инициализирует"""
    db.create_all()
    try:        
        users = User.query.all()      
    except Exception as e:
        _init_db()
        print(e)

check_db_exists()
