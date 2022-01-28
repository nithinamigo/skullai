import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
from gtts import gTTS
import cv2
import numpy as np
import random
from requests import get
import wikipedia
import winshell
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import geocoder
import requests
import instaloader
import instalooter
import PyPDF2
import operator
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from skull_2 import Ui_skullUi_3
import requests
from bs4 import BeautifulSoup
from pywikihow import WikiHow, search_wikihow
import psutil
import speedtest
import urllib.request

















engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()



#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak(f"Good morning, its {tt}")
    elif hour>12 and hour<18:
        speak(f"good afternon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    assname = "skull"
    speak("I am Skull. How can i help you")

#send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nithinkutty12345@gmail.com', 'nithinmalu2525')
    server.sendmail('nithinkutty12345@gmail.com', to, content)
    server.close()

#for news
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3ed4ae6b776545489b21e6eaa795d183'

    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day = ["first","second","third","fourth","fifth" "sixth","seventh","eight","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        #print(f"today's {day[i]} news is:", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

#audiobook
def pdf_reader():
    book = open('pyrob.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"total number of pages in this book {pages}")
    speak("please enter the page number i have to read")
    pg = int(input("please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        #self.TaskExecution()
        speak("say my name to activate boss")
        while True:
            self.query = self.takecommand()
            if "wake up" in self.query or "are you there" in self.query or "skull" in self.query or "cal" in self.query:
                self.TaskExecution()

    #to convert voice to text
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=5, phrase_time_limit=5)


        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")

        except Exception as e:
            speak("say that again...")
            return "none"
        query = query.lower()
        return query




    def TaskExecution(self):
        wish()
        while True:
        #if 1:
            self.query = self.takecommand().lower()

            #logic building for tasks

            if "open notepad" in self.query:
                speak("opening notepad boss")
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open command prompt" in self.query:
                speak("opening command prompt boss")
                os.system("start cmd")

            elif "what is the time now" in self.query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                speak("boss current time is " + time)

            elif "play" in self.query:
                song = self.query.replace('play', '')
                speak("good choice boss. playing " + song)
                kit.playonyt(song)

            elif "your voice" in self.query:
                speak("thanks for the compliment, boss")

            elif "volume up" in self.query:
                speak("increasing volume ")
                pyautogui.press("volumeup")

            elif "volume down" in self.query:
                speak("decreasing volume")
                pyautogui.press("volumedown")

            elif "volume mute" in self.query or "mute" in self.query:
                pyautogui.press("volumemute")






            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    if cv2.waitKey(10) == ord('q'):
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif "play music" in self.query:
                music_dir = "C:\\Users\\NITHIN PC\\Music\\music"
                songs = os.listdir(music_dir)
                #rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))

            elif "ip address" in self.query:
                ip = get('http://api.ipify.org').text
                speak(f"boss our ip adress is {ip} ")

            elif "who is" in self.query:
                person = self.query.replace('who is', '')
                info = wikipedia.summary(person, 2)
                print(info)
                speak(info)

            elif "are you single" in self.query:
                speak("I am in relationship with devil haha haha haha ha...")

            elif ("open youtube") in self.query:
                speak("opening youtube boss")
                webbrowser.open("www.youtube.com")

            elif ("open facebook") in self.query:
                speak("opening facebbok boss")
                webbrowser.open("www.facebook.com")

            elif ("open instagram") in self.query:
                speak("opening instagram boss")
                webbrowser.open("www.instagram.com")

            elif ("open twitter") in self.query:
                speak("opening twitter boss")
                webbrowser.open("www.twitter.com")

            elif ("open google") in self.query:
                speak("what do you want to know boss")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")

            elif "send whatsapp message" in self.query:
                kit.sendwhatmsg("+919965540070", "this is testing protocol",14,53)
                time.sleep(120)
                speak("message has been sent boss")

            elif "send message" in self.query:
                speak("what should i say")
                msz = self.takecommand()

                from twilio.rest import Client

                account_sid = 'AC83c828500d637b8f9a9d24cea35459cb'
                auth_token = '6f7b5de6a269e9ce3e7739c38eee19b3'

                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                        body = msz,
                        from_= '+12156081977',
                        to = '+918939331645'
                    )
                print(message.sid)
                speak("message has been sent")

            elif "make a phone call" in self.query:
                #speak("what should i say...")
                #mpz = self.takecommand()
                speak("calling...")

                from twilio.rest import Client

                account_sid = 'AC83c828500d637b8f9a9d24cea35459cb'
                auth_token = '6f7b5de6a269e9ce3e7739c38eee19b3'

                client = Client(account_sid, auth_token)

                message = client.calls \
                    .create(
                        twiml = '<Response><Say> this a testing message from skull...</Say></Response>',
                        from_= '+12156081977',
                        to = '+918939331645'
                    )
                print(message.sid)
                speak("message has been sent")

            elif "say hi to amma" in self.query:
                speak("hello amma, how are you?")




            elif "temperature" in self.query:
                search = self.takecommand().lower()
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"checking {search}")
                speak(f"boss, current {search} is {temp}")

            elif "advanced search" in self.query:
                speak("advance search is activated")
                while True:
                    speak("what do you want to know ")
                    how = self.takecommand().lower()
                    try:
                        if "exit" in how or "close" in how:
                            speak("advance search exited")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(how, max_results)
                            assert len(how_to) == 1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak("sorry, i could find it")

            elif "write a note" in self.query:
                speak("What should i write, sir")
                note = takeCommand()
                file = open('skull.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)
         
            elif "show note" in self.query:
                speak("Showing Notes")
                file = open("skull.txt", "r")
                print(file.read())
                speak(file.read(6))

            elif "power left" in self.query or "battery" in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"our system has {percentage} percent battery")
                if percentage>=75:
                    speak(" whohoo boss, system has enough power")
                elif percentage>=40 and percentage<=70:
                    speak("boss, system needs to be charged to continue work")
                elif percentage<=15 and percentage<=40:
                    speak("boss, connect to charing portal orelse system will shutdown")
                elif percentage<=15:
                    speak("come on boss, wake up system is shutting down soon...")

            elif "internet speed" in self.query:
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                speak(f"we have {dl} bit per second download speed and {up} bit per second uploading speed.")

                #try:
                 #   speed_net = os.system('cmd /k "speedtest"')
                  #  speak(speed_net)
                #except:
                 #   speak("there is no internet connection")
            

            #elif "play song on youtube" in self.query:
             #   kit.playonyt("silu silu")

        #    elif "email to avinash" in self.query:
        #        try:

        #            speak("what should i send?")
        #           content = takecommand().lower()
        #            to = "kuttygomathinithin@gmail.com"
        #            sendEmail(to,content)
        #            speak("Email has been sent to mom")

        #        except Exception as e:
        #            print(e)
        #            speak("sorry, i could not send this email")

            elif "shutdown" in self.query:
                speak("come on boss, why too soon. anyways have a dazzling day")
                sys.exit()

            #close any application
            elif "close notepad" in self.query:
                speak("okay, closing notepad boss")
                os.system("taskkill /f /im notepad.exe")

            elif "close browser" in self.query:
                speak("closing, browser boss")
                os.system("taskkill /im chrome.exe /f")

            elif "boss" in self.query or "don't call me boss" in self.query:
                speak("okay, my dear buddy")

            #set alarm
            elif "set alarm" in self.query:
                speak("tell me the time to set alarm. Like, set alarm to 5:30am")
                tt = self.takecommand()
                tt = tt.replace("set alarm to", "")
                tt = tt.replace(".", "")
                tt = tt.upper()
                import MyAlarm
                MyAlarm.alarm(tt)

            elif "open mobile camera" in self.query or "open mobile cam" in self.query:
                URL = "http://192.168.29.222:8080/shot.jpg"
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                    img = cv2.imdecode(img_arr,-1)
                    cv2.imshow('IPWebcam', img)
                    q = cv2.waitKey(1)
                    if q == ord("q"):
                        break;
                cv2.destroyAllWindows()
                

                #crack joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "turn off the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif 'lock window' in self.query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
            
            elif 'empty recycle bin' in self.query:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled")

            elif "camera" in self.query or "take a photo" in self.query:
                ec.capture(0, "skull Camera ", "img.jpg")

            elif "can you tweet" in self.query:
                speak("what should i tweet boss")
                cmm = self.takecommand().lower()
                tweet = cmm
                from twitterBot import account_info
                from account_info.txt import text

            elif "Good Morning" in self.query:
                speak("A warm" +query)
                speak("How are you ")
                speak(assname)

            elif 'open stack overflow' in self.query:
                speak("Here you go to Stack Over flow.")
                webbrowser.open("www.stackoverflow.com")  
               
                

            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me the news" in self.query:
                speak("please wait, fetching the news boss")
                news()

            elif "email to amma" in self.query:
                speak("what should i send")
                query = takecommand().lower()
                if "send a file" in self.query:
                    email = 'nithinkutty12345@gmail.com'
                    password = 'nithinmalu2525'
                    send_to_email = 'kuttygomathinithin@gmail.com'
                    speak("what is the subject for this mail")
                    query = takecommand().lower()
                    subject = query
                    speak("and, what the message for this mail")
                    query2 = takecommand().lower()
                    message = query2
                    speak("please enter the current path of the file into the shell")
                    file_location = input("please enter the path here: ")

                    speak("please wait, i am sending the mail now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    #setup the attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename = %s" % filename)

                    #attach the attachment to the MIMEMultipart object
                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("email has been sent to amma")

                else:
                    email = 'nithinkutty12345@gmail.com'
                    password = 'nithinmalu2525'
                    send_to_email = 'kuttygomathinithin@gmail.com'
                    message = query

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login('nithinkutty12345@gmail.com', 'nithinmalu2525')
                    server.sendmail(email, send_to_email, message)
                    server.quit()
                    speak("email has been sent to amma")


    #calculations

            elif "do some calculations" in self.query or "calculate" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("What do you want to calculate, for example: 1 plus 1")
                    print("Listening...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string=r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' : operator.__truediv__, 
                        }[op]
                def eval_binary_expr(op1, oper, op2):  # 5 plus 8
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("your result is ")
                speak(eval_binary_expr(*(my_string.split())))


            elif "where is" in self.query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")



    #find location

            elif "location" in self.query or "where are we" in self.query:
                speak("wait, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    #print(geo_data)
                    city = geo_data['city']
                    #state = geo_data['state']
                    country = geo_data['country']
                    speak(f"i think we are at {city} located in {country} ")
                except Exception as e:
                    speak("sorry, due some issues i could not trace the location")
                    pass

    #to check instagram profile

            elif "instagram profile" in self.query or "insta profile" in self.query:
                speak("enter the username correctly")
                name = input("Enter the username: ")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"here the profile of the user {name}")
                time.sleep(4)
                speak("would ypu like to download the profile picture of this account...")
                condition = takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("it's done, profile picture is saved in our main folder. do you need anything")
                else:
                    pass
                    
    #take screenshot

            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                speak("what should i name this screenshot file")
                name = takecommand().lower()
                speak("hold the screen for few seconds, i am taking the screenshot")
                time.sleep(2)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done, the screenshot is saved in the main folder. do you need anything")

    #to make audio book

            elif "read pdf" in self.query:
                pdf_reader()

    #hide your files in folder

            elif "hide all files" in self.query or "hide this folder"in self.query or "visible for everyone" in self.query:
                speak("do you want to hide this folder or make it visible to everyone")
                condition = takecommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d") #os module
                    speak("all the files in the folder are hidden")

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("all the files in the folder are visible to everyone. Do you want it to be hidden for safety")

                elif "leave it" in condition or "leave for now" in condition:
                    speak("ok")

            elif "hey" in self.query or "hello" in self.query or "hola" in self.query or "bonjour" in self.query:
                speak("Hola boss, do you need anything")
                
            elif "how are you" in self.query:
                speak("hey there, i am pretty good. what about you.")

            elif " also good" in self.query or "fine" in self.query:
                speak("that's great")

            elif "look good" in self.query:
                speak("as preety as always")

            elif "thank you" in self.query or "thanks" in self.query:
                speak("you're welcome")

            elif " you can sleep" in self.query or "sleep now" in self.query:
                speak("okay, call me anytime. zzz. zzz. zzz. ")
                sys.exit()
                break
                

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_skullUi_3()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.startTask)
        self.ui.pushButton_3.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../../Downloads/语音音波.gif")
        self.ui.skullUi.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../../Downloads/AlTq.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

        


app = QApplication(sys.argv)
skull = Main()
skull.show()
exit(app.exec_())






