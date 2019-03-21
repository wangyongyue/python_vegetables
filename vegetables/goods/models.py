from run import db

class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(99), unique=False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name