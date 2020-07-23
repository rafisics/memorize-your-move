import random2
from colorama import init, Fore, Back, Style     #[This package has helped me to generate the color in game state in windows ternimal.But not working in Google Colab. Why?]
init()

# Random co-ordibate generator function
def Rand(start, end, length):
    list = []
    while len(list)<length:
        res = []
        for j in range(2):
            res.append(random2.randint(start, end))
        list.append(res)
        if [0,0] in list:
            list.remove([0,0])
        if [end, end] in list:
            list.remove([end, end])
    list.sort()
    return list

# Game dictionary
Game_dict={'Easy':{'Size':10, 'Life':5, 'Jump':5, 'Obstacle':10, 'Advantage':20,
                   'Obstacle_coordinates':[],

                   'Advantage_coordinates':[]},

           'Medium':{'Size':20, 'Life':8, 'Jump':10,'Obstacle':15, 'Advantage':25,
                     'Obstacle_coordinates':[],

                     'Advantage_coordinates': []},

           'Hard':{'Size':25, 'Life':10, 'Jump':15, 'Obstacle':20, 'Advantage':35,
                   'Obstacle_coordinates':[],

                   'Advantage_coordinates':[] }}

# Game state sign function
def Game_State_Sign(x,y,level):
    Obstacle_list = Game_dict[level]['Obstacle_coordinates']
    Advantage_list = Game_dict[level]['Advantage_coordinates']
    Size = Game_dict[level]['Size']
    for i in range(0, Size):
      for j in range(0, Size):
        list_ij=[i,j]
        if (i==x and j==y):
          print("\033[0;37;44m   s ",end='  ')
        elif (list_ij in Obstacle_list):
          print("\033[0;37;41m   * ",end='  ')
        elif (list_ij in Advantage_list):
          print("\033[0;37;42m   + ",end='  ')
        elif (i==Size-1 and j==Size-1):
          print("\033[0;37;45m   e ",end='  ')
        else:
          print("\033[0;30;47m   - ",end='  ')
      #print('\033[ \n')             #newline with default style [It works in Google Colab, but not working in windows terminal. Why!?]
      print(Style.RESET_ALL,"\n")    #newline with default style [It works in windows terminal, but not working in  Google Colab. Why!?]

# Game state coordinate function
def Game_State_Coordinate(x,y,level):
    Obstacle_list = Game_dict[level]['Obstacle_coordinates']
    Advantage_list = Game_dict[level]['Advantage_coordinates']
    size = Game_dict[level]['Size']
    for i in range(0, size):
      for j in range(0, size):
        list_ij=[i,j]
        if (i==x and j==y):
          print("\033[0;37;44m    s ",end='  ')
        elif (list_ij in Obstacle_list):
          print("\033[0;37;41m {:2.0f},".format(i),j,end='  ')
        elif (list_ij in Advantage_list):
          print("\033[0;37;42m {:2.0f},".format(i),j,end='  ')
        elif (i==size-1 and j==size-1):
          print("\033[0;37;45m    e ",end='  ')
        else:
          print("\033[0;30;47m {:2.0f},".format(i),j,end='  ')
      #print('\033[ \n')             #newline with default style [It works in Google Colab, but not working in windows terminal. Why!?]
      print(Style.RESET_ALL,"\n")    #newline with default style [It works in windows terminal, but not working in  Google Colab. Why!?]

# Game state function
def Game_State(x,y,level):
  print("\nYour game state with sign:\n")
  Game_State_Sign(x,y,level)
  print("\nYour game state with coordinate:\n")
  Game_State_Coordinate(x,y,level)
  print("\nYour current coordinate: {}, {}".format(x,y))

# Jump function
def Jump(command,x,y, jump):
     if jump>0:
         if command == '56':
           x = x
           y = y+2
           jump = jump - 1
           print("You have only",jump,"jump left!")
         elif command == '54':
            x = x
            y = y-2
            jump = jump - 1
            print("You have only",jump,"jump left!")
         elif command == '58':
            x = x-2
            y = y
            jump = jump - 1
            print("You have only",jump,"jump left!")
         elif command == '52':
            x = x+2
            y = y
            jump = jump - 1
            print("You have only",jump,"jump left!")
     else:
         print("Sorry, you can't jump anymore.")
     return x, y, jump

# Move function
def Move(command,x,y, jump):
    commands = ['0', '1', '2', '4', '6', '8', '52', '54', '56', '58']
    if command == '6':
      x = x
      y = y+1
    elif command == '4':
       x = x
       y = y-1
    elif command == '8':
       x = x-1
       y = y
    elif command == '2':
       x = x+1
       y = y
    elif command in commands[6:]:
        x,y,jump = Jump(command,x,y,jump)
    elif command not in commands:
        print("Invalid command key\nThe valid command keys are:", end= " ")
        print(*commands, sep = ", ")
    return x, y, jump

