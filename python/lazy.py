from lazyobject import ThreadSafeLazyObject

print '* variant 1'
class LazyObject(object):
    def __init__(self, lazy_obj):
        self.lazy_obj = lazy_obj

    def __get__(self, obj, type_):
        if not hasattr(self, 'forced_obj'):
            self.forced_obj = self.lazy_obj()
        return self.forced_obj


def get_version():
    print 'getting version'
    return '3.6.3'


class Settings(object):
    version = LazyObject(get_version)


version_ = LazyObject(get_version)

print 'Starting...'
print Settings.version
print Settings.version
print version_
print version_


print '* variant 2'
class MyLazyClass(ThreadSafeLazyObject):
    def _setup(self):
        my_real_object = get_version()
        self._wrapped = my_real_object


version_ = MyLazyClass()


class Settings(object):
    version = MyLazyClass()

print 'Starting'
print Settings.version
print Settings.version
print version_
print version_
print ','.join([version_, Settings.version])


print '* variant 3'
class LazyStr(str):

    def __init__(self, lazy_obj):
        self.lazy_obj = lazy_obj

    def __str__(self):
        if not hasattr(self, 'forced_obj'):
            self.forced_obj = self.lazy_obj()
        return self.forced_obj


version_ = LazyStr(get_version)


class Settings(object):
    version = LazyStr(get_version)


print 'Starting'
print Settings.version
print Settings.version
print version_
print version_
print ','.join([version_, Settings.version])

