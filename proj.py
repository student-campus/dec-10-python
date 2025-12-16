#project 1: Snake , Water, Gun Game
'''
1 for snake
-1 for water
0 for gun
'''
computer = -1
youstr = input("Enter your choice ")
youDict = {"s":1 , "w":-1, "g":0}
you= youDict[youstr]
if(computer == you):
    print("Draw")
else:

     if(computer == -1 and you == 1):
         print("You win")
    
     elif(computer == -1 and you == 0):
         print("You loose!")
     elif(computer == 1 and you == -1):
         print("You loose!")

     elif(computer == 1 and you == 0):
         print("You win")
     elif(computer == 0 and you == -1):
         print("You win")
     elif(computer == 0 and you == 1):
         print("You lose")
     else:
         print("Something went wrong")
