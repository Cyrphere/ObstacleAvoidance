from play_game import run_moves
from random import randint

# accepts a list of list of agent moves


def run_trial(agentmoves):
    run_moves(agentmoves)


moves = ['R', 'L', 'U', 'D', 'N']
arr = []
arr = [[None for i in range(100)] for j in range(1000)]
for i in range(1000):
    for j in range (100):
        arr[i][j] = moves[randint(0,4)]
run_trial(arr)
