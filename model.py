from tinydb import TinyDB, Query

db = TinyDB('db.json')


def get_todos():
    return db.all()


def new_todo(text):
    db.insert({'id': '1', 'title': text})


def del_todo(id):
    query = Query()
    db.remove(query.id == id)
