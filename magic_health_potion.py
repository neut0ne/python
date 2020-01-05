## for this project, I've been using Idle IDE on mac.
## the first row here is an imported module. Find modules from your Idle menu through help > pythondocs > modules.
## the module has a .randint function that returns a random number between two set values. 
## It looks like this: random.randint(x,y)
import random

## my game characters' initial health score.
health = 50

## We're on the easiest level (difficulty one out of 3)
difficulty = 1

## My game character has encountered a health potion! The health potion's value is between 25 and 
## 50 health points, divided by the difficulty level. 
potion_health = int(random.randint(25,50) / difficulty)

## My game character uses the potion and his health score increases accordingly.
health = health + potion_health

## This is the new health score!
print(health)
