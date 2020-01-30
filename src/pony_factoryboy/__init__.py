from factory import base

from ._version import get_version


class PonyOptions(base.FactoryOptions):

    def _build_default_options(self):
        return super()._build_default_options() + [
            base.OptionDefault('db', None, inherit=True),
        ]


class PonyFactory(base.Factory):

    _options_class = PonyOptions

    class Meta:
        abstract = True

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        db = cls._meta.db
        obj = model_class(*args, **kwargs)
        db.flush()
        return obj


__version__ = get_version()
del get_version
