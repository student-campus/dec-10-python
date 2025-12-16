#Dictionary {key:value pairs
dict = { 
    "name" : "shardha",
    "cgpa" : 9.6,
    "marks" : {98,97,95}
    
}

info = {
    "key" : "value",
    "words": "meaning",
    "learning":"coding",
    "subjects":["python","Java","C","C++"]

}
print(info)
print(type(info))#dictionary doesnot have index cant create duplicate keys
print(info["key"])
print(info["subjects"])
info["name"] = "caste"
print(info)
 
null_dict = {}
print(null_dict)
null_dict["score"] = [3,4,5]
print(null_dict)

#nested dictionary
student = {
    "name": "Shardha",
    "score": {
        "chem":87,
        "phy":98,
        "Eng":90
    }
}
print(student["score"]["chem"])
print(student.get("name"))
print(student.keys())
print(student.items())
print(student.values())

#lists 
marks_of_students = [98,90,78,76]
print(sum(marks_of_students))
print(max(marks_of_students))
print(min(marks_of_students))
print((98+76)/2)
'''
le = []
l1 = int(input("enter the number"))
le.append(l1)
l2 = int(input("enter the number 2nd"))
le.append(l2)
i=0
for i in range(len(le)):
    if(le[i]%2 == 0):
        print("The number is even.",le[i])
    else:
        print("The number is odd.",le[i])
    if(le[i]>0):
        print("The number is positive.")
    elif(le[i]<0):
        print("The number is negative.")
print(le)
le.sort()
print(le)'''

#dictionary
student = {
    "Ram" : 78,
    "hari" : 98,
    "Ramesh" : 90
}
print(student)
student["Sita"] = 90
print(student)
print(student.keys())
print(student.values())
max_val = max(student.values())
print(max_val)
min_val = min(student.values())
print(min_val)
print(sum(student.values())/len(student))