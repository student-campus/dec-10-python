# while loop
i = 1
while i <= 10:
    print("inside loop")
    i = i + 1

j = 1
while j <= 10:
    print(j)
    j = j + 1
print("....." * 5)
a = [1, 2, 3, 4, 5, 5, 5, 65]
u = 0
while u < len(a):
    print(a[u])
    u = u + 1

e = 100
while e <= 200:
    if e % 2 == 0:
        print(i, "number is even")
    if e == 256:
        break
    e = e + 1
print("..." * 4)
import random

random_num = random.randint(1, 5)
print(random_num)
uu = 0
while True:
    uu = uu + 1
    user_input = int(input("Enter a number "))
    if random_num == user_input:
        print("successfuly guessed random number")
        again = input("Do you want to play againY/N")
        if again == "Y":
            random_num = random.randint(1, 5)
            print(random_num)
            uu = 0
        else:
            break
print(uu)

print("...." * 6)
for p in [1, 2, 3, 4]:
    for q in [5, 6]:
        print(p, q)
print("...." * 8)
i = 1
while i <= 10:
    print(i)
    i = i + 1

a = [1, 2, 3, 4, 5]
i = 0
while i < len(a):
    print(a[i])
    i = i + 1

j = 200
while j <= 300:
    if j % 2 == 0:
        print(f"{j} is even")
        if j == 256:
            break
    j = j + 1
