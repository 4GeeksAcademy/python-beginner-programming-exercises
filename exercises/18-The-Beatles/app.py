# Your code here!!
def sing():
    song = ""
    for verse in range(11):
        if verse == 4:
            song += "whisper words of wisdom, "
        elif verse == 10:
            song += "there will be an answer, let it be"
        else:
            song += "let it be, "
    return song

print(sing())