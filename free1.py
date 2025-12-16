def check_win(player, computer):
    print(f"You chose {player} computer chose  {computer}")
    if player == computer:
        return "It's a tie."


check_win("rock", "paper")
age = 25
print(f"Jim is {age} years old")

# else and elif statement
age = 20
if age >= 18:
    print("\nYou are an adult")
elif age > 12:
    print("You are a teenager.")
elif age > 1:
    print("You are a child. ")
else:
    print("You are a baby. ")

print("Sardha ",end="Kharpa")
''' multi-line comment. '''

#arithmetic operators
a=5
b=2
sum = a+b

#type conversion
a="2"
b=5.3
print(a.isnumeric())
e=int(a)
print(e)

c=2.333
d=int(c)
print(d)
r=5.6
s=str(r)
print(type(s))

name=input("Enter your name: ")
print(name)
#input value is always string 