#for loop is finite (range)
'''
for i in <sequence>
   <code block>
'''

for data in [1,2,3,4,5,6,7]:
    if(data%2!=0):
        print(f'{data} is odd')
    
print("________________________"*5)
    
for name in ("saru"):
    print(name)

data ={
    "name":"Saru",
    "address":"kirtipur"
}
for i in data.values():
    print(i)
for j in data.keys():
    print(j)

#range is always numeric 
for y in range(1,100,1): # doesnot print 100 increament by 1 
    print(y)

print("......"*5)

for u in range(5):
    print(u) #starts from 0

for p in range(150,200):
    if(p%2==0):
        print(p)
    p=p+1

string_list =[
    "python_programming",
    "learn_data_science",
    "backend_development",
    "full_stack_development",
    "object_oriented_prog"
]
'''for w in range(len(string_list)):
    print(string_list[w])'''

for s in range(1,10):
    if s==5:
        print("five")
        break # break close entire program
    print(i)

for h in range(1,10):
    if h ==5:
        print("Five")
        continue #continue doesnot print 5 but five
    print(h)
      
