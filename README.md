# Project: Memorize Your Move
'Memorize Your Move' is my first project. It was assigned to me in an online workshop 'Python: Anybody Can Code' by Jahangirnagar University Computer Club.

## Project Idea:
This is a console game where you (the player) will need to start from the starting coordinate and reach the ending coordinate.
On your way to the ending coordinate, you will find obstacles and advantages.

## Project Features:
The game has three levels - 1) Easy, 2) Medium and 3) Hard.

For each level, you will have fixed game state, lives and jumps

Obstacles will reduce your point and Advantages will increase your point.

You can jump over the obstacles also. But only for fixed times.

You can see your present coordinate anytime. But for each time of seeing your game state, you will lose one of your life.

If you go out of the bound, you will lose one of your life.

So, you need to memorize your last position and walk or jump according to that.

#### Game Version 1 
(project_v1): https://colab.research.google.com/drive/1374IjekwbEIpPOG29VTcKbXJtawjBc9j?usp=sharing

Your life-point and game-point are considered same. So, your life-point changes due to the advantages or obstacles.

#### Game Version 2 
(project_v2): https://colab.research.google.com/drive/1SJ0fP8tTMpz1NexKSkUBWzhQV7jZASbC?usp=sharing

Your life-point and game-point are considered different. So, your-life point doesn't change due to the advantages or obstacles.

#### Game Version 3
(project_v3): https://colab.research.google.com/drive/1AYSd0Y4By5p_B_n79bTH6m0PuNIDV2TA?usp=sharing

Some new features have beeen added and some errors have been fixed. 

Here, the effect of advantage/obstacle on each coordinate works the first time only. So, your lives/points won't change when you undo your move or go back to any of your past coordinates. Also, all your past coordinates will be shown in a different color in your game state.

