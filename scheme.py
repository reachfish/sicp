#--------------------------------------------------------------
# pair
def cons(a, b):
    return lambda pick: (a,b)[pick]

def car(x):
    return x(0)

def cdr(x):
    return x(1)

def cons_str(x):
    return "[%s, %s]" %(str(car(x)), str(cdr(x)))

#--------------------------------------------------------------
# slist
def slist(*args):
    if len(args) == 0:
        return None

    return cons(args[0], slist(*(args[1:])))

def slist_len(ls):
    if ls is None:
        return 0
    else:
        return 1 + slist_len(cdr(ls))

def slist_foreach(ls, f):
    if ls is None:
        return

    f(car(ls))
    slist_foreach(cdr(ls), f)

def slist_map(ls, f):
    if ls is None:
        return None 

    return cons(f(car(ls)), slist_map(cdr(ls), f))

def slist_scale(ls, s):
    return slist_map(ls, lambda x: x * s)

def slist_str(ls):
    t = [] 
    def f(x):
        t.append(str(x))

    slist_foreach(ls, f)

    return '[%s]' % (','.join(t))

#--------------------------------------------------------------

if __name__ == "__main__":
    ls = slist(10, 20, 30, 40)
    slist_str(ls) #[10,20,30,40]
    slist_len(ls) # 4
    slist_str(slist_map(ls, lambda x : x * x)) #[100, 400, 900, 1600]
