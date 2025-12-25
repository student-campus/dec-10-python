# Tuples
#immutable data type
#cannot use the rules of list
#it has index 
#to add or convert type conversion is done
a = (1,2,3,3,4)
print(a[0])
print(type(a))
a=list(a)
a.pop()
print(tuple(a))
#if data is not changed 
#list data is changed in running

# in sets values are in curly bracket separated by comma
# in sets data are in unordered
s= [1,2,34,5,"name",1,2,2,2]
b=set(s)
b.remove(2)
print(list(b))
#to remove duplicate data 