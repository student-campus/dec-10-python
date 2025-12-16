# step 1 : Given
# Grade of concrete, Grade of rebars, clear span , load, support width
fck = int(input("Enter the grade of concrete in N/mm2:  "))
fy = int(input("Enter the grade of rebar in N/mm2:  "))
l = float(input("Enter the clear span of beam in m:  "))
su_wd = 230 #in mm
''' Find the depth of beam '''
beam = ["cantilever beam", "simply supported beam","continuous beam"]
if (beam[0]):
    print(d=l/10)
elif(beam[1]):
    print(d=l/15)
elif(beam[2]):
    print(d=l/25)