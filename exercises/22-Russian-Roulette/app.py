import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position


def fire_gun():
	#you code here
	if(spin_chamber() == bullet_position):
	  return 'Keep playing :)'
	else:
	  return 'You are dead!'



print(fire_gun())