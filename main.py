import random

def validate_input(user_input):
    if not user_input.isdigit():
        print("Invalid input! Enter a number between 1 and 100! ")
        return False
        
    input_number = int(user_input)
    if input_number < 1 or input_number > 100:
        print("Invalid input. Try again. Your guess should be between 1 and 100!")
        return False
    
    return True 

def start_game():
    rand_num = random.randint(1, 100)
    score = 100

    while True:
        user_input = input("Welcome to the game! Please enter a number between 1 and 100: ")

        if user_input.lower() == "q":
            print("Thank you for playing. Goodbye!")
            break

        if not validate_input(user_input):
            continue

        input_number = int(user_input)
        if input_number > rand_num:
            print("Your guess is higher than the answer!")
            
        
        elif input_number < rand_num:
            print("Your guess is lower than the answer!")
            
        else:
            print(f"You guessed correctly! Your score is: {score}")
            wanna_play = input("Do you want to play again? (y/n)")
            if wanna_play.lower() == "y":
                rand_num = random.randint(1, 100)
                score = 100
                continue
            else:
                print("Goodbye!")
                break
        score -= 10
        score = max(score, 0)

        
if __name__ == '__main__':
    start_game()            