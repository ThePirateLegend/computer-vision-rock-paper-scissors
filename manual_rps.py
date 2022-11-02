#%%
import random 
class rock_paper_scissors_game():
    def __init__(self, game_list = ["rock", "paper", "scissors"]):
        self.guess = random.choice(game_list)
        self.game_list = game_list

    def get_computer_choice(self):
        print("computer guessed", self.guess)
        self.get_winner()

    def get_user_choice(self):
        self.user_guess = input("Rock, paper, scissors, shoot!")
        print("You guessed", self.user_guess)
        self.get_computer_choice()

    def get_winner(self):
        if self.guess=="rock" and self.user_guess=="paper":
            print("You win!")
        elif self.guess=="paper" and self.user_guess=="scissors":
            print("You win!")
        elif self.guess=="scissors" and self.user_guess=="rock":
            print("You win!")
        elif self.guess==self.user_guess:
            print("Draw!")
        else: print("You lost!")

rock_paper_scissors_game().get_user_choice()
#%%