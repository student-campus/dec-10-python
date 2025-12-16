#dict
student = {
    "id" : 101,
    "name":"saru",
    "age" : 22,
    "course" : "python",
    "marks" : [78,85,90],
    "is_activate" : True
}
print(student["name"])
print(student.keys())
print(student.values())
student['num'] = [98062,9822]
student ["num2"] ="980"
student["age"] = 12
print(student)
student.update({"name":"Hari","num":123}) #add or update the existing data 
print(student) # mutable type list and dictionary but dict dont have same keys 
# dict is in the form of keys: values separated by comma with curly braces


#removing of data
del student["course"] #remove according to keys
student.pop("name") #remove the data according to keys
student.popitem() #remove last key value pair
print(student)
print(student.get('age','Not found'))

student = {
    "id": 101,
    "name": "Sudan",
    "age": 22,
    "course": "Python",
    "marks": [78, 85, 90],
    "is_active": True,
    "num":{
        "ntc":980,
        "ncell":{
            "telecom":"nepal"
        }
    }
}
print(f'{student["name"]} total marks is {(student["marks"][0]+student["marks"][1]+student["marks"][0])} and his best course is {student["course"]}')