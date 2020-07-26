import random2
from colorama import init, Style
init()           #[It generates the game state colors in windows terminal, not in Google Colab.]

# Random coordinate generator function
def Rand(start, end, length):
    list = []
    while len(list)<length:
        res = []
        for j in range(2):
            res.append(random2.randint(start, end))
        if res not in list:
            list.append(res)
        if res==[0,0] or res==[end, end]:
            list.remove(res)
        list = [i for i in list+obs if i in list and i not in obs]
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
    for i in range(0, size):
      for j in range(0, size):
        list_ij=[i,j]
        if (i==x and j==y):
          print("\033[0;37;44m   s ",end='  ')
        elif (list_ij in p_xy):
          print("\033[1;36;40m   - ",end='  ')
        elif (list_ij in Obstacle_list):
          print("\033[0;37;41m   * ",end='  ')
        elif (list_ij in Advantage_list):
          print("\033[0;37;42m   + ",end='  ')
        elif (i==size-1 and j==size-1):
          print("\033[0;37;45m   e ",end='  ')
        else:
          print("\033[0;30;47m   - ",end='  ')
      #print('\033[ \n')             #newline with default style [It works in Google Colab, but not in windows terminal. Why!?]
      print(Style.RESET_ALL,"\n")    #newline with default style [It works both in windows terminal and Google Colab.]

# Game state coordinate function
def Game_State_Coordinate(x,y,level):
    for i in range(0, size):
      for j in range(0, size):
        list_ij=[i,j]
        if (i==x and j==y):
          print("\033[0;37;44m    s ",end='  ')
        elif (list_ij in p_xy):
          print("\033[1;36;40m {:2.0f},".format(i),j,end='  ')
        elif (list_ij in Obstacle_list):
          print("\033[0;37;41m {:2.0f},".format(i),j,end='  ')
        elif (list_ij in Advantage_list):
          print("\033[0;37;42m {:2.0f},".format(i),j,end='  ')
        elif (i==size-1 and j==size-1):
          print("\033[0;37;45m    e ",end='  ')
        else:
          print("\033[0;30;47m {:2.0f},".format(i),j,end='  ')
      #print('\033[ \n')             #newline with default style [It works in Google Colab, but not in windows terminal. Why!?]
      print(Style.RESET_ALL,"\n")    #newline with default style [It works both in windows terminal and Google Colab.]

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
         if command == '56':        # Jump right
            x = x
            y = y+2
         elif command == '54':      # Jump left
            x = x
            y = y-2
         elif command == '58':      # Jump up
            x = x-2
            y = y
         elif command == '52':      # Jump down
            x = x+2
            y = y
         jump = jump - 1
         print("You have only",jump,"jumps left!")
     else:
         print("Sorry, you can't jump anymore.")
     return x, y, jump

# Move function
def Move(command,x,y, jump):
    if command == '6':        # Move right
       x = x
       y = y+1
    elif command == '4':      # Move left
       x = x
       y = y-1
    elif command == '8':      # Move up
       x = x-1
       y = y
    elif command == '2':      # Move down
       x = x+1
       y = y
    elif command in commands[-4:]:
        x,y,jump = Jump(command,x,y,jump)
    elif command not in commands:
        print("Invalid command key\nThe valid command keys are:", end= " ")
        print(*commands, sep = ", ")
    return x, y, jump

# Undo function       [It's mot much efficient. If you use it twice in a row to return to previous coordinates, it won't function the second time.  #Because it stores only your last coordinates, not all your past ones.
def Undo(x_past,y_past):
    x = x_past
    y = y_past
    return x,y

# Point function [ I tried to apply Game_Denoter concept. But in doing so, my Point function became complicated and was giving wrong output.]
def Points(x,y,level,life,jump,point,command):
    if command in commands:
        if command=='0':
            Game_State(x,y,level)
            life = life - 1
            print("You have seen the game state again. Your life is reduced to", life)
        elif command=='3':
            life = life
            point = point
            print("You have returned to your previous coordinate by the undo command.\nSo Your lives or points haven't changed.")
        else:
            if [x,y] != [x_past,y_past] and [x,y] not in p_xy:
                if [x,y] in Obstacle_list:
                    point = point - 5
                    print("It's an obstacle coordinate. Your point is reduced to",point)
                elif [x,y] in Advantage_list:
                    point = point + 10
                    print("It's an advantage coordinate. Your point is increased to",point)
                else:
                    if [x,y] not in list_xy:
                        life = life - 1
                        #print("Your current coordinate: {}, {}".format(x,y))
                        print("You are out of the game state boundary. You life is reduced to",life)
                        if life>0:
                            print("Press 3 to undo this move and return back inside the game state.")
            else:
                if command in commands[-4:]:
                    print("So, your coordinate is not changed.")
                else:
                    print("You have come here before.\nSo it can't change your lives or points anymore.")
    return life, point