# Undo function [It's mot much efficient]
def Undo(x_past,y_past):
    x = x_past
    y = y_past
    return x,y

# Point function [ I tried to apply Game_Denoter concept. But in doing so, my Point function became complicated and was giving wrong output.]
def Points(x,y,level,life,jump,command):
    Obstacle_list = Game_dict[level]['Obstacle_coordinates']
    Advantage_list = Game_dict[level]['Advantage_coordinates']
    size = Game_dict[level]['Size']
    commands = ['0', '1', '2', '4', '6', '8', '52', '54', '56', '58']

    if command in commands:
        if command=='0':
            Game_State(x,y,level)
            life = life - 1
            print("You have seen the game state again. Your life point is reduced to", life)
        else:
            if [x,y] in Obstacle_list:
                life = life - 5
                print("It's an obstacle coordinate. Your life point is reduced to",life)
            elif [x,y] in Advantage_list:
                life = life + 10
                print("It's an advantage coordinate. Your life point is increased to",life)
            else:
                list_ij = []
                for i in range(0, size):
                    for j in range(0, size):
                         list_ij.append([i,j])
                if [x,y] not in list_ij:
                    life = life - 1
                    #print("Your current coordinate: {}, {}".format(x,y))
                    print("You are out of the game state boundary. You life point is reduced to",life)

    return life

#main program
print("Welcome to 'Memorize your move' game!\n")
print("This is a console game where you will need to start from your starting coordinate \nand need to reach your ending coordinate. On your way to the ending coordinate, you will find obstacles and advantages.\n")

print("Game Features: \n# The game has three levels - 1) Easy, 2) Medium and 3) Hard.")
print("# For each level, you will have fixed game state, lives and jumps \n# Obstacles will reduce your point and Advantages will increase your point.")
print("# You can jump over the obstacles also. But only for fixed times. \n# You can see your present position anytime. But for each time of seeing, you will lose one of your life.")
print("# If you go out of the bound, you will lose one of your life. \n# So, you need to memorize your last position and walk or jump according to that.\n")

print("Choose your level: \nPress 1 for Easy \nPress 2 for Medium \nPress 3 for Hard")
while True:
    gl = input("> ",)
    if gl == '1':
        Game_level = 'Easy'
        break
    elif gl == '2':
        Game_level = 'Medium'
        break
    elif gl == '3':
        Game_level = 'Hard'
        break
    else:
        print("Invalid input. Try again. Choose 1, 2 or 3.")
        continue

Game_dict[Game_level]['Obstacle_coordinates'] = Rand(0, Game_dict[Game_level]['Size']-1, Game_dict[Game_level]['Obstacle'])
Game_dict[Game_level]['Advantage_coordinates'] = Rand(0, Game_dict[Game_level]['Size']-1, Game_dict[Game_level]['Advantage'])

size = Game_dict[Game_level]['Size']
life = Game_dict[Game_level]['Life']
jump = Game_dict[Game_level]['Jump']
print("Welcome to level: {}".format(Game_level))
print("Here, you have {} life points".format(life), end=" ")
print("and {} jump points".format(jump))
x=0
y=0
Game_State(x,y, Game_level)
print("\nHow to Play: \nPress 8 to move up \nPress 2 to move down \nPress 4 to move left \nPress 6 to move right")
print("Press 5x to jump (double move) at a specific direction. For example:\n  Press 58 to jump up; other jumps are 52, 54, 56 respectively")
print("Press 0 to see the game state and your present position.\nPress 3 to undo your coordinate change\nPress 1 to exit the game")

print("\nMemorize your present coordinate and obstacles ....")
print("\nStart making moves by pressing the command keys which are listed above.")
while (life > 0):
    command = input("\ncommand: ")

    if command=='0':
        #Game_State(x,y, Game_level)
        life = Points(x,y,Game_level,life,jump,command)
        #print("Your current life:", life)
        if life==0:
            print("You lost with",jump,"jump points.\n Game is over.")
            break
    elif command=='1':
        print("Game is stopped.")
        break
    elif command=='3':                          # I am not reducing life points for undo move
        x,y = Undo(x_past, y_past)
        #print("Your current coordinate: {}, {}".format(x,y))
        #print("Your current life:", life)
    else:
        x_past = x
        y_past = y
        x,y,jump = Move(command,x,y,jump)
        #print("Your current coordinate: {}, {}".format(x,y))
        life = Points(x,y,Game_level,life,jump,command)
        #print("Your current life:", life)
        if life==0 and x==size-1 and y==size-1:
            print("You have reached the end. But you have no life point left.\n Game is over.")
            break
        elif life==0:
            print("You lost with",jump,"jump points.\n Game is over.")
            break
        elif (x==size-1 and y==size-1):
            Game_State(x,y, Game_level)
            print("You have reached the end. \nYou won with",life,"life points and",jump,"jump points. Congrats!\n Game is over.")
            break
