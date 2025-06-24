
import random

game = ["rock", "paper", "siccers"]


computer = ""



your_score = 0
computer_score = 0


shart_bazi = True


while(shart_bazi):

    user = input("CHOOSE (ROCK OR PAPER OR SICCERS ? )")

    rand = random.randint(0,2)
    computer = game[rand]


    
    if user=="rock" and computer=="paper" :
        your_score = your_score+1

    if user=="rock" and computer=="paper" :
        computer_score = computer_score+1



    if user=="paper" and computer=="rock":
        your_score=your_score+1



    if user=="paper" and computer=="siccers":
        computer_score=computer_score+1


    if user=="siccers" and computer=="rock":
        computer_score=computer_score+1



    if user=="siccers" and computer=="paper":
        your_score=your_score+1



    if your_score>=3 or computer_score>=3 :
        shart_bazi = False


    print("YOU: (", your_score  ,")",   user,"     COM:(", computer_score  ,")",computer)


    

print("YOU :", your_score)
print("COMPUTER :", computer_score)


if your_score>computer_score :
        print("YOU WINNNN!!")
        
else :
    print("YOU LOSE!")
