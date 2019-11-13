import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate",200)

volume = engine.getProperty("volume")
engine.setProperty("volume",1000)

voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)

lk='iam mmacheei'
engine.say(lk)
engine.runAndWait()

fg='am ur personal assistant '
engine.say(fg)
engine.runAndWait()


say = "hi mr joshan john"
engine.say(say)

engine.runAndWait()

ser='your server is quite overload'
engine.say(ser)
engine.runAndWait()
    
val = 'but dont worry i will fix it out'
engine.say(val)

engine.runAndWait()

giy='your C drive is used almost 52.23 gb out of 500 sir '
engine.say(giy)

engine.runAndWait()

enh='c p u is at 62 percentage working '
engine.say(enh)

engine.runAndWait()

cdl='calculating your boady temperature and blood preasure sir'
engine.say(cdl)
engine.runAndWait()

vb='initialising data'
engine.say(vb)
engine.runAndWait()

bod='ohhooo i think ur quit nervous .'
engine.say(bod)
engine.runAndWait()

gh='sir u must always be calm'  
engine.say(gh)
engine.runAndWait()

lov='love you sir'
engine.say(lov)
engine.runAndWait()







