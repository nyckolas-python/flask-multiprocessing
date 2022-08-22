from app import db
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    announcements = db.relationship('Announcement', backref='owner')

    def __repr__(self):
        return "<User {}:{}>".format(self.id, self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Announcement(db.Model):
    __tablename__ = 'announcement'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255))
    name = db.Column(db.String(1024), nullable=False)
    price = db.Column(db.String(255), nullable=False)
    vendor_name = db.Column(db.String(255))
    olx_id = db.Column(db.String(25))
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # owner = db.relationship('User', backref=db.backref('creater', lazy=True))
   
    def __repr__(self):
        return "<Announcement {}:{}>".format(self.name, self.price)


def add_announcements(items):
    for item in items:
        user_id = current_user.get_id()
        try:
            if item:
                new_announcement = Announcement(name=item.get('name'), price=item.get('price'), \
                                image=item.get('image'), vendor_name=item.get('vendor_name'), \
                                olx_id=item.get('olx_id'), user_id=user_id\
                                )
                db.session.add(new_announcement)
                db.session.commit()
        except Exception as e:
            print(e)

def delete_announcement(olx_id):
    try:
        user_id = current_user.get_id()
        Announcement.query.filter_by(olx_id=olx_id, user_id=user_id).delete()
        db.session.commit()
        
    except Exception as ex:
        print(ex)
    return


def sort_by_price(price_field):
    try:
        pass
    except Exception as ex:
        print(ex)


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


def _drop_db():
    db.session.commit()
    db.drop_all()
    return _init_db()


def check_db_exists():
    
    """Проверяет, инициализирована ли БД, если нет — инициализирует"""
    db.create_all()
    try:
        if User.query.first():
            pass
        else:
            _init_db()
    except Exception as e:
        print(e)

check_db_exists()
