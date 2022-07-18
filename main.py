from connexion import FlaskApp
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import create_engine

basedir = os.path.abspath(os.path.dirname(__file__))

connexion_app = FlaskApp(__name__)
app=connexion_app.app
uri = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

engine = create_engine(
    uri,
    connect_args={'check_same_thread': False}
)


if __name__ == '__main__':
    from orm import Base
    Base.metadata.create_all(db.engine)
    connexion_app.add_api('openapi.yaml')
    connexion_app.run(host='0.0.0.0', port=5000, debug=True)
