class Meta(type):
    def __init__(cls, *args, **kwargs):
        print 'called Meta.__init__({}, {}, {})'.format(cls, args, kwargs)
        return super(Meta, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print 'called Meta.__call__({}, {}, {})'.format(cls, args, kwargs)
        new_cls = type(cls.__name__, (cls,), dict(cls.__dict__))
        for k, v in kwargs.items():
            setattr(new_cls, k, v)
        return super(Meta, new_cls).__call__()


class A(object):
    __metaclass__ = Meta

    att = 123

    def __new__(cls, *args, **kwargs):
        print 'called A.__new__({}, {})'.format(args, kwargs)
        print 'A.__dict__ = {}'.format(cls.__dict__)
        return super(A, cls).__new__(cls, *args, **kwargs)


a = A()
a2 = A(x=1)
a3 = A(y=5)
a3 = A(z=7)
