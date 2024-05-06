import random

while True:
     print("welcome to ROCK-PAPER-SCISSOR GAME")
     
     print("1. ROCK.")
     print("2. PAPER.")
     print("3. SCISSORS")
     
     user_choice=int(input("enter your choice: "))
     
     if user_choice == 1:
         choice_name= "ROCK"
     elif user_choice == 2:
         choice_name= "PAPER"
     else:
         choice_name= "SCISSOR"
              
             # print user choice
     print('User choice is \n',choice_name)
     
     print("now its computer turn........")
     
     if user_choice >=4 or user_choice<1:
         print("you entered invalid number, try again")
     else:
         computer_choice=random.randint(1,3)
         
         if computer_choice == 1:
             comp_choice_name = "ROCK"
         elif computer_choice == 2:
             comp_choice_name = "PAPER"
         else:
             comp_choice_name = 'SCISSOR'

         print("Computer choice is \n", comp_choice_name)


         print(choice_name,'Vs',comp_choice_name)
   
   
     if computer_choice==user_choice:
         print("its a draw")
     elif user_choice > computer_choice:
         print("you won ")
     elif computer_choice > user_choice:
         print("you lose.")
     elif computer_choice==1 and user_choice==3 :
         print("you lose.")
     elif user_choice==1 and computer_choice==3:
         print("you won ")
     
      
     print("Do you want to play again? (Y/N)")
     # if user input n or N then condition is True
     ans = input().lower()
     if ans =='n':
         break      
  
print("THANKS FOR PLAYING")


    