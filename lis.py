#string are unmutable (that cannot change.)
#list are mutable (that can change.)
# #It can store string , integer , float etc.
student = ["Teena" , "Reena", "Sita","Ram"]
Teena_marks = [97,67,89,43]
Reena_marks = [89,97,76,45]
Sita_marks = [90,66,76,85]
Ram_marks = [76,88,53,73]
print(type(student))
Teena_total_marks = sum(Teena_marks[0:])
Reena_total_marks = sum(Reena_marks[0:])
Sita_total_marks = sum(Sita_marks[0:])
Ram_total_marks = sum(Ram_marks[0:])
percentage_of_Teena = (Teena_total_marks/400)*100
percentage_of_Reena = (Reena_total_marks/400)*100
percentage_of_Sita = (Sita_total_marks/400)*100
percentage_of_Ram = (Ram_total_marks/400)*100
print(percentage_of_Teena )
print(percentage_of_Reena)
print(percentage_of_Ram)
print(percentage_of_Sita)
print(Teena_marks[3])
print(len(Teena_marks))

mark = [90,87,76,66]
print(mark[-4:-1])
# method of list
mark.append(88)
print(mark)
mark.sort()
print(mark)
mark.reverse()
print(mark)
mark.insert(3,87)
mark.remove(87) #in remove we remove according to element
print(mark)
mark.pop(1) #in pop we remove according to index
print(mark)

#Tuples in Python 
# A built-data type that lets us create immutable sequences of values.
tup = (2,1,3,1)
print(type(tup))
print(tup[0])
print(tup[1])
# this cannot be formed tup[4]=0
tupp=(1)
print(tupp)
print(type(tupp))
tuppl = (1,)
print(type(tuppl))
#slicing within the tupple
print(tup[1:3])

#Two method of tupple
tupple = (2,1,3,1)
#tupple.index method
#tupple.count method
print(tupple.index(2)) #2 is in index 0 
print(tupple.count(1)) #2 times the 1 occur in tupple 
'''
# WAP to ask the user to enter names of their favourite movies and store them in list.
movie = []
us1 = input("Enter your favourite movie: ")
movie.append(us1)
us2 = input("Enter your favourite movie: ")
movie.append(us2)
us3 = input("Enter your favourite movie: ")
movie.append(us3)
print(movie)'''

# WAP to check if a list contains a palindrome of elements.
#Reading from beginning and ending is same.
# like maam
li = [1,2,3,2,1]
li2 = [1,2,3]
copy_list1 = li2.copy()
copy_list1.reverse()
if copy_list1 == li2:
    print("palindrome. ")
else:
    print("The number is not palindrome.")

# WAP to count the number of students with the "A" grade in the following tuple.
Grade = ["C","D","A","A","B","B","A"]
Grade.sort()
print(Grade)