#main program
print("Welcome to the 'Memorize your move' game!\n")
print("This is a console game where you will start from the initial coordinate and need to reach the final coordinate. \nOn your way to the ending coordinate, you will find some obstacles and advantages.\n")
print("Game Features: \n# The game has three levels - 1) Easy, 2) Medium and 3) Hard.")
print("# For each level, you will have fixed game state, lives and jumps. \n# Obstacles will reduce your point and Advantages will increase your point.")
print("# You can jump over the obstacles also, but only for fixed times. \n# You can see your present coordinate anytime. But for each time of seeing, you will lose one of your life.")
print("# If you go out of the bound, you will lose one of your life.")
print("# The effect of advantage/obstacle on each coordinate works the first time only. \n  That means your lives/points won't change when you undo your move or go back to any of your past coordinates.")
print("# So, you need to memorize your coordinate, obstacles, advantages. And move or jump according to that.\n")
print("Choose your level: \nPress 1 for Easy \nPress 2 for Medium \nPress 3 for Hard")

while True:
    gl = input("> ",)
    if gl == '1':
        level = 'Easy'
        break
    elif gl == '2':
        level = 'Medium'
        break
    elif gl == '3':
        level = 'Hard'
        break
    else:
        print("Invalid input. Try again. Choose 1, 2 or 3.")
        continue

obs = []
Game_dict[level]['Obstacle_coordinates'] = Rand(0, Game_dict[level]['Size']-1, Game_dict[level]['Obstacle'])
obs = Game_dict[level]['Obstacle_coordinates']
Game_dict[level]['Advantage_coordinates'] = Rand(0, Game_dict[level]['Size']-1, Game_dict[level]['Advantage'])
adv = Game_dict[level]['Advantage_coordinates']

size = Game_dict[level]['Size']
life = Game_dict[level]['Life']
jump = Game_dict[level]['Jump']
Obstacle_list = Game_dict[level]['Obstacle_coordinates']
Advantage_list = Game_dict[level]['Advantage_coordinates']

print("Welcome to level: {}".format(level))
commands = ['0', '1', '2', '3', '4', '6', '8', '52', '54', '56', '58']
list_xy = []
for i in range(0, size):
    for j in range(0, size):
        list_xy.append([i,j])   #This list contains all the cordinates of the game state of the selected level.

#Starting conditions:
x=0
y=0
point=0
p_xy = [[x,y]]               #This list will keep all the coordinates that the player will go through.

Game_State(x,y, level)
print("Here, you have {} lives".format(life), end=" ")
print("and {} jumps.".format(jump))
print("There are",len(obs),"obstacles and",len(adv),"advantages in this game state.")

print("\nHow to Play: \nPress 8 to move up \nPress 2 to move down \nPress 4 to move left \nPress 6 to move right")
print("Press 5 and any of the move commands to jump at a specific direction:\n  Press 58 to jump up\n  Press 52 to jump down\n  Press 54 to jump left\n  Press 56 to jump right")
print("Press 0 to see the game state and your current coordinate \nPress 3 to undo your last move\nPress 1 to exit the game")
print("\nMemorize your present coordinate, obstacles, advantages.")
print("\nStart making moves by pressing the command keys which are listed above.")

while (life > 0):
    command = input("\ncommand: ")
    if command=='0':
        life,point = Points(x,y,level,life,jump,point,command)
        print("Your current point:", point)
        if life==0:
            print("You lost with",jump,"jumps.\n Game is over.")
            break
    elif command=='1':
        print("Game is stopped.")
        break
    elif command=='3':
        x,y = Undo(x_past, y_past)
        #print("Your current coordinate: {}, {}".format(x,y))
        life,point = Points(x,y,level,life,jump,point,command)
        #print("Your current point:", point)
    else:
        x_past = x
        y_past = y
        x,y,jump = Move(command,x,y,jump)
        #print("Your current coordinate: {}, {}".format(x,y))
        life,point = Points(x,y,level,life,jump,point,command)
        #print("Your current point:", point)
        if [x,y] not in p_xy:
            p_xy.append([x,y])
        #print(p_xy)

        if life==0 and x==size-1 and y==size-1:
            print("You have reached the end. But you have no life left.\n Game is over.")
            break
        elif life==0:
            print("You lost with",point,"points and",jump,"jumps.\n Game is over.")
            break
        elif (x==size-1 and y==size-1):
            Game_State(x,y, level)
            print("You have reached the end. \nYou won with ",point,"points,",life,"lives and",jump,"jumps. Congrats!\n Game is over.")
            break
input("Press enter to exit.\n")
