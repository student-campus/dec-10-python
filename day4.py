'''

lst5 = [1,2,3,4,5,7]
num = int(input("Enter the index number in list"))

if(-len(lst5)<=num and num<=len(lst5)-1):
    print(f'The index number exist which is {num} is {lst5[num]}')
else:
    print(f'The index number doesnot exist which is {num}')'''


'''ls1 = [1,2,2,3,5,4,6]
ls2 = ["Red","Green","Blue"]
print(ls1)
print(ls2)
print(len(ls1))'''

teachers = ["Nasir","Irfan","Haris","Sheraz","Farhan","Rafiq","Haris","Ihsan"]
print(teachers)

li1 = ["Apple","Banana","Cherry","Orange"]
li2 = [1,4,7,3,6,0,12,33]
li3 = [True, False, True, True,False]
li4 = [17.3,71.3,34.5,87.0,23.4]
print(teachers[3])
print(teachers[2:6])
print(teachers[1:5:1])
print(teachers[-7:-3])

teachers.append("Sita")
print(teachers)
teachers.insert(1,"Ram")
print(teachers)

teachers.extend([1,2,3,4,5,6])
print(teachers)

teacher = ["Ram","Hari","Sita","Rija"]
student = ["marks","subject"]
teacher_student = teacher + student
print(teacher_student)
del teacher[2]
print(teacher)
teacher.remove("Rija")
print(teacher)
teacher.pop(1)
print(teacher)
student.reverse()
print(student)
li2.sort()
print(li2)