import pytest
import factory
from pony.orm import db_session
from pony_factoryboy import PonyFactory

from . import models


class StandardFactory(PonyFactory):

    class Meta:
        db = models.db
        model = models.StandardModel

    foo = factory.Sequence(lambda n: f'foo-{n}')


@pytest.fixture
def database():
    models.db.create_tables()
    yield
    models.db.drop_all_tables(with_all_data=True)


@pytest.mark.usefixtures('database')
class TestStandardSequence:

    @pytest.fixture(autouse=True)
    def set_up(self):
        StandardFactory.reset_sequence()

    @db_session
    def test_single(self):
        std = StandardFactory.build()
        assert std.foo == 'foo-0'

    @db_session
    def test_many(self):
        std1 = StandardFactory.build()
        std2 = StandardFactory.build()
        assert std1.foo == 'foo-0'
        assert std2.foo == 'foo-1'

    @db_session
    def test_pk_creation(self):
        std1 = StandardFactory.create()
        assert std1.foo == 'foo-0'
        assert std1.id == 1
        StandardFactory.reset_sequence()
        std2 = StandardFactory.create()
        assert std2.foo == 'foo-0'
        assert std2.id == 2

    @db_session
    def test_pk_force_value(self):
        std1 = StandardFactory.create(id=10)
        assert std1.foo == 'foo-0'
        assert std1.id == 10
        StandardFactory.reset_sequence()
        std2 = StandardFactory.create()
        assert std2.foo == 'foo-0'
        assert std2.id == 11
