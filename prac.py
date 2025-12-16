student = { 
    "name" : "saru",
    "marks" : [98,99,97],
    "status" : "activate"
}
if(student["status"] == "activate"):
    total_marks = student["marks"][0]+student["marks"][1]+student["marks"][2]
    if(total_marks>=350):
        no_of_marks = len(student["marks"])
        print(no_of_marks)
        if(no_of_marks>=5):
            print(f'The student is eligible')
        else:
            print(f'The student is not eligible')