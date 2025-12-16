#lists
number = [1,2,3,4,5,7,6]
num = [45,76,98]
number.append(10)
number.insert(3,30)
number.extend([33,44,55])
total = number + num 
del num[2]
print(num)
number.remove(7)
print(num)
print(total)