# from copy import deepcopy
from multimethod import multimethod
from pymonad import curry, Monad, List
# from operator import add
add = curry(lambda a, b: a + b)
mul = curry(lambda a, b: a * b)


class User(Monad):
    login = None
    password = None

    def __init__(self):
        super(User, self).__init__(self.login)

    def bind(self, function):
        return function(self.login)

    def fmap(self, function):
        return function(self.login)


@multimethod(type, basestring, basestring)
def make_instance(cls, login, password):
    obj = cls()
    obj.login = login
    obj.password = password
    return obj


@multimethod(type, basestring)
def make_instance(cls, login):
    obj = cls()
    obj.login = login
    return obj


@multimethod(User, basestring)
def check_passwd(self, password):
    return self.password == password


@multimethod(User)
def login(self):
    return self.login


nightblues = make_instance(User, 'nightblues', 'passg')
print check_passwd(nightblues, '123456')
print nightblues.login
print add('the_') * nightblues

newuser = make_instance(User, 'Alice') >> (lambda l: make_instance(User, l + '&Bob'))
print newuser.login

users = List(mul(2), add('!')) & List('Alice', 'Bob', 'Eve')
print users
