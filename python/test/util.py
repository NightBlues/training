__author__ = 'nightblues'
# objects of this class should help us with testing
# sorting and data structures for working with non primitive types
class CompEl():
    def __init__(self, val, key):
        self.val=val
        self.key=key

    def __unicode__(self):
        return "<CompEl %s, %d>" %\
         (self.val, self.key)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()