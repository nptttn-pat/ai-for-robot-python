from gtts import gTTS

mytext = 'สวัสดีครับ'

language = 'th'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")