#Q13
re=int(input('enter the real number: '))
im=int(input('enter the imaginary number: '))
print('re={} im={}'.format(re,im))


#Q14
def input_complex():
    re=int(input('enter the real number: '))
    im=int(input('enter the imaginary number: '))
    return re,im

def print_complex(re,im):
    print('re={} im={}'.format(re,im))
s = input_complex()
print(s)
print_complex(10,20)


#Q15
def add(re1,im1,re2,im2):
    return re1+re2,im1+im2

def sub(re1,im1,re2,im2):
    return re1-re2,im1-im2

a=add(10,20,5,-10)
print('addition is: ',a)
s=sub(10,20,5,-10)
print('subtraction is: ',s)


#Q16
def conj(re,im):
    return re,-im
def mul(re1,im1,re2,im2):
    return re1*re2,im1*im2
def div(re1,im1,re2,im2):
    return re1//re2,im1//im2

c=conj(5,3)
print('conjugate is: ',c)
m=mul(10,20,5,-10)
print('multiplication is: ',m)
d=div(10,20,5,-10)
print('division is : ',d)