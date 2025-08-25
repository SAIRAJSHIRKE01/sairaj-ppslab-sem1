# import pyttsx3
# engine = pyttsx3.init()
# engine.say("loooooluuuuuuluuuuluuliooooooloooooloooolyyluullllololoooollluuuuuuuuuuulooooolollluuuuuluuuuulluouluouluouiuluouluuuouluouluouluoouuouluouluouluo")
# engine.runAndWait()

# Rock Paper Scissors using if-elif

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game = [rock , paper , scissors]
player1 = int(input("your choice 0 for rock ,1 for paper ,2 for scissors\n"))
system_choice = random.randint(0 ,2)
player2 = game[system_choice]
print(system_choice)

if player1 == player2:
    print("It's a draw!")

elif player1 == game[0] and player2 == game[2]:
    print("Player 1 wins! Rock crushes Scissors.")

elif player1 == game[2] and player2 == game[1]:
    print("Player 1 wins! Scissors cut Paper.")

elif player1 == game[1] and player2 == game[0]:
    print("Player 1 wins! Paper covers Rock.")

elif player2 == game[0] and player1 == game[2]:
    print("Player 2 wins! Rock crushes Scissors.")

elif player2 == game[2] and player1 == game[1]:
    print("Player 2 wins! Scissors cut Paper.")

elif player2 == game[1] and player1 == game[0]:

    print("Player 2 wins! Paper covers Rock.")

else:
    print("Invalid input! Please choose Rock, Paper, or Scissors.")
