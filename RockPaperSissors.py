import random
options_comp=['r',
'p',
's']
while True:
 comp=random.choice(options_comp)
 user_choice=input("Enter 'r' for rock, 'p' for paper and 's' for sissors (or q to quit the game) : ")
 user_choice=user_choice.lower()
 if user_choice=="q":
     print("You quitted the game")
     break
 if user_choice=="r" or user_choice=="p" or user_choice=="s":
   if comp==user_choice:
	   print("Game draw!")
   elif comp=="p" and user_choice=="s":
	   print("You win!")
   elif comp=="s" and user_choice=="p":
	   print("You lose!")
   elif comp=="r" and user_choice=="s":
	   print("You lose!")
   elif comp=="s" and user_choice=="r":
	   print("You win!")
   elif comp=="p" and user_choice=='r':
	   print("You lose!")
   elif comp=="r" and user_choice=="p":
	   print("You win!")
 else:
	  print("Following input option is irrelvent to the games input!")
	  print("You may like to try again: ")
	  user_choice=input("Enter 'r' for rock, 'p' for paper and 's' for sissors : ")
 print("Computer choose: ",comp)
 print("Player choose: ",user_choice)


