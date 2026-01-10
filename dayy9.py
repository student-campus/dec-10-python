#function
'''
def test():
     <code block
     return
test()
'''

def sum(a,b): #function definition ,parameter
    return a+b
    
print(sum(2,3)) # function call, argument

def mult(d,f):
    return d*f
print(mult(4,5))

def analysis(name,maths_mark,science_mark,engl_mark):
    total_marks = maths_mark+science_mark+ engl_mark
    return total_marks
print(analysis(name='saru',maths_mark=99,science_mark=98,engl_mark=97))    

#keyword argument 
def student_detail(student,math,science,nepali):
    total = math + science + nepali
    avg = total/3
    result ={
        "name":student,
        "total": total,
        "avg":avg
    }
    return result
print(student_detail("saru",99,98,76))
#(positional argument, default argument)
def userinfo(fname, lname ="karki"):
    return f'my name is {fname}{lname}'
print(userinfo("saru"))
print(userinfo("sarru",".."))

def force(m,a=9.8):                                #default argument 
    return m*a
print(force(10))
print(force(14,18))

#arbitary positional argument 
#tuple is denoted by *
def test(*args):
    print(args)
    sum=0
    i=0
    for i in range(0,len(args)):
        sum = sum +args[i]
        i=i+1
    return sum

print(test(1,2,3,4))
print(test(1,2,3))
print(f'...'*3)

