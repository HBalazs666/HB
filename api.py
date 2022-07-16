from connexion.problem import problem
from orm import Noun, Other
from orm import Verb
from orm import Adjective
from orm import Dictionary
from main import db


def create_dictionary(body):
    dictionary = Dictionary()
    db.session.add(dictionary)
    db.session.commit()


def get_dict_nouns():
    dictionaries = db.session.query(Dictionary).all()

    verbs = dictionaries[0].verbs
    lst = [v.dump() for v in verbs]

    return lst, 200


def get_dictionary():

    dictionary = db.session.query(Dictionary).filter_by(id=1).one_or_none()

    if dictionary == None:
        dictionary = Dictionary()
        db.session.add(dictionary)
        db.session.commit()

    ret = dictionary.dump()
    return ret, 200

def add_word(_type, germanWord):
    dictionary = db.session.query(Dictionary).filter_by(id=1).one_or_none()
    
    if _type == 'noun':
        word = db.session.query(Noun).filter_by(word=germanWord).one_or_none()
        dictionary.nouns.append(word)
        db.session.commit()
    elif _type == 'verb':
        word = db.session.query(Verb).filter_by(
                                        praesent=germanWord).one_or_none()
        dictionary.verbs.append(word)
        db.session.commit()
    elif _type == 'adjective':
        word = db.session.query(Adjective).filter_by(id=germanWord).one_or_none()
        dictionary.adjectives.append(word)
        db.session.commit()
    elif _type == 'other':
        word = db.session.query(Other).filter_by(id=germanWord).one_or_none()
        dictionary.others.append(word)
        db.session.commit()
    else:
        return problem(404, 'Not found',
                       'Word Type does not exist.')

    return dictionary

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
    noun = Noun(article=article, word=word, plural=plural, dictionary_id=1)
    db.session.add(noun)
    db.session.commit()
    noun_queried = db.session.query(Noun).filter_by(word=word).one_or_none()

    add_word('noun', noun_queried.word)

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


    add_word('verb', praesent)

    return verb.dump(), 201


def get_verbs():
    verbs = db.session.query(Verb).all()
    lst = [verb.dump() for verb in verbs]
    return lst, 200
