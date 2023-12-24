from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("Madeline/Upset_Mid_B_09.mp3") + AudioSegment.from_mp3("Madeline/Upset_Mid_A_06.mp3") + AudioSegment.from_mp3("Madeline/Upset_Mid_C_05.mp3") + AudioSegment.from_mp3("Madeline/Upset_Mid_C_09.mp3")
play(song)

tab_Per = ["Upset_Per_", "Surprised_Per_", "Sadder_Per_", "Sad_Per_", "Panic_Per_", "Normal_Per_","Distracted_Per_", "Determined_Per_","Deadpan_Per_", "Angry_Per_"]
tab_Mid = ["Upset_Mid_", "Surprised_Mid_", "Sadder_Mid_", "Sad_Mid_", "Panic_Mid_", "Normal_Mid_","Distracted_Mid_", "Determined_Mid_","Deadpan_Mid_" , "Angry_Mid_"]