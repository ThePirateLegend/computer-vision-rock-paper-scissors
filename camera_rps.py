#%%
import time
import numpy as np
import cv2
from keras.models import load_model
import random
model = load_model('keras_model.h5')

class RPSgame:
    
    def __init__(self,model):
        self.player_wins=0
        self.computer_wins=0
        self.computer_pick = "Nothing"
        self.player_pick= "Nothing"
        self.model=model

    def get_computer_pick(self):
        pick_list = ["Rock", "Paper", "Scissors"]
        self.computer_pick = random.choice(pick_list)
    
    def get_winner(self):
        if self.player_pick == "Nothing": #no choice
            print('invalid player pick')

        elif self.computer_pick=='Rock' and self.player_pick=='Paper':  #where player wins
            print("You win!")
            self.player_wins+=1

        elif self.computer_pick=='Paper' and self.player_pick=='Scissors':
            print("You win!")
            self.player_wins+=1

        elif self.computer_pick=='Scissors' and self.player_pick=='Rock':
            print("You win!")
            self.player_wins+=1

        elif self.computer_pick==self.player_pick: # same choice
            print("Draw!")

        else:
            print("Computer wins") #where computer wins
            self.computer_wins+=1

    def get_prediction(self):
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) #stores models output
        time_init=time.time() 
        font = cv2.FONT_HERSHEY_TRIPLEX
        pick_list= {0:"Rock", 1:"Paper", 2:"Scissors", 3:"Nothing"}
        countmax=5

        while time.time() < time_init+countmax:
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = self.model.predict(data)
            pickcountdown = str(int(time_init+countmax-time.time()))
            frame2=cv2.putText(frame, pickcountdown, (50, 50), font, 1, (255,255,255), 2, cv2.LINE_AA)
            cv2.imshow('frame', frame2)
        cap.release()
        cv2.destroyAllWindows()
        self.player_pick=pick_list[prediction.argmax()]
        return()

def play_game(model):
    game=RPSgame(model)
    print("First to 3 wins!")
    while True:
        if game.player_wins==3:
            print("Well done!")
            break
        elif game.computer_wins==3:
            print("You Lose!")
            break
        else:
            game.get_computer_pick()
            game.get_prediction()
            game.get_winner()
        print("computer wins: ",(game.computer_wins))
        print("player wins: ",(game.player_wins)) 


play_game(model)
#%%