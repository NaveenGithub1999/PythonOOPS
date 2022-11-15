from pickle import TRUE
import random

def play_game():
    user = input("whats your choice 'p' for paper,'s' for sciccer, 'r' for rock\n")
    cumputer = random.choice(['p','r','s'])

    if user == cumputer:
        return 'tie'
    if is_win(user,cumputer):
        return 'you won'

    return 'you lost'

def is_win(player,opponent):
    if (player =='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True

print(play_game())