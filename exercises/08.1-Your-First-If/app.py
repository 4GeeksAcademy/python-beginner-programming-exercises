total = int(input('How much money do you have in your pocket\n'))

# YOUR CODE HERE
if total > 100:
    print("Going to a trip.")
elif total > 50 and total <= 100:
    print("Going out for dinner.")
elif total <=50:
    print("Better stay at home and save some money.")