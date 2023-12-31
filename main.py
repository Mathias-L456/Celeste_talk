from pydub import AudioSegment
from pydub.playback import play
from random import randint
import re

import audio_effects as ae
from pydub.playback import _play_with_simpleaudio as play_sound

tab_Per = ["Upset_Per_", "Surprised_Per_", "Sadder_Per_", "Sad_Per_", "Panic_Per_", "Normal_Per_","Distracted_Per_", "Determined_Per_","Deadpan_Per_", "Angry_Per_"]
tab_Mid = ["Upset_Mid_", "Surprised_Mid_", "Sadder_Mid_", "Sad_Mid_", "Panic_Mid_", "Normal_Mid_","Distracted_Mid_", "Determined_Mid_","Deadpan_Mid_" , "Angry_Mid_"]


mood = 5 ## indice du mood dans le tab
##lenght = 5 ## nombre de puit puit qu'on veux
sentence = "ceci est un gros test . mais bon c'est un peu nul . enfin je crois ?"
#sentence = input("what do you want madeline to say ? \n>>> ")

def count(sen):
    """count number of words in a sentence

    Args:
        sen (string): sentence you need to count words

    Returns:
        integer: number of words
    """
    words = sen.split() ## permet de separer les mots
    return len(words)

def analyse(texte):
    """split and count the number of sentence and add it to a tab named taille

    Args:
        texte (string): your sentences

    Returns:
        list of int: the number of words of each sentence in the order
    """
    sen_tab = re.split(r'[.!?]', texte) ## on detecte les phrases (sen = sentence)
    sen_tab = [sen.strip() for sen in sen_tab if sen.strip()] ## on applique sen.strip pour chacune des phrases dans le tableau si sen.strip n'est pas vide
    taille = [count(i) for i in sen_tab] ## on ajoute le nombre de mot dans chacune de phrase
    print(sen_tab) ## si je print pas j'ai des erreurs ¯\_(ツ)_/¯
    return taille

lenght = analyse(sentence)
print(lenght)

def create_sound_random(mood, lenght):
    """create random segment talking sound from celeste

    Args:
        mood (int): index of the mood in tab_per and tab_mid
        lenght (int): the number of words of the sentence

    Returns:
        pydub audioSegment: a concatenate audio file of each segment
    """
    sound = AudioSegment.from_mp3("Madeline/silence.mp3")
    last_rand = 0

    for i in range(0,lenght):
        rand_let = randint(1,4) ## pour le choix entre ABC et Per
        rand_num = randint(1,10) ## choix de la variante
        rand_num_f = f'0{rand_num}' if rand_num < 10 else str(rand_num) ## permet d'avoir les nombre sous le format 0X
        while rand_let == last_rand: ## pour eviter d'avoir 2 fois d'affilé le meme son (je suis pas sur que ca marche)
            rand_let = randint(1,4)

        if rand_let == 1: ## A
            sound += AudioSegment.from_mp3(("Madeline/" + tab_Mid[mood] + "A_" + rand_num_f + ".mp3")) + AudioSegment.from_mp3("Madeline/silence.mp3") ## fichier silence.mp3 qui dure 0.02sec

        elif rand_let == 2: ## B
            sound += AudioSegment.from_mp3(("Madeline/" + tab_Mid[mood] + "B_" + rand_num_f + ".mp3")) + AudioSegment.from_mp3("Madeline/silence.mp3")

        elif rand_let == 3: ## Pre
            sound += AudioSegment.from_mp3(("Madeline/" + tab_Per[mood] + rand_num_f + ".mp3"))

        elif rand_let == 4: ## C
            sound += AudioSegment.from_mp3(("Madeline/" + tab_Mid[mood] + "C_" + rand_num_f + ".mp3"))

        last_rand = rand_let ## anti doublon

    
    sound += AudioSegment.from_mp3(("Madeline/" + tab_Mid[mood] + "C_" + rand_num_f + ".mp3")) ## fin de phrase
    return sound

def create_sentence(mood, lenght):
    """concatenate all the sentences (based on the size of lenght) to have a big one

    Args:
        mood (int): index index of the mood in tab_per and tab_mid
        lenght (list of int): the number of words of each sentence in the order

    Returns:
        pydub audioSegment: _description_
    """
    final_sound = AudioSegment.from_mp3("Madeline/silence.mp3")

    for i in range(0,len(lenght)): ## on créé autant de phrase que de phrase mis en entrée
        final_sound += create_sound_random(mood, lenght[i]) ## on créé autant de puit puit que de nombre de mot dans chacune des phrases
        final_sound += AudioSegment.from_mp3("Madeline/big_silence.mp3") ## permet de mettre une coupure entre les phrases

    return final_sound

play(create_sentence(5,lenght))

##current_audio_slow_down = ae.speed_down(create_sentence(mood,lenght), 0.85)
##play_sound(current_audio_slow_down)
##play(current_audio_slow_down)


        