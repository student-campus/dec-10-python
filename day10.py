#def data(** kwags):

import datetime


def error_catching(**kwargs):
    if len(kwargs) == 0:
        return "please provide kwargs"
    elif "message" not in kwargs.keys():
        return "please provide message keys"
    message = kwargs.get("message")
    time = kwargs.get("time") if "time" in kwargs.keys() else ""
    level = kwargs.get("level") if "level" in kwargs.keys() else ""
    return f"{level} {message}-{time}"


time = datetime.datetime.now().strftime("%H:%M:%S")
print(error_catching(title="this is testing", author="", time=time))

import datetime


def report(**kwargs):
    if len(kwargs) == 0:
        return "please provide kwargs"
    elif "message" not in kwargs.keys():
        return "please provide message keys"
    message = kwargs.get("message")
    time = kwargs.get("time") if "time" in kwargs.keys() else ""
    level = kwargs.get("level") if "level" in kwargs.keys() else ""
    return f"{level} {message}-{time}"


time = datetime.datetime.now().strftime("%H:%M:%S")
print(report(title="this is testing", author="Name", date =time))


def student_info(*marks, **info):
    add =0
    for i in marks:
        add =add +i
        i=i+1
        avg = add/len(marks)
    return f' {avg} \n{info["name"]}'
print(student_info(40,50,69,80,name="saru",address =" Kathmandu"))





