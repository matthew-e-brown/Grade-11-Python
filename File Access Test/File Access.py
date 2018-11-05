score = 5413    

def scores():
    highscores = []
    file = open("highscores.txt", "r+")

    for i in range(0, 9):        
        data = file.readlines()[i]
        print(int(data))
    
    #print(highscores[1])
    #print(highscores[3])

    for i in range (0, len(highscores)):
        if score > highscores[i] and score not in highscores:
            highscores[i] = score

    for i in range (0, len(highscores)): ##convert each line to a string with a \n after it
        highscores[i] = str(highscores[i])
        highscores[i] = highscores[i] + "\n"

    file.seek(0)
    file.truncate()
    for i in range (0, len(highscores)):
        file.write(highscores[i])

scores()
        
