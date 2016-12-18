import time                                                
import timeit



class Foo(object):

    @timeit.timeit
    def foo(self, a=2, b=3):
        time.sleep(0.2)



@timeit.timeit
def f1():
    time.sleep(1)
    print 'f1'

@timeit.timeit
def f2(a):
    time.sleep(2)
    print 'f2',a

@timeit.timeit
def f3(a, *args, **kw):
    time.sleep(0.3)
    print 'f3', args, kw


f1()
f2(42)
f3(42, 43, foo=2)
Foo().foo()

