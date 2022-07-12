from main import db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


class Noun(db.Model):
    __tablename__ = 'nouns'

    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.String(3))
    word = db.Column(db.String)
    plural = db.Column(db.String)

    def dump(self):
        ret = {
            'id': self.id,
            'article': self.article,
            'word': self.word,
            'plural': self.plural
        }
        return ret

    def __str__(self):
        return self.word

# Base.metadata.bind = eng        
# Base.metadata.create_all()  

# Session = sessionmaker(bind=eng)