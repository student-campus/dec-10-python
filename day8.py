for i in [1, 2, 3, 4]:
    for j in [5, 6]:
        print(i, j)
i = 1
while i <= 10:
    print(i)
    i = i + 1

a = [1, 2, 3, 4, 5, 5, 5, 65]
h = 0
while h < len(a):
    print(a[h])
    h = h + 1

y=200
while(y<300):
    if(y%2==0):
        print(f'{y} is even')


"""import random
random_num  =random.randint(1,15)
i=0
print(random_num)
while True:
    user_input = int(input("enter a number "))
    i=i+1
    if random_num == user_input:
        print("successfully guessed random number")
        again = input("Do you want to play again Y/N")
        if(again == "Y"):
            random_num =random.randint(1,15)
            print(random_num)
            i=0
        else:
            break
print(f'attempt:{i}')"""

import random

random_num = random.randint(1, 5)
print(random_num)
guess_count = []
i = 0
while True:
    user_input = int(input("Guess the number "))
    i += 1
    if random_num == user_input:
        print("Right")
        play_more = input("Do you want to play more? Y/N ").upper()
        if play_more == "Y":
            guess_count.append(i)
            random_num = random.randint(1, 5)
            print("again ....", random_num)
            i = 0
        else:
            guess_count.append(i)

            break

print(f"attempt: {i}")
print(f"history attempt: {guess_count}")
if i > 1:
    print(f"")
