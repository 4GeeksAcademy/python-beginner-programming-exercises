# ✅↓ Write your code here ↓✅
def sing():
    song = ""
    for i in range(11):
        if i == 4:
            song += "there will be an answer, "
        elif i == 10:
            song += "whisper words of wisdom, let it be"
        else:
            song += "let it be, "
    return song

print(sing())
