from main import db
from sqlalchemy import Column, Integer, String, ForeignKey
import json



class Dictionary(db.Model):
    __tablename__ = 'dictionary'

    id = db.Column(db.Integer, primary_key=True)

    nouns = db.relationship('Noun', back_populates='dictionary')
    verbs = db.relationship('Verb', back_populates='dictionary')
    adjectives = db.relationship('Adjective', back_populates='dictionary')
    others = db.relationship('Other', back_populates='dictionary')

    def dump(self):
        verbs = [v.dump() for v in self.verbs]
        nouns = [n.dump() for n in self.nouns]
        adjectives = [a.dump() for a in self.adjectives]
        others = [o.dump() for o in self.others]
        ret = {
            'id': self.id,
            'nouns': nouns,
            'verbs': verbs,
            'adjectives': adjectives,
            'others': others
        }

        return ret


class Noun(db.Model):
    __tablename__ = 'nouns'

    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.String(3))
    word = db.Column(db.String)
    plural = db.Column(db.String)

    dictionary_id = db.Column(Integer, ForeignKey('dictionary.id'))
    dictionary = db.relationship('Dictionary', back_populates='nouns')

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


class Verb(db.Model):
    __tablename__ = 'verbs'

    id = db.Column(db.Integer, primary_key=True)
    praesent = db.Column(db.String)
    E3 = db.Column(db.String)
    praeteritum = db.Column(db.String)
    perfekt = db.Column(db.String)

    dictionary_id = db.Column(Integer, ForeignKey('dictionary.id'))
    dictionary = db.relationship('Dictionary', back_populates='verbs')

    def dump(self):
        ret = {
            'id': self.id,
            'praesent': self.praesent,
            'E3': self.E3,
            'praeteritum': self.praeteritum,
            'perfekt': self.perfekt
        }
        return ret

    def __str__(self):
        return self.praesent


class Adjective(db.Model):
    __tablename__ = 'adjectives'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String)

    dictionary_id = db.Column(Integer, ForeignKey('dictionary.id'))
    dictionary = db.relationship('Dictionary', back_populates='adjectives')

    def dump(self):
        ret = {
            'id': self.id,
            'word': self.word,
        }
        return ret

    def __str__(self):
        return self.word


class Other(db.Model):
    __tablename__ = 'others'

    id = db.Column(db.Integer, primary_key=True)
    words = db.Column(db.String)

    dictionary_id = db.Column(Integer, ForeignKey('dictionary.id'))
    dictionary = db.relationship('Dictionary', back_populates='others')

    def dump(self):
        word_list = [word.dump() for word in self.words]
        ret = {

            'id': self.id,
            'words': word_list,
        }
        return ret

    def __str__(self):
        return self.word


db.create_all()
