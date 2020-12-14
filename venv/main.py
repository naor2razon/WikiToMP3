import os
from gtts import gTTS
import wikipedia

wikipedia.set_lang('he')
result = wikipedia.summary('Israel',sentences=4)
#print(result)

file = gTTS(result)
file.save('Israel.mp3')
