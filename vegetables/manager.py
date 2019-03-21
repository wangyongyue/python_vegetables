from flask_script import Manager
from flask_script import Command
from app import app
from run import db
from goods.models import Goods
from account.models import Role

manager = Manager(app)


@manager.command
def run():
    db.create_all()
    print('run_db')

if __name__ == '__main__':
    manager.run()