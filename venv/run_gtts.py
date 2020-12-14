from gtts import gTTS
import os

text1 = 'Any text will work here'
file = gTTS(text1)
file.save('any.mp3')
os.system('start any.mp3')


