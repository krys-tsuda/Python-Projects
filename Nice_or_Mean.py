#
# Python: 3.11.5
#
# Author: Krystle A. Tsuda
#
# Purpose:  The Tech Academy - Python Course, creating our first program together.
#           Demonstrating how to pass variables from function to function
#           While producing a functional game.
#
#           function_name(variable) _means that we pass in the variable.
#           return variable _means that we are returning the variable
#           back to the calling function.




def start(agree=0, disagree=0, player=""):
    player, opponent = describe_game(player)
    for question in questions:
        agree, disagree, player = agree_disagree(agree, disagree, player, opponent, question)
    end_game(agree, disagree, player, opponent)  # Add this line to end the game

    

def describe_game(player):
    if player != "":
        opponent = input("\nWho is your opponent? \n>>> ").capitalize()
        print("\nThank you for playing again, {}!".format(player))
    else:
        stop = True
        while stop:
            if player == "":
                player = input("\nPlayer, what is your name? \n>>> ").capitalize()
                opponent = input("\nWho is your opponent? \n>>> ").capitalize()
                if player != "":
                    print("\nWelcome, {} and {}".format(player, opponent))
                    print("\nIn this game, {} will be asked \na series of questions. \n If {} agrees with the majority, you win!".format(player, opponent))
                    print("If not, you loooose. \nSo tell me, would you rather...")
                    stop = False
    return player, opponent


questions = [
    {"option1": "Live forever with an eyelash in your eye...", "option2": "or spinach in your teeth?"},
    {"option1": "Be trapped in a romantic comedy with your enemies...", "option2": "or trapped in a horror movie with your friends?"},
    {"option1": "Always hit a red light for the rest of your life...", "option2": "or always get slow internet after sundown"},
    {"option1": "Be forced to sing every time you hear music...", "option2": "or dance every time you hear music?"},
    {"option1": "Jump like a rabbit wherever you go...", "option2": "or crawl like a baby?"},
    # Add more questions as needed
]



def agree_disagree(agree, disagree, player, opponent, question):
    stop = True
    while stop:
        show_score(agree, disagree, player)
        opt1 = question["option1"]
        opt2 = question["option2"]
        pick = int(input("\nWould you rather... \n1. {}, \n2. {}? (1/2) \n>>>: ".format(opt1, opt2)))

        if pick == 1:
            wouldYou = input("You'd rather {}.\n{}, do you agree? (Y/N) \n>>>: ".format(opt1, opponent)).lower()
            if wouldYou == "y":
                agree += 1
            elif wouldYou == "n":
                disagree += 1
            stop = False
        elif pick == 2:
            wouldYou = input("You'd rather {}.\n{}, do you agree? (Y/N) \n>>>: ".format(opt2, opponent)).lower()
            if wouldYou == "y":
                agree += 1
            elif wouldYou == "n":
                disagree += 1
            stop = False
        else:
            print("Invalid input. Please enter 1 or 2.")
    
    show_score(agree, disagree, player)
    return agree, disagree, player




def show_score(agree,disagree,player):
    print("\nScore for Player {}: Agree: {}, Disagree: {}".format(player, agree, disagree))



def score(agree,disagree,player):
    if agree > disagree:
        win(agree, disagree, player)
    elif disagree > agree:
        lose(agree, disagree, player)
    else:
        start() 



def win(agree,disagree,player,opponent):
    # Substitute the {} wildcards with our variable values
    print("\nNice job {} you win, \nor rather {} loses!".format(player,opponent))
    # call again function and pass in our variables
    again(agree,disagree,player)



def lose(agree,disagree,player,opponent):
    # substitute the {} wildcards with our variable values
    print("\nAhhh too bad {} loses, \nor rather {} wins!".format(player,opponent))
    # call again function and pass in our variables
    again(agree,disagree,player)



def again(agree,disagree,player):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(agree,disagree,player)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\Enter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")



def reset(agree,disagree,player):
    agree = 0
    disagree = 0
    #Notice, I do not reset the name variable as that same user has elected to play again
    start(agree,disagree,player)



def end_game(agree, disagree, player, opponent):
    if agree > disagree:
        win(agree, disagree, player, opponent)
    elif disagree > agree:
        lose(agree, disagree, player, opponent)
    else:
        print("\nIt's a tie!")  # Add a message for a tie   



if __name__ == "__main__":
    start()
