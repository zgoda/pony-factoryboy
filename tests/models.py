from pony.orm import Database, Optional, Required, PrimaryKey

db = Database()


class StandardModel(db.Entity):
    foo = Required(str, 20)


class NonIntegerPK(db.Entity):
    foo = PrimaryKey(str, 20)
    bar = Optional(str, 20)


class MultifieldModel(db.Entity):
    slug = Required(str, 20, unique=True)
    text = Required(str, 20)


class MultifieldUniqueModel(db.Entity):
    slug = Required(str, 20, unique=True)
    text = Required(str, 20, unique=True)
    title = Required(str, 20, unique=True)


db.bind('sqlite', ':memory:')
db.generate_mapping(create_tables=True)
