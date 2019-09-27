def number_of_bottles():
    plural_line = ""
    second_line = ""
    sing_line = ""
    last_line = ""
    for i in range(100,0,-1):
    
        if i>2:
            plural_line += str(i) + " bottles of milk on the wall, " + str(i) + " bottles of milk."+ "\n" + "Take one down and pass it around, " + str(i-1) + " bottles of milk on the wall."+ "\n"
        elif i == 2:
            second_line += str(i) + " bottles of milk on the wall, " + str(i) + " bottles of milk."+ "\n" + "Take one down and pass it around, " + str(i-1) +" bottle of milk on the wall."+ "\n"
        elif i == 1:
            sing_line += str(i) + " bottle of milk on the wall, " + str(i) + " bottle of milk."+ "\n" + "Take one down and pass it around, " +  "no more bottles of milk on the wall."+ "\n"
        else: 
            last_line = "No more bottles of milk on the wall, no more bottles of milk." +"\n"+"Go to the store and buy some more, "+ str(i+99) +" bottles of milk on the wall."
        
    return plural_line + second_line + sing_line + last_line
  

print(number_of_bottles())       