# Design steps for slabs
# step1:
lx = float(input("Enter the length of slab along"))
ly = float(input("Enter the length of slab along"))
Grade_of_rebar = int(input("Enter the grade of rebar: "))
Grade_of_concrete = int(input("Enter the grade of concrete: "))
live_loads = float(input("Enter the loads on beam : "))
clearspan = float(input("Enter the clear span of beam:  "))
support_width = float(input("Enter the support width "))
size_of_slab = int(input("Enter the size"))
# from thumb rule criteria
if lx > ly:
    l = ly
else:
    l = lx
slab = ["cantilever_slab", "simply_supported_slab", "continuous_slab"]
for i in slab:
    if i == "cantilever_slab":
        d = l / 10
    elif i == "simply_supported_slab":
        d = l / 25
    else:
        d = l / 30
print(
    f"{l} is length of slab at smaller side and{d:.3f} is depth of slab from deflection criteria"
)
clear_cover = 0.02
diameter = int(input("Enter the diameter of rebar: "))
Total_depth = d + clear_cover + diameter / 2
print(f"Total_depth_{Total_depth}")
# step 3 :Find effective length
leffx = lx + (diameter / 2) + (diameter / 2)
leffy = ly + (diameter / 2) + (diameter / 2)
print(f"The effective length is {leffx}{leffy}")
# step4: Find load on slab
b = 1
Dead_load = 25 * b * Total_depth
Total_load = Dead_load + live_loads
factored_load = 1.5 * Total_load
# check the slab and calculate the bending moment
if (leffy / leffx) < 2:
    print("The slab is two way slab: ")
else:
    print("The slab is one way")
# for restrained slab
print(f"see the IS 456:2000 pg 91 Table 26 for restrained slab")
ax_positive = float(input("Enter the alpha x positive value: "))
ax_negative = float(input("Enter the alpha x negative value: "))
ay_positive = float(input("Enter the alpha y positive value: "))
ay_negative = float(input("Enter the alpha y negative value: "))
bending = {
    "bending_moment_x_positive": ax_positive * Total_load * (leffx**2),
    "bending_moment_y_positive": ay_positive * Total_load * (leffy**2),
    "bending_moment_x_negative": ax_positive * Total_load * (leffx**2),
    "bending_moment_y_negative": ay_positive * Total_load * (leffy**2),
}
import math

dia = 10  # mm
area_of_one_rebar = (math.pi * (dia**2)) / 4
for i in bending.values():
    q = 0.87 * Grade_of_rebar
    w = Grade_of_rebar / (b * Grade_of_concrete)
    r = q * w
    t = q * d
    area = (t - math.sqrt((t**2) - 4 * i * r)) / (2 * r)
    spacing = ((area_of_one_rebar) / (area)) * 1000
    space = min(3 * d, 300, spacing)
    area_provided = (area_of_one_rebar) / space
    print(area)
    print(spacing)
    print(space)
    print(area_provided)
    if area_provided > (0.12 / 100) * b * Total_depth:
        print(f"The area is ok")
