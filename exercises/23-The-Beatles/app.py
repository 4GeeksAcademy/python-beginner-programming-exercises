# Your code here!!
def sing():
  
    repeated_text = ""
    final_string = ""
    for i in range(1,5):
        repeated_text += "let it be, \n" 
        final_string = repeated_text + "Whisper words of wisdom, let it be, " + repeated_text + "there will be an answer, " + "let it be"
    return final_string 
  

print(sing())  