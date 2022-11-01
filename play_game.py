import sys
import pygame
from random import randint
from ship import Ship
from obj import Obj

pygame.init()

size = width, height = 640, 480
speed = [4, 4]
black = 0, 0, 0
GREEN = (20, 255, 140)
screen = pygame.display.set_mode(size)

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

all_sprites_list = pygame.sprite.Group()

goal = Obj(PURPLE, 10, 10, randint(380, 480),
           randint(0, 30), is_goal=True)
all_sprites_list.add(goal)

# generate the maze
wall_list = [goal]
for i in range(100):
    y = randint(40, 440)
    x = randint(0, 640)
    wall = Obj(RED, 10, 10, x, y)
    wall_list.append(wall)
    all_sprites_list.add(wall)


def handle_collision_play(w, ship):
    if w.is_goal:
        print("hit the goal")
        ship.set_pos(300, 440)
    else:
        ship.set_pos(300, 440)


def handle_collision_sim(w, ship):
    if w.is_goal:
        print("hit the goal")
        ship.stop()
    else:
        ship.stop()


def input_move(move, ship):
    #print('inputting move', move)
    if move == 'R':
        #print("right")
        ship.move_right()
    if move == 'L':
        #print("left")
        ship.move_left()
    if move == 'U':
        #print("up")
        ship.move_up()
    if move == 'D':
        #print("down")
        ship.move_down()
    #else:
        #print("do nothing")


def rand_move():
    a = randint(1,6)
    if a == 1:
        return 'R'
    elif a == 2:
        return 'L'
    elif a == 3:
        return 'U'
    elif a == 4:
        return 'D'
    elif a == 5:
        return 'N'
    
def mutate(move_list):
    # move_list => ['R', 'L', 'N' ....]
    new_moves = []
    for i in move_list:
        a = randint(1,101)
        if a <= 10:
            new_moves.append(rand_move())
        else:
            new_moves.append(i)
    return new_moves
    


# should return a list of all the success scores of the ships
def calculate_success(ships):
    x = []
    y = []
    numbers = []
    for ship in ships:
        x.append(goal.rect.x - ship.rect.x)
        y.append(goal.rect.y - ship.rect.y)
    for i in range (len(x)):
        numbers.append(-(x[i]**2 + y[i]**2)**1/2)
    print(numbers)
    top_ten_percent = sorted(range(len(numbers)), key=lambda i: numbers[i])[-int((len(x)/10)):]
    print(top_ten_percent)
    print("calculating success")
    return top_ten_percent


# should update the moves to be better
def recalculate_moves(moves, successes):
    new_moves = []
    for i in successes:
        for j in range(10):
            new_moves.append(mutate(moves[i]))
    return new_moves


def run_moves(agent_moves):
    ships = []
    for i in agent_moves:
        ship = Ship(GREEN, 10, 40, 300, 440)
        ships.append(ship)
        all_sprites_list.add(ship)
    move_number = 0
    while 1:
        for a in range(len(agent_moves)):
            all_sprites_list.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if move_number < len(agent_moves[0]):  # this is an agent move
                input_move(agent_moves[a][move_number], ships[a])
            else:  # we are done
                successes = calculate_success(ships)
                agent_moves = recalculate_moves(agent_moves, successes)
                for ship in ships:
                    ship.reset()
                move_number = 0

            ships[a].move(width, height)
        screen.fill(black)
        all_sprites_list.draw(screen)
        pygame.display.flip()
        move_number += 1

        # handle the collision for if ship collided with     
        for w in wall_list:
            for ship in ships:
                if w.collides_with(ship):
                    handle_collision_sim(w, ship)


if __name__ == "__main__":
    ship = Ship(GREEN, 10, 40, 300, 440)
    all_sprites_list.add(ship)
    while 1:
        all_sprites_list.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        ship.handle_keys()
        ship.move(width, height)
        screen.fill(black)
        all_sprites_list.draw(screen)
        pygame.display.flip()

        # handle the collision for if ship collided with wall
        for w in wall_list:
            if w.collides_with(ship):
                handle_collision_play(w, ship)
