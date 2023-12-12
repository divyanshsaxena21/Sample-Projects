import datetime
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
print ("Login time: ", current_time)

import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',140)
engine.say("HELLO SIR!!")
engine.say("I AM YOUR PERSONAL AI")
engine.say("HOW ARE YOU SIR?")
engine.runAndWait()

def greet():
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate',110)
    engine.say("GOOD TO HEAR THAT SIR")
    engine.say("HOW MAY I HELP YOU??")
    engine.runAndWait()

def date():
    import pyttsx3
    import datetime
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    date = datetime.date.today()
    day = date.strftime('%A')
    engine.say("Today's date is:")
    engine.say(date)
    engine.say("And Day is :")
    engine.say(day)
    print("Today's date is:", date)
    print("Today's day is: ", day)
    engine.runAndWait()

def time():
    import pyttsx3
    import datetime
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    engine.say("Current time:")
    engine.say(current_time)
    print("Current time: ", current_time)
    engine.runAndWait()

def myname():
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate',90)
    engine.say("Divyansh")
    engine.runAndWait()


def browse():
    import webbrowser
    url= ""
    while True:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate',110)
        a= input("What you want to search: ")
        if a.lower()=='google':
            url="google.com"
            engine.say("OPENING GOOGLE")
            engine.runAndWait()
        if a.lower() == 'youtube':
            url="https://www.youtube.com/"
            engine.say("OPENING YOUTUBE")
            engine.runAndWait()
        if a.lower() in ['play music', 'listen to music', 'music','songs','play songs']:
            url="https://gaana.com/"
            engine.say("opening music")
            engine.runAndWait()
        if a.lower() =='anime':
            url= "https://animixplay.to/?from=com"
            engine.say("SHOWING ANIME")
            engine.runAndWait()
        if a.lower() == "latest news":
            ask= input("Indian or International news: ")
            if ask.lower() in ['indian', 'indian news']:
                url ="aajtak.in"
                engine.say("SHOWING LATEST INDIAN NEWS")
                engine.runAndWait()
            if ask.lower() in ['international','international news']:
                url="https://us.cnn.com/"
                engine.say("SHOWING LATEST INTERNATIONAL NEWS")
                engine.runAndWait()
        if a.lower()=='wikipedia':
            url="https://www.wikipedia.org/"
            engine.say("OPENING WIKIPEDIA")
            engine.runAndWait()
        if a.lower() in ['exit', 'stop', 'end','close','close browsing']:
            import pyttsx3
            engine = pyttsx3.init()
            engine.setProperty('rate',110)
            engine.say("EXITING BROWSER")
            engine.runAndWait()
            break

        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get("chrome").open_new_tab(url)

    
def selfintro():
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate',110)
    engine.say("I AM AI VERSION 2.0 DEVELOPED BY DIVIYANSH IN THE PERIOD 2019-2022")
    engine.say("I CAN PERFORM VARIOUS TASKS LIKE, BROWSING THE INTERNET, TELLING CURRENT DATE AND TIME")
    engine.say("I AM GLAD TO OFFER MY HELP IN ANYWAY POSSIBLE")
    engine.say("I AM STILL UNDER- DEVELOPMENT AND VARIOUS NEW FEATURES WILL BE ADDED WITH TIME")
    print("I can tell current Date and Time\nYou can browse the internet, listen to music")
    engine.runAndWait()
    
def stop():
    import datetime
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Logout time: ", current_time)
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate',110)
    engine.say("THANK YOU SIR!!")
    engine.say("HAVE A GOOD DAY SIR.")
    engine.runAndWait()

    

#main
print("For information regarding software type->\tINFO")
while True:
    a=input("Enter the command: ")      

    if a.lower() in ["tell current time", 'current time','time',"tell today's date", "today's date","tell today date","today date","date",'good', 'great' , 'excellent','tell my name', 'who am i','who am i?',"browse", 'surf the internet',
                     'introduce yourself', 'who are you','who are you?', 'give self introduction','give self intro','self intro','info','stop','close','exit','end']:
        if a.lower() in ["tell current time", 'current time','time']:
            time()
        if a.lower() in ["tell today's date", "today's date","tell today date","today date","date"]:
            date()
        if a.lower() in ['good', 'great' , 'excellent']:
            greet()
        if a.lower() in ['tell my name', 'who am i','who am i?']:
            myname()
        if a.lower() in ["browse", 'surf the internet']:
            browse()
        if a.lower() in ['introduce yourself', 'who are you','who are you?', 'give self introduction','give self intro','self intro', 'info']:
            selfintro()       
        if a.lower() in ['stop','close','exit','end']:
            stop()
            break
    else:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate',110)
        print("ERROR!!")
        engine.say("INVALID COMMAND")
        engine.runAndWait()
