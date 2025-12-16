#logical operator 
a=3
b=2
print(a>b)
print(1==1)
if(a>b):
    print("The value is true")
print("and",True and False)
print("and", False and True)
print("or", True or False)
print("or", True and True )
#return the value in bool of logical operator

data= True
data = not (data)
if data:
    print("this is true")
    data = 'this is world'
    a=a+1
    print(a)
else:
    print("iam else")



department = input("Enter the department: ")
experience =int(input("Enter the years of experiences: "))
performance_score = float(input("Enter the performance score: "))
initial_salary = float(input("Enter your initial salary: "))
if(department=="It"):
    if(experience>5):
          if(performance_score >=90):
              print("bonus is 20%")
              print(f'The salary after bonus is {0.2*initial_salary +initial_salary}')
          elif(performance_score<89 and performance_score>70):
               print("The bonus is 12%")
               print(f'The salary after bonus is {0.12*initial_salary +initial_salary}')
          else:
                 print("bonus=5%")
                 print(f'The salary after bonus is {0.05*initial_salary +initial_salary}')
    else:
         if(performance_score>=85):
              print("THe bonus is 10%")
              print(f'The salary after bonus is {0.1*initial_salary +initial_salary}')
         else:
              print("The bonus is 3%")
              print(f'The salary after bonus is {0.03*initial_salary +initial_salary}')
elif(department == "Hr"):
    if(performance_score >=80):
        if(experience >3):
            print("The bonus is 15 %")
            print(f'The salary after bonus is {0.15*initial_salary +initial_salary}')
    else:
        print("The bonus is 7%")
        print(f'The salary after bonus is {0.07*initial_salary +initial_salary}')
elif(department =="Any"):
    if(experience>=4):
        print("THe bonus is 6%")
        print(f'The salary after bonus is {0.06*initial_salary +initial_salary}')
    else:
        print("THe bonus is 2%")
        print(f'The salary after bonus is {0.02*initial_salary +initial_salary}')
