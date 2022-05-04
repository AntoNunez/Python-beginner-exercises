# Your code here!!
def sing ():

    s = ""
    for i in range(0, 4):
        s += "let it be, " 
    for i in range(0, 1):
        s += "whisper words of wisdom, " 
    for i in range(0, 5):
        s += "let it be, " 
    for i in range(0, 1):
        s += "there will be an answer, " 
    for i in range (0,1):
        s += "let it be"
    
    return str(s)

print(sing())
