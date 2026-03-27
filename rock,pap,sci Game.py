"""
WORKFLOW OF THE GAME
1-enter user choice (Rock,Paper,Scissor)
2-enter computer choice (computer choose randomly not conditionally)
3-print result

3Cases
A - Rock
Rock - Rock = tie
Rock - Scissor - Rock Win
Rock - Paper - Paper Win

B - Paper
Paper - Paper = tie
Paper - Rock = Paper Win
Paper - Scissor = Scissor Win

C - Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock Win
Scissor - Paper = Scissor Win

"""

import random 
item_list = ["Rock", "Paper", "Scissor"]
user_choice = input("Enetr your move= Rock, Paper, Scisor= ")
comp_choice = random.choice(item_list)
print(f"User choice= {user_choice}, computer choice == {comp_choice}")

if user_choice == comp_choice:
    print("Both choices are same:= Match tie")
elif user_choice == "Rock" :
    if comp_choice =="Scissor" :
       print("Rock smashes scissor ,You Win")
    else:
       print("Paper covers rock ,You Lose")
elif user_choice == "Paper" :
    if comp_choice =="Rock" :
      print("Paper covers Rock,You Win")
    else: 
      print("Scissor cuts Paper, You Lose")

elif user_choice == "Scissor" :
    if comp_choice == "Rock" :
      print("Rock smashes Scissor, You Lose")
else:
       print("Scissor cuts Paper, You Win")                              
