import os
import redis
import uuid
import datetime
from abc import ABCMeta, abstractproperty


class Identifier:
    def __init__(self, value=None):
        if value is None:
            value = str(uuid.uuid4())
        self.value = value

    def __repr__(self):
        return self.value

    __str__ = __repr__


client = redis.Redis.from_url(os.environ['REDIS_PORT'])

class Manager:

    storage = client

    @classmethod
    def save(cls, entity):
        cls.storage.set(entity.identifier, entity.document)

    @classmethod
    def get(cls, identifier):
        cls.storage.get(identifier)


class Entity:

    __metaclass__ = ABCMeta

    @abstractproperty
    def fields(self):
        return []

    @abstractproperty
    def relations(self):
        pass

    @property
    def uuid(self):
        return str(self.__identifier)

    def __init__(self):
        self.__identifier = Identifier()
        if len(self.fields):
            for field in self.fields:
                setattr(self, field, None)

    @property
    def identifier(self):
        name = self.__class__.__name__
        return '%s:%s'%(name, self.uuid)

    @classmethod
    def get(cls, identifier):
        if type(identifier) != Identifier:
            identifier = Identifier(identifier)
        key = '%s:%s'%(cls.__name__, identifier)
        inst = cls.create(Manager.get(key))
        inst.setuuid(identifier)
        return inst

    def save(self):
        Manager.save(self)

    @classmethod
    def create(cls, fields):
        item = cls.__new__(cls)
        return item

    @property
    def document(self):
        return {field:getattr(self, field) for field in self.fields}

class Relation(object):
    TYPE_SINGLE = 'single'
    TYPE_MULTIPLE = 'multiple'
    type = TYPE_SINGLE
    types = [TYPE_SINGLE, TYPE_MULTIPLE]


def timestampable(cls):
    cls.fields += ['created_at', 'udpated_at']
    cls.created_at = datetime.datetime.now()
    old_setattr = cls.__setattr__

    def new_setter(self, key, value):
        cls.updated_at = datetime.datetime.now()
        old_setattr(self, key, value)
    cls.__setattr__ = new_setter
    return cls

@timestampable
class Customer(Entity):
    fields = [
        'name',
        'email'
    ]
    relations = []

class User(Entity):
    pass

