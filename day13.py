try:
    print(a)
  
except NameError:
    print("name error")
except TypeError as e:
    print(e)
except:
    print("something went wrong")
'''
def test():
    <code block>
    return 1,2,3
    '''
def test():
    
    return ("This_is_inside_func")
print(test())

def sum(a,b):
    return a+b
print(sum(2,6))
# Positional argument 
def mul(y,u):
    return y*u
print(mul(7,8))

def student(student_name,math_marks,science_marks,english_marks,attendence_percentage):
    avg= (math_marks+science_marks+english_marks)/3
    return f'The average is {avg}'
print(student("Saru",99,98,97,78))

#keyword argument
def result(percentage,math,science,social):
    return f'The marks is {math},{science},{social}'
print(result(math = 88, science= 98, social=95,percentage = 77))

#default argument
def force(m,g=9.8):
    f=m*g
    return f

print(force(10))
print(force(78))

def userinfo(fname,lname = "Karki"):
    return f'my name is {fname} {lname}'
print(userinfo("Saru"))

def test(*a):
    sum =0
    for i in a:
        sum = sum+i
    return f'This is inside funct {a},{sum}'
print(test(1,2,3))
print(test(1,2,45,5,6))

def data(**kwags):
    print(kwags)
data(a=10,b="test",c=11)        # saved in dictionary form

