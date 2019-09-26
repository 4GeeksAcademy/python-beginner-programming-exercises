import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position


def fire_gun():
	#you code here
	if(spin_chamber() == bullet_position):
	  return False
	else:
	  return True
	  
 

if(fire_gun()): print('Keep playing :)')
else: print('You are dead!')