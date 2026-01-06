f= open("day.txt","w")
f.write("This the writing formate used in txt")
def handle_error(message,file):
    f= open(file,'a')
    f.write(message)
    f.close()


try:
    print(aa)
except NameError as e:
    handle_error(str(e),'name.txt')
    
except TypeError as e:
    handle_error(str(e),'typeerror.txt')
    
except:
    handle_error("something went wrong",'error.txt')
   

