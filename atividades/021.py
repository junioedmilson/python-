# Atividade 021
# Abrindo e reproduzindo um arquivo de audio
from just_playback import Playback

playback = Playback()
playback.load_file("hino-cruzeiro.mp3")
playback.play()
input(" Pressione Enter para parar.")