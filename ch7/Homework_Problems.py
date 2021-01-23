#!/usr/bin/env python
# coding: utf-8

# ## Problem 1
# 
# 
# Lauren's 4 year old neice has fallen in love with the board game [Hoot Owl Hoot](https://boardgamegeek.com/boardgame/94483/hoot-owl-hoot) and wants to know what the probability of winning the game is (if it's too low, she might become discouraged). Unfortunately, her aunt hasn't taught her how to program in Python yet, so she has asked you to write a program that will figure out the probability of winning by simulating the game repeatedly and counting the number of times that the game results in the players winning (an approach known as the [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method)).
# 
# ### Rules of the game
# 
# <img src="empty_board.jpg" width="400" />
# 
# Hoot Owl Hoot is a cooperative game, so either everyone wins or everyone loses. The objective of the game is to move all the owls around the board and into the nest before the sun rises. The owls start on the "Start" spaces on the right side of the board. You can choose to play with any number of owls you want (at least three and as many as six). The sun piece starts on "Sun Start" at the top of the board. There is a deck of 50 cards that includes 36 colored cards (six of each color on the board) and 14 sun cards. Each player (from 2-4 players) is dealt three cards. Players keep their cards face up in front of them so that they can work together to strategize how to move. If a player has a sun card, on her turn she must discard the sun and move the sun token one space; if she has all color cards, she discards any one color card, then moves any owl to the next open space of that color. Each space can only be occupied by a single owl. If an owl "flies" over an owl on a space of that color on its way to the next open space, all players make a hooting sound! After a player moves an owl, they should take a new card from the deck.
# 
# If you're confused about the rules, you can watch this [short, informative video](https://www.youtube.com/watch?v=czk0V3mga0Q) or read the [instructions](instructions.jpg).
# 
# ### Simulating the game
# 
# You are to write a program that simulates the Hoot Owl Hoot game. Your program will need to keep track of:
# - The positions of the 3-6 owls on the board.
# - The deck of cards
# - The cards held by each of the 2-4 players. Since any player can move any owl, this implies that the players' hands and the owls positions should be stored separately.
# - The position of the sun.
# 
# Your program should have a loop for which the body corresponds to a single turn. The algorithm should roughly look as follows:
# 
# 1. Assign starting positions for the owls. Note that if fewer than six owls are used, the first few spaces on the board are unoccupied.
# 2. Create a deck of cards and "shuffle" it. The easiest way to do this is to use the [random.shuffle](https://docs.python.org/3/library/random.html#random.shuffle) function from the standard library.
# 3. Deal three cards to each player.
# 4. Iterate over the player's turns. If you have a list storing the hand held by each player, one approach would be to cycle through it using [itertools.cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle).
# 5. If the current player has a sun in their hand, they must play it. The sun piece advances and they receive a new card (if the deck is not empty). If the sun has already risen (moved 13 times), the game is lost. If not, continue to the next player's turn.
# 6. If the current player does not have a sun in their hand, they need to play a color. Here, the strategy you should implement is to move the owl who is furthest from the nest. Given the three cards the player is holding, determine which card would result in that owl moving the maximum number of spaces. If playing a card results in the owl moving to the nest, that card should be preferred. After the owl has been moved, the player receives a new card from the deck (if not empty).
# 7. If all owls have reached the nest, the game is won. Otherwise, proceed to the next player's turn.
# 
# You are free to implement the simulation using whatever classes and functions you'd like.
# 
# ### Determining the probability of winning
# 
# Once you have a function/class/module that can be used to simulate the game, write a separate function that repeatedly simulates the game, counts the number of times that the game is won, and prints out the probability of winning based on the observations (number of wins divided by number of games played) The game should be simulated at least 10,000 times to get good statistics. In addition, you should determine how the probability changes if we change the number of players and/or the number of owls. In your program, add a comment somewhere that lists the probability of winning with:
# 
# - 2 players and 3 owls
# - 2 players and 6 owls
# - 4 players and 3 owls
# - 4 players and 6 owls
# 
# Although not required for credit, if you want to report not only the mean value of the win probability but also its standard deviation

# In[ ]:


#

