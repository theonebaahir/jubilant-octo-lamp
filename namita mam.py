import random
import time
number = random.randint(1,100)

def intro():
    print("may I ask you to play a game with me")

    global name
    name = input(int)
    print(name+",we are going to play a game.I am thinking of a number between 1 to 100")
    if(number%2==0):
        x = 'even'
    else:
        x ='odd'
    print("/nThis an {} number".format(x))
    print("go ahead. guess!")


def pick():
        guessesTaken = 0
        while guessesTaken < 6:
            time.sleep(.25)
            enter= input("Guess: ")
            try:
                
                
                
                guess = int(enter)
                if guess<=100 and guess>=1:
                    if guessesTaken<6:
                        if guess<number:
                            print("the guess of the number that you have entered is too low ")
                            if guess>number:
                                
                                print("the guess of the number that have you entered is too high")
                        if guess != number:
                            time.sleep(.5)
                            print("try again")    
                        if guess == number:
                            break
                if guess>100 or guess<1:
                    print("silly goose! That number isn't in the range")
                    time.sleep(.25)  
                    print("Please enter a number between 1 and 100")
            except:
                print("I don't think that"+enter+" is a number")  
                    
                guessesTaken = str(guessesTaken)
                print("'good job{}you guessed it right you gusses my number{} ".format(name, guessesTaken))
                if guess != number:
                    print("nope the number I was thinking of '+str(number)")
                    playagain = "yes"
                    while playagain=="yes" or playagain=="y" or playagain=="Yes":
                        intro()
                        pick()
                        print("Do you want to play again")
                        playagain = input()
                

                