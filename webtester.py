import webbrowser #pip install webbrowser
import pyttsx3 #pip install pyttsx3
import sys 

engine=pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate',188)

volume = engine.getProperty("volume")
engine.setProperty("volume",1000)

ji=int(input('Enter the limit '))
for i in range(ji):

    print('''
    
            [1] Google           [6]  mypage
            [2] instagra                    
            [3] facebook                         
            [4] github                   
            [5] whatsapp                    ''')
    opt=int(input('Enter the number :'))
    if opt==1:
        webbrowser.open('www.google.com')
        gh='ok sir opening google'
        engine.say(gh)
        engine.runAndWait()
    elif opt==2:
        webbrowser.open('www.instagram.com')
        hj='ok sir opening instagram'
        engine.say(hj)
        engine.runAndWait()

    elif opt==3:
        webbrowser.open('www.facebook.com')
        gh='ok sir opening facebook'
        engine.say(gh)
        engine.runAndWait()

    elif opt==4:
        webbrowser.open('www.github.com')
        gh='ok sir opening github'
        engine.say(gh)
        engine.runAndWait()

    elif opt==5:
        webbrowser.open('www.whatsapp.com')
        gh='ok sir opening whatsup'
        engine.say(gh)
        engine.runAndWait()

    elif opt==6:
        webbrowser.open('www.github.com/joshanjohn')
        gh='ok sir  '
        hj='here we go '
        engine.say(gh)
        engine.say(hj)
        engine.runAndWait()
    else:
        gh='ohoo that was a out of given options'
        engine.say(gh)
        engine.runAndWait()
