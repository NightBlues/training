__author__ = 'nightblues'
# from __future__ import division

def print_heap(h):
    """
    Try to draw a tree in ascii mode.

    @param h: heap
    @type h: list
    """
    level = 0
    result = []
    accum = []
    for x in range(len(h)):
        if (x + 1) >= (2 ** level):
            level += 1
            result.append(accum)
            accum = []
        accum.append(h[x])
    result.append(accum)
    result = result[1:]
    res_str = ""
    start_spaces_count = 0
    between_spaces_count=1
    for x in reversed(range(len(result))):
        start_spaces_count = start_spaces_count*2 +1
        between_spaces_count = between_spaces_count*2 +1
        sp_b = ' '*between_spaces_count
        if x>0:
            prep_str= ' ' * start_spaces_count
            for a in range(len(result[x])):
                prep_str += '/' if a%2==0 else '\\'
                prep_str += sp_b
            prep_str+='\n'
        else :
            prep_str = ''
        prep_str+= ' ' * start_spaces_count +sp_b.join([str(a) for a in result[x]])+'\n'

        res_str=prep_str+res_str

    print(res_str)


def insert(h, el, last=None, comp=lambda a, b: a < b):
    """
    Insert an element to the heap without breaking it.

    @param h: heap
    @param el: element to be inserted (not index)
    @param last: the last element of heap (all elements with indexes>last are being ignored)
    @param comp; compare function (default is lambda a, b: a < b)
    @type h: list
    @type el: object
    @type last: int
    @type comp: function
    """
    if last is None:
        last = len(h)
    h.insert(last, el)
    pushup(h, last, comp)


def pop(h, last=None, comp=lambda a, b: a < b):
    """
    Return first element and delete it without breaking tree.

    @param h: heap
    @param last: the last element of heap (all elements with indexes>last are being ignored)
    @param comp; compare function (default is lambda a, b: a < b)
    @type h: list
    @type last: int
    @type comp: function
    """
    if last is None:
        last = len(h)-1
    if last <0:
        return None
    result = h[0]
    delete(h, 0, last, comp)
    return result


def delete(h, el_i, last=None, comp=lambda a, b: a < b):
    """
    Delete element @el_i it without breaking tree.

    @param h: heap
    @param el_i: index of element to be deleted
    @param last: the last element of heap (all elements with indexes>last are being ignored)
    @param comp; compare function (default is lambda a, b: a < b)
    @type h: list
    @type el_i: int
    @type last: int
    @type comp: function
    """
    if last is None:
        last = len(h) - 1
    h[el_i] = h[last]
    h.pop(last)
    pushdown(h, el_i, last, comp)


def pushup(h, el_i, comp=lambda a, b: a < b):
    """
    Push element @el_i up according heap rules for saving tree.

    @param h: heap
    @param el_i: index of element to be pushed up
    @param comp; compare function (default is lambda a, b: a < b)
    @type h: list
    @type el_i: int
    @type comp: function
    """
    while el_i > 0 and comp(h[el_i], h[el_i // 2]):
        h[el_i], h[el_i // 2] = h[el_i // 2], h[el_i]
        el_i = el_i // 2


def pushdown(h, el_i, last=None, comp=lambda a, b: a < b):
    """
    Push element @el_i down according heap rules for saving tree.

    @param h: heap
    @param el_i: index of element to be deleted
    @param last: the last element of heap (all elements with indexes>last are being ignored)
    @param comp; compare function (default is lambda a, b: a < b)
    @type h: list
    @type el_i: int
    @type last: int
    @type comp: function
    """
    if last is None:
        last = len(h)
    prior_child = get_prior_child(h, el_i,last, comp)
    # print("-----")
    # print("pushdown element %d for heap:%s,child_i=%d"%(el_i,h,prior_child))
    while el_i < last-1 and (prior_child is not None) and not comp(h[el_i], h[prior_child]):
        h[el_i], h[prior_child] = h[prior_child], h[el_i]
        el_i = prior_child
        prior_child = get_prior_child(h, el_i,last, comp)
        # print("heap: %s,el_i=%s,child_i=%s"%(h,el_i,prior_child))
    # print("-----")


def get_children(h, el_i, last=None):
    """
    Return 2 children of element @el_i without disturbing elements with indexes greater than @last.

    @param h: heap
    @param el_i: index of element to be deleted
    @param last: the last element of heap (all elements with indexes>last are being ignored)
    @type h: list
    @type el_i: int
    @type last: int
    """
    # because of indexes of list starts with 0 not 1
    # we use ((el_i+1) * 2)-1 and ((el_i+1) * 2)
    # instead of el_i * 2 and (el_i * 2)+1
    if last is None:
        last = len(h)-1
    ch1 = ((el_i+1) * 2)-1
    if ch1 >= last:
        return []
    ch2 = (el_i+1) * 2
    if ch2 >= last:
        return [ch1]
    return [ch1, ch2]


def get_prior_child(h, el_i,last=None, comp=lambda a, b: a < b):
    """
    Return element being greater/lower than other one depending on @comp function.

    @param h: heap
    @param el_i: index of element to be deleted
    @param last: the last element of heap (all elements with indexes>last are being ignored)
    @param comp; compare function (default is lambda a, b: a < b)
    @type h: list
    @type el_i: int
    @type last: int
    @type comp: function
    """
    if last is None:
        last = len(h)-1
    ch = get_children(h, el_i,last)
    if len(ch)==0:
        return None
    if len(ch) < 2:
        return ch[0]
    result = 0
    if comp(h[ch[0]], h[ch[1]]):
        result = ch[0]
    else:
        result = ch[1]
    return result




