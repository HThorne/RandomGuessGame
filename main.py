import random

while True:  
    random_num = random.randint(1,10)
  
    user_input = input("Choose a number from 1 to 10!\n")
  
    guess = int(user_input)
  
    if guess == random_num:
        print(f'\nYou chose {user_input}. Good guess, you win!')
    else:
        print(f'\nYou chose {user_input}. Sorry the number was {random_num}!')
    
    play_again = input("\nPlay again? (y/n):")
    print()
    if not play_again.lower().startswith("y"):
        break