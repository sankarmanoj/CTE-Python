a=4
def double(x):
    return x*2
def triple(x):
    return x*3
def square(x):
    global a
    a= x(a)

def half():
    global a
    a = a/2
print a
square(triple)
print a
square(double)
print a
half()
print a
