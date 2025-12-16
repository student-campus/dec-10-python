'''student = {
    "id" : 101,
    "name":"saru",
    "age" : 22,
    "course" : "python",
    "marks" : [100,150,100],
    "is_activate" : True
}'''







student = { 
    "name" : "saru",
    "marks" : [100,150,100],
    "status" : "activate"
}
if(student["status"] == "activate"):
    total_marks = student["marks"][0]+student["marks"][1]+student["marks"][2]
    if(total_marks<=350):
        no_of_marks = len(student["marks"])
        print(no_of_marks)
        if(no_of_marks>=5):
            print(f'The student is eligible')
        else:
            print(f'The student is not eligible')


exam_score = {
    "maths" : 98,
    "science" : 99,
    "ph" : 98,
    "physic" : 78,
    "geo" : 90,
    "eco" : 97
}
if(exam_score["maths"]>=65 and exam_score["science"]>=65 and exam_score["ph"]>=65 and exam_score["physic"]>=65 and exam_score["geo"]>=65 
   and exam_score["eco"]>=65):
    print("The score is average score")
elif(exam_score<40):
    print("no score")