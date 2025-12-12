# ↓ Write your code here ↓
def repeat_lyrics(num_times):
    repeat_Str =""
    for i in range(num_times) :
        repeat_Str += "let it be,\n"
    return repeat_Str


def sing():
    songStr = ""
    songStr += repeat_lyrics(4)
    songStr += "there will be an answer,\n"
    songStr += repeat_lyrics(5)
    songStr += "whisper words of wisdom, let it be"
    return songStr

print(sing())