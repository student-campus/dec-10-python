'''#list in python 
a = [23,45,67,88,98] #creating of list 
print(a[0])
print(a[-1])
a.append(33) #used to add a value 
print(a)
a.extend([76,89]) #used to add the values at the end of list
print(a)
a.insert(2,0)
print(a)

num = [2,3,4,5,6,7]
name = ["sita", "Rita", "Hari","Shayam","Ram","Laxman","Prena"]
print(name[2:4:2])
num.remove(5)
print(num)

num.pop(2) #According to index
print(num)
 #index numnber deleted


print(type(num))

a = [7, 2, 3]
a.sort()
print(a)
a.reverse()
print(a)'''

#Tuple
ss = (2,3,4,5,6)
print(ss[0])
print(ss[-1])
print(ss[2:5])

t = ('a', 'b', 'c', 'd')
print(len(t))

t1 = (1, 2, 3)
t2 = (4, 5)
ti = t1 +t2
print(ti)

t = ((1, 2), (3, 4), (5, 6))
print(t[1][1])
lst = [34,56,78]
print(tuple(lst))