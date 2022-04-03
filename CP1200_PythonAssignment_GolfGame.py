"""
Golf Game Assignment 1
Name: Riya Sen
Student ID: 13106631
Date Started: 6th April,2015
Last Date Modified: 27th April,2015

This program creates golf console for the user. It calculates the distance to the hole accordingly.The player chooses a club and then the program generates the distance hit for
each shot, updating and then the program informs the user of their score. The play goes on until the ball reaches the hole.

Pseudocode:

print golf game calculator
print welcome message

function Menu():
    Asks the user to enter the menuChoice and get it in the menu choice variable
    return menuChoice

import random function
function playRound():
    print clubSelection instructions
    hole=230
    trail=0
    while hole!=0:
        get input for clubSelection
        if clubSelection=='d' or clubSelection=='D' then:
            shotHit= random.randint(80,100)
            if hole>0 then:
                hole= hole - shotHit
            else:
                hole= hole + shotHit
            trial= trial + 1
            print the results mentioning how far you are from the hole after the number of trials
            print new line

        elif  clubSelection=='i' or clubSelection=='I' then:
            shotHit= random.randint(1,30)
            if hole>0 then:
                hole= hole - shotHit
            else:
                hole= hole + shotHit
            trial= trial + 1
            print the results mentioning how far you are from the hole after the number of trials
            print new line

        elif clubSelection=='p' or clubSelection=='P' then:
            shotHit=random.randint(1,10)
            if hole>0 then:
                hole= hole - shotHit
            else:
                hole= hole + shotHit
            trial= trial + 1
            print the results mentioning how far you are from the hole after the number of trials
            print new line

        else:
            print invalid button pressed

    print("Clunk! After ",trial," hits, the ball is in the hole!")
    if trial<=5 then:
        print("Congratulations. You are",5-trial,"under par.",sep='')

    else:
        print("Dissapointing. Your are",trial-5,"over par.",sep='')


function main():
    print welcome message
    while True:
          Choice= Menu()
          get Choice
          if Choice == 'I' or Choice == 'i' then:
             print(" INTRUCTIONS: It's golf on your console. \n\
             For each shot, you may use a driver, iron, or a putter- each shot will vary in \n\
             distance. The average distance each club can hit is: Driver= 100m, Iron= 30m, Putter= 10m")
          else if Choice == 'p' or Choice == 'P' then:
             playRound()
          else if  Choice == 'Q' or Choice == 'q' then:
             print Thanks for playing!
             break   
          else:
             print invalid menu choice

execute main()
"""


#this function consist of the options in the main menu.    
def Menu():
    
    menuChoice = input("Golf! \n\
Menu: \n\
(I)nstructions. \n\
(P)lay Round. \n\
(Q)uit. \n")
    return menuChoice


#random function is used to pick a random number in a given range
#this function calculates the distance between the clubs
#and generates the results accordingly
import random
def playRound():
    print("This hole is 230m par 5. \n\
Club Selection: press D for Driver, I for Iron, P for Putter.\n")
    hole=230
    trial=0
    while hole!=0:
        clubSelection=input("Press a button to take a shot:")
        if clubSelection=='d' or clubSelection=='D':
            shotHit= random.randint(80,100)
            if hole>0:
                hole= hole - shotHit
            else:
                hole= hole + shotHit
            trial= trial + 1
            print("Your shot went ",shotHit," m.\n "," You are ",hole,"m away from the hole, after ",trial," shots/s.",sep='')
            print()

        elif  clubSelection=='i' or clubSelection=='I':
            shotHit= random.randint(1,30)
            if hole>0:
                hole= hole - shotHit
            else:
                hole= hole + shotHit
            trial= trial + 1
            print("Your shot went ",shotHit," m.\n "," You are ",hole,"m away from the hole, after ",trial," shots/s.",sep='')
            print()

        elif clubSelection=='p' or clubSelection=='P':
            shotHit=random.randint(1,10)
            if hole>0:
                hole= hole - shotHit
            else:
                hole= hole + shotHit
            trial= trial + 1
            print("Your shot went ",shotHit," m.\n"," You are ",hole,"m away from the hole, after ",trial," shots/s.",sep='')
            print()

        else:
            print("Invalid button; Please press again.")

    print("Clunk! After ",trial," hits, the ball is in the hole!")
    if trial<=5:
        print("Congratulations. You are",5-trial," under par.",sep='')

    else:
        print("Dissapointing. Your are",trial-5," over par.",sep='')

        

#this is the main function, which prints the welcome message and also
#gets input from the users         
def main():
    print("Let's Play Golf... In CP1200 Style.! \n\
           Presented By: Riya Sen, March 2015. \n")
    while True:
        Choice=Menu()
        if Choice == 'I' or Choice == 'i':
            print("INTRUCTIONS: It's golf on your console. \n\
For each shot, you may use a driver, iron, or a putter- each shot will vary in \n\
distance. \n\
The average distance each club can hit is: Driver= 100m, Iron= 30m, Putter= 10m")

        elif Choice == 'p' or Choice == 'P':
            playRound()
            
        elif Choice == 'q' or Choice == 'Q':
            print(" Thanks for playing! ")
            break

        else:
            print("Invalid Menu Choice.")

        
            
main()
