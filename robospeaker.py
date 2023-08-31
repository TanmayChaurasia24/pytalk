import pyttsx3

if __name__ == '__main__':
    print("-------------------Welcome to pytalk, created by tanmay------------------------------")
    s = 'not'
    while True:
        engine = pyttsx3.init()
        s = input("What do you want me to speak: ")
        if(s == 'what is your name'):
            engine.setProperty('rate',100)
            engine.say("my name is pytalk i was created by tanmay")
            engine.runAndWait()
            continue


        if(s == 'exit'):
            engine.setProperty('rate',80)
            engine.say("bye bye friend")
            engine.runAndWait()
            break
      
        engine.setProperty('volume',0.9)
        engine.setProperty('rate',100)

        engine.say(s)
        engine.runAndWait()
        
     
   
