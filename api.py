from orm import Noun
from orm import Verb
from orm import Adjective
from orm import Dictionary
from main import db


def create_dictionary():
    pass


def get_dictionary():
    dictionary = db.session.query(Dictionary).all()
    return dictionary.dump(), 200


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


def create_verb(body):
    praesent = body['praesent']
    E3 = body['E3']
    praeteritum = body['praeteritum']
    perfekt = body['perfekt']
    verb = Verb(praesent=praesent, E3=E3, praeteritum=praeteritum,
                perfekt=perfekt)
    db.session.add(verb)
    db.session.commit()
    return verb.dump(), 201


def get_verbs():
    verbs = db.session.query(Verb).all()
    lst = [verb.dump() for verb in verbs]
    return lst, 200
