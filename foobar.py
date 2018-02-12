'''
def bar(x,y):
    for i in range (x, y+1):
        for h in range (1, i):
            if (h * h) == i:
                print i, "is a perfect square", "of", h
'''

'''
def foo(x,y):
    for i in range (x, y+1):
        for h in range (2, i):
            if i % h == 0:
                break
            if i == check:
                break
            if h < i - 1:
                continue
            else:
                check = i
                print i, "is prime"
'''


def foobar(x, y):
    check = 0
    for i in range (x, y+1):
        for h in range (2, i):
            x = 0
            if (h * h) == i:
                #print i, "is a perfect square", "of", h
                print "bar", i
                x = 1
            if i % h == 0:
                if x != 1:
                    print "foobar", i
                break
            if i == check:
                break
            if h < i - 1:
                continue
            else:
                check = i
                print "foo", i
    
foobar(100, 100000)