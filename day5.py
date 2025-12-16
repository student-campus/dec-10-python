data = [1,2,3,4,5,6,7,8]
del data[1] #index
data.remove(3) #items of data
print(data)
data.pop() #last value of data 
data.pop(0) #index
print(data)

data = [1,2,3,4,[5,6,7,[8,9,0]]]
print(data[4][3][0])
print(data[-1][-1][0])