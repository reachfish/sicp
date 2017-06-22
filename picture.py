# -- coding: utf-8 --
from scheme import *

#--------------------------------------------------------------
# vector
make_vector = cons
xcor = car
ycor = cdr
vector_str = cons_str

def vector_add(x, y):
    return make_vector(xcor(x) + xcor(y), ycor(x) + ycor(y))

def vector_scale(x, s):
    return make_vector(xcor(x) * s, ycor(x) * s)

#--------------------------------------------------------------
# segment 线段
make_segment = cons
seg_start = car
seg_end = cdr
#--------------------------------------------------------------
# rect 矩形
def make_rect(o, h, v):
    return slist(o, h, v)

def origin(rect):
    return car(rect)

def horiz(rect):
    return car(cdr(rect))

def vert(rect):
    return car(cdr(cdr(rect)))

#点对矩形的变换
def coor_map(rect):
    def f(p):
        return vector_add(origin(rect),  \
                vector_add( vector_scale(horiz(rect), (xcor(p))), \
                            vector_scale(vert(rect),  (ycor(p))))) 
    
    return f

#两点之间画线
def drawline(p1, p2):
    print "line: %s -> %s" % (vector_str(p1), vector_str(p2))

#对线段列表进行矩阵变换
def make_picture(seglist):

    def f(rect):
        slist_foreach(seglist, lambda x: \
                drawline(coor_map(rect)(seg_start(x)), coor_map(rect)(seg_end(x))))

    return f

#两张图并排放到矩阵中，横坐标比为a:1-a
def beside(p1, p2, a):

    def f(rect):
        p1(make_rect(origin(rect), vector_scale(horiz(rect), a), vert(rect)))
        p2(make_rect(vector_add(origin(rect), vector_scale(horiz(rect), a)), vector_scale(horiz(rect), 1 - a), vert(rect)))

    return f

#两张图并排放到矩阵中，纵坐标比为a:1-a
def above(p1, p2, a):

    def f(rect):
        p1(make_rect(origin(rect), horiz(rect), vector_scale(vert(rect), a)))
        p2(make_rect(vector_add(origin(rect) , vector_scale(vert(rect), a)), horiz(rect), vector_scale(vert(rect), 1-a)))

    return f


#--------------------------------------------------------------
if __name__ == "__main__":

    seglist = slist( make_segment(make_vector(3, 4), make_vector(1,7)), \
            make_segment(make_vector(2, 0), make_vector(3,5)), \
            make_segment(make_vector(4, 5), make_vector(7,9)), \
            )

    p1 = make_picture(seglist)
    p2 = make_picture(slist())

    rect = make_rect(cons(2, 5), cons(5,0), cons(0, 6))

    beside(p1, p2, 0.5)(rect)
    above(p1, p2, 0.4)(rect)

