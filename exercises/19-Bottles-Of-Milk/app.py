
def number_of_bottles_song(num_bottles,num):
    songStr = ""

    for i in range(num_bottles, num, -1):
        if (i == 0):
            songStr +=  (
                       "No more bottles of milk on the wall, no more bottles of milk.\n"
                       "Go to the store and buy some more, 99 bottles of milk on the wall.")
            
        elif (i == 1):
            songStr += (
                        f"{i} bottle of milk on the wall, 1 bottle of milk.\n"
                        "Take one down and pass it around, no more bottles of milk on the wall.\n\n")
            
        elif (i == 2):
            songStr += (
                        f"{i} bottles of milk on the wall, {i} bottles of milk.\n"
                          "Take one down and pass it around, 1 bottle of milk on the wall.\n\n" )
              
        else :
            songStr += (
                       f"{i} bottles of milk on the wall, {i} bottles of milk.\n"
                       "Take one down and pass it around, {i -1} bottles of milk on the wall.\n\n" )

    return songStr


# ?main method to call the song builiding function
def number_of_bottles():
    song = number_of_bottles_song(99, -1)  
    print(song)
    return None
    

number_of_bottles() 