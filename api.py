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
    dictionaries = db.session.query(Dictionary).all()
    lst = [dictionary.dump() for dictionary in dictionaries]
    return lst, 200


def add_word(_type, germanWord):
    dictionary = db.session.query(Dictionary).filter_by(id=1).one_or_none()
    
    if _type == 'noun':
        word = db.session.query(Noun).filter_by(id=germanWord).one_or_none()
        dictionary.nouns.append(word)
    elif _type == 'verb':
        word = db.session.query(Verb).filter_by(
                                        praesent=germanWord).one_or_none()
        dictionary.verbs.append(word)
    elif _type == 'adjective':
        word = db.session.query(Adjective).filter_by(id=germanWord).one_or_none()
        dictionary.adjectives.append(word)
    elif _type == 'other':
        word = db.session.query(Other).filter_by(id=germanWord).one_or_none()
        dictionary.others.append(word)
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
    noun = Noun(article=article, word=word, plural=plural)
    db.session.add(noun)
    db.session.commit()

    add_word('noun', noun.id)

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
