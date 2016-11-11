

class Complex:
    def __init__(self,real=0,img=0):
        self.real = real
        self.img = img
        print real,img
    def __str__(self):
        return "%d + j %d"%(self.real,self.img)
    def __add__(self,other):
        return Complex(self.real+other.real,self.img+other.img)
    def __getitem__(self,index):
        if index==0:
            return self.real
        elif index==1:
            return self.img
        else:
            raise Exception(" Invalid Index ")
    def __mul__(self,other):
        return Complex((self.real*other.real)-(self.img*other.img),(self.real*other.img)+(other.real*self.img))

a = Complex(1,2)
b = Complex(2,3)
# class Vector:
#     #write your code here :P
#
#
#


print __name__
if __name__ == '__main__':

    a = Complex(5,6)
    b = Complex(4,9)
    print a*b
    c = Complex()
    print a[1]

    print c
    print a+b
