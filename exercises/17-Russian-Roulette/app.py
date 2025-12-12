import random

bullet_position = 3


def spin_chamber():
    chamber_position = random.randint(1, 6)
    return chamber_position

#  ⬆ DON'T CHANGE THE CODE ABOVE ⬆


def fire_gun() :
    # ✅ ↓ your code here ↓ ✅
    chamber_position = int(spin_chamber())
    if bullet_position == chamber_position : 
        return "You are dead!"
    return "Keep playing!"


print(fire_gun())
