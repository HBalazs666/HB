from orm import Noun
from main import db


def get_nouns():
    nouns = db.session.query(Noun).all()
    lst = [noun.dump() for noun in nouns]
    return lst, 200


def get_noun(nounId):
    pass


def create_noun(body):
    article = body['article']
    word = body['word']
    plural = body['plural']
    noun = Noun(article=article, word=word, plural=plural)
    db.session.add(noun)
    db.session.commit()
    return noun.dump(), 201