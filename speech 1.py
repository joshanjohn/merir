import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate",150)

volume = engine.getProperty("volume")
engine.setProperty("volume",150)

voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

say = "at your service sir, mariya john is a  thadiyathii who always vedaal valli but that is her one of her hobby she use study every time . she is also know as tik tok . her brother joshan john is a quite cool guy who used to be good  "
engine.say(say)

engine.runAndWait()


