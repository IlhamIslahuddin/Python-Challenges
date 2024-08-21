import random

def prisoners_dilemma():
    decision = ["confess","stay silent"]
    print ("The 'Prisoner's Dilemma' is the choice between you, who in this scenario is a prisoner, and another prisoner.")
    print ("You are given the option to either confess or stay silent.")
    print ("If one of you choose to confess and the other prisoner chooses to stay silent, the one who confessed is released and the other prisoner stays in prison for 20 years.")
    print ("If you both choose to stay silent, you both stay in prison for only 1 more year.")
    print ("If you both choose to confess, you will both stay in prison for 5 years each.")
    playing = True
    while playing == True:
        valid = False
        com_choice = random.choice(decision)
        while valid == False:  
            user_choice = str(input("Do you choose to stay silent or confess? ").lower())
            if user_choice != "stay silent" and user_choice != "confess":
                print ("Choice not recognised. Try again.")
            else:
                valid = True
                print (f"You chose to {user_choice}.")
                if user_choice == "stay silent" and com_choice == "silent":
                    print ("The other prisoner chose...")
                    print ("To stay silent.")
                    print ("With both of you choosing to stay silent, you will both stay in prison for only 1 more year.")
                elif user_choice == "confess" and com_choice == "silent":
                    print ("The other prisoner chose...")
                    print ("To stay silent.")
                    print ("Since you chose to confess and the other prisoner chose to stay silent, you will be released from prison and the other prisoner will receive 20 years.")
                elif user_choice == "stay silent" and com_choice == "confess":
                    print ("The other prisoner chose...")
                    print ("To confess.")
                    print ("Since the other prisoner chose to confess and you chose to stay silent, the other prisoner will be released and you will receive 20 years.")
                elif user_choice == "confess" and com_choice == "confess":
                    print ("The other prisoner chose...")
                    print ("To confess.")
                    print ("Since you both chose to confess, you will both receive 5 more years in prison each.")
                play_again = input("Would you like to play again? Yes or No ").lower()
                if play_again == "no":
                    playing = False
                elif play_again != "yes" and play_again != "no":
                    print ("Input not recognised. Ending game...")
                    playing = False

if __name__ == "__main__":
    prisoners_dilemma()
