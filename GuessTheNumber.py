#  this is a guss the number game
import random as rand
print("GUSSING GAME")
print("Enter Yes to play the game")

def opt():
    global ans 
    ans = str(input("Do you want to play : [yes | no] "))

def game():
    MAX = 50
    guess = rand.randint(1,MAX)
    print("Guess the  between 1 and "+str(MAX))
    gameIn = str(input("Guess number > "))
    while gameIn!='q':
        
        if(gameIn!=str(guess)):
            print("try agin !")    
        else:
            print("Good job !")
            newGuss = str(input("Would you like to try another one [yes|no]"))
            if newGuss=="yes" :
                MAX=MAX*2
                print("Guess the  between 1 and "+str(MAX))
                guess = rand.randint(1,MAX)
        gameIn = str(input("Guess number > "))
        
opt()
if ans=='yes':
    game()
elif ans=='no':
    print("Good bay !")
else:
    print("Please answer either [Yes | no ] ,["+ans+"] is not alloed!")


