# var total = prompt('How much money do you have in your pocket');
total = int(input('How much money do you have in your pocket'))
if (total > 100):
    print("Give me your money!")
elif (total > 50):
    print("Buy me some coffee you cheap!")
elif (total < 51):
    print("You are a poor guy, go away!")
   