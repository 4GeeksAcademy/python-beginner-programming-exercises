# Solution 1:

def number_of_bottles():
    for x in reversed(range(100)):
        if (x==0):
            print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")
        elif (x==1):
            print("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.")
        elif (x==2):
            print("2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall.")
        else:
            print(str(x) + " bottles of milk on the wall, " + str(x) + " bottles of milk. Take one down and pass it around, " + str(x - 1) + " bottles of milk on the wall.")

number_of_bottles()

# Solution 2:

def number_of_bottles():
    for x in range(99,1,-1): 
        if (x==2):
            print("2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall.")
        else:
            print(str(x)+" bottles of milk on the wall, "+str(x)+" bottles of milk. Take one down and pass it around, "+str(x-1)+" bottles of milk on the wall.")
    print("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.")
    print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")

number_of_bottles()