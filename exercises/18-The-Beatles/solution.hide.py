# ✅↓ Write your code here ↓✅
def sing():
    song = ""
    for i in range(11):
        if i == 4:
            song += "there will be an answer,\n"
        elif i == 10:
            song += "whisper words of wisdom, let it be"
        else:
            song += "let it be,\n"
    return song

sing()
