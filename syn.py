#Conditional Statement
''' if elif else (syntax)
if(condition):
   code block
elif(condition):
    code block
else:
    code block
    '''
'''light = "green"
if (light == "red"):
    print("stop")
elif(light == 'green'):
    print("go")
elif(light == "yellow"):
    print("look")
print("end of code.")

age = 12
if age >= 18:
    print("can vote")
else:
    print("cannot vote.")

marks = int(input("Enter the marks of a student:"))
if (marks >= 90):
    print(f'The grade of student is A')
elif (marks <90 and marks >=80):
    print(f'The grade of student is B')
elif (marks <80 and marks >=70):
    print(f'The grade of student is C')
elif (marks>70 ):
    print(f'The grade of student is D')

# WAP to check if a number entered by the user is odd or even.
num = int(input("Enter the number: "))
if (num%2 == 0):
    print("The number is even ", num)
else:
    print("The number is odd", num)

#WAP to find the greatest of 3 number entered by the user.
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))
if a>b>c:
    print(f'The greatest number is {a}')
elif b>a>c:
    print(f'The greatest number is {b}')
else:
    print(f'The greatest number is {c}')'''

#WAP to check if a number is a multiple of 7 or not 
n = int(input("Enter the number: "))
if(n%7 == 0):
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7")