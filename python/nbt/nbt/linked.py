import sys

w = sys.stdout.write

cons   = lambda el, lst: [el, lst]
make_list = lambda *args: reduce(lambda lst, el: cons(el, lst), reversed(args), None)
car = lambda lst: lst[0] if lst and hasattr(lst, "__len__") and len(lst) == 1 else lst
cdr = lambda lst: lst[1] if lst and hasattr(lst, "__len__") and len(lst) > 1 else lst
nth = lambda n, lst: nth(n - 1, cdr(lst)) if n > 0 else car(lst)
length  = lambda lst, count=0: length(cdr(lst), count + 1) if lst else count
# length = lambda lst: reduce(lambda res, el: res + 1, lst)
begin   = lambda *args: args[-1]
display = lambda lst: begin(w("%s " % car(lst)), display(cdr(lst))) if lst else w("nil\n")
