from pydub import AudioSegment
from pydub.playback import play
from random import randint


tab_Per = ["Upset_Per_", "Surprised_Per_", "Sadder_Per_", "Sad_Per_", "Panic_Per_", "Normal_Per_","Distracted_Per_", "Determined_Per_","Deadpan_Per_", "Angry_Per_"]
tab_Mid = ["Upset_Mid_", "Surprised_Mid_", "Sadder_Mid_", "Sad_Mid_", "Panic_Mid_", "Normal_Mid_","Distracted_Mid_", "Determined_Mid_","Deadpan_Mid_" , "Angry_Mid_"]


mood = 5 ## indice du mood dans le tab
lenght = 20 ## nombre de puit puit qu'on veux

def create_sound(mood, lenght):
    final_sound = AudioSegment.from_mp3("Madeline/silence.mp3")
    temp_sound = ""
    last_rand = 0

    for i in range(0,lenght):
        rand_let = randint(1,4) ## pour le choix entre ABC et Per
        rand_num = randint(1,10) ## choix de la variante
        rand_num_f = f'0{rand_num}' if rand_num < 10 else str(rand_num) ## permet d'avoir les nombre sous le format 0X
        while rand_let == last_rand: ## pour eviter d'avoir 2 fois d'affilé le meme son (je suis pas sur que ca marche)
            rand_let = randint(1,4)

        if rand_let == 1: ## A
            final_sound += AudioSegment.from_mp3(("Madeline/" + tab_Mid[mood] + "A_" + rand_num_f + ".mp3")) + AudioSegment.from_mp3("Madeline/silence.mp3") ## fichier silence.mp3 qui dure 0.02sec

        elif rand_let == 2: ## B
            final_sound += AudioSegment.from_mp3(("Madeline/" + tab_Mid[mood] + "B_" + rand_num_f + ".mp3")) + AudioSegment.from_mp3("Madeline/silence.mp3")

        elif rand_let == 3: ## Pre
            final_sound += AudioSegment.from_mp3(("Madeline/" + tab_Per[mood] + rand_num_f + ".mp3"))

        elif rand_let == 4: ## C
            final_sound += AudioSegment.from_mp3(("Madeline/" + tab_Mid[mood] + "C_" + rand_num_f + ".mp3"))

        last_rand = rand_let ## anti doublon

    temp_sound = ("Madeline/" + tab_Mid[mood] + "C_" + rand_num_f + ".mp3") ## fin de phrase
    final_sound += AudioSegment.from_mp3(temp_sound)
    return final_sound

play(create_sound(mood, lenght))


        