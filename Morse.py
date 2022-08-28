Morse = {'.-':'A', '-...':'B','-.-.':'C', '-..':'D', '.':'E',
         '..-.':'F', '--.':'G', '....':'H','..':'I', '.---':'J',
         '-.-':'K','.-..':'L', '--':'M', '-.':'N','---':'O', 
         '.--.':'P', '--.-':'Q','.-.':'R', '...':'S', '-':'T',
         '..-':'U', '...-':'V', '.--':'W','-..-':'X', '-.--':'Y', 
         '--..':'Z','.----':'1', '..---':'2', '...--':'3',
        '....-':'4', '.....':'5', '-....':'6','--...':'7', '---..':'8',            '----.':'9','-----':'0','/':' '}
Message = ""
Space = []
Code = input('Morce code : ')

if Code.find('/') > -1:
  start = 0
  Word = Code  
  while start<len(Word) :
    index = Word.find('/',start,len(Word))
    if index ==-1:
      break
    elif index > -1:
      Space.append(index)
      Word = Word[:index]+' / '+Word[index+1:]
      start = index+2
else :
  Word = Code
if Word.find(" "):
  Alphabet = Word.split(' ')
  
for y in Alphabet:
  found_index = Morse.get(y)
  Message += found_index
    
print(Message)