import pyttsx3
import speech_recognition as sr
import time
import datetime
import wikipedia
import webbrowser
import subprocess
import os
import smtplib
from getpass import getpass
import random
import pyautogui as pag

'''MachineLearning class is define to play with some speech api avilable in python'''
class MachineLearning:
    def __init__(self):
        
        self.r1 = sr.Recognizer()
        self.r2 = sr.Recognizer()
        self.r3 = sr.Recognizer()
        self.m = sr.Microphone()
        try:
            self.engine = pyttsx3.init()
        except ImportError:
            print("driver not found")
        except RuntimeError:
            print("driver fails to initialize")
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',  'english+f3') #f1 to f5 for female voice
        self.engine.setProperty('rate', 180)#speaking speed
        self.custom = None  #to pass custom text to speak_()
        self.speak_('Starting personal assistant..')
    def get_install_voices(self):
        all_voices = self.voices
        for voice in all_voices:
            print("Voice:")
            print(" - ID: %s" % voice.id)
            print(" - Name: %s" % voice.name)
            print(" - Languages: %s" % voice.languages)
            print(" - Gender: %s" % voice.gender)
            print(" - Age: %s" % voice.age)
            time.sleep(0.9)
            self.engine.setProperty('voice', voice.id+'+f4')
            self.engine.setProperty('rate', 250)
            self.wish_message()

    
    def convert_to_text(self, voice):
        #print the voice as text
        print(voice)


    def wish_message(self):
        #welcome message
        persion = 'Sir,'
        priod = ''
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            priod = 'Morning'
        elif hour>=12 and hour<18:
            priod = 'Afternoon'
        else:
            priod = 'Evening'
        message = 'Good '+priod+' ' +persion+ " How can I help you?"
        self.speak_(message, 'blue')


    def sendEmail(self, to, messages, password):
        '''to send email you need to turn on allow less secure apps from which email id you gonna send and to do that just type
            less secure app access in google'''
        sender = 'gopal3493@gmail.com'
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, to, messages)
        server.close()

    def colored_msg(self, color, msg):
        switcher = {'red': u"\u001b[31m", 'green': u"\u001b[32m", 'yellow': u"\u001b[33m", 'blue': u'\u001b[34m',
                    'magenta': u'\u001b[35m', 'cyan': u'\u001b[36m', 'white': u'\u001b[37m'}
        ansi_color = switcher.get(color, "\u001b[37m")
        reset = u'\u001b[0m'
        res = ansi_color + msg + reset
        print(res)

    '''-------------------------------------various command operation methods------------------------'''
    def speak_(self, audio, color=None, custom=None):#custom param is used for customize out put
        # print(custom)
        if custom!=None:
            audio1 = 'You said, '+audio
        else:
            audio1 = audio
        #speak whatever it takes as an input
        # self.convert_to_text(audio)
        self.colored_msg(color, audio1)
        self.engine.say(audio1)
        self.engine.runAndWait()

    def exit_(self):
        self.speak_('Thanks for your time, Bye!', 'green')
        exit()

    def silent_(self):
        self.speak_("Ok I'm silent" )
        time.sleep(30)

    def wikipedia_(self, input):
        self.speak_("What to search?")
        query = self.listen_().lower()
        self.speak_("Serching wikipedia for " + query, 'green')
        result = wikipedia.summary(query, sentences=2)
        self.speak_('According to wikipedia..', 'white')
        self.speak_(result, 'yellow')

    def youtube_(self, input):
        query = input.replace("location", "")
        webbrowser.open('youtube.com')

    def google_(self):
        try:
            self.speak_('ok', self.custom)
            self.speak_("What to search?")
            search_query  = self.listen_().lower()
            self.speak_("Serching google for " + search_query)
            webbrowser.open("https://google.com/search?q="+''.join(search_query))
        except Exception as e:
            print(e)
            self.speak_("Sorry something went wrong!", 'red')

    def terminal_(self):
        self.speak_('Ok')
        os.system("gnome-terminal")

    def music_(self, input):
        self.speak_('Ok Playing..', 'green')
        music_folder = '/home/gopal/Music/'
        mp3 = '/home/gopal/Music/SampleAudio_0.7mb.mp3'
        music = ['SampleAudio_0.7mb', 'mp3downloadfree_2coldmp3', 'jamalxganja_iloveit', 'hardkorerapbeats_dripmode', 'daheadcutta_circleblades']
        random_music = music_folder + random.choice(music) + '.mp3'
        self.play = subprocess.call(['xdg-open', random_music])  # using linux default payer
        # webbrowser.open(music_dir) #user web browser
        # os.system(mp3)

    def location_(self, input):
        location = input.replace("location of", "")
        self.speak_("Showing location of " + location)
        webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")  # user web browser

    def jira_(self, input):
        try:
            while True:
                self.speak_("What is the ticket number?")
                ticket_no  = self.listen_().lower()
                self.speak_(ticket_no, 'blue', self.custom)
                flag = 0
                while True:
                    self.speak_("Is that ok? yes or no.", "yellow")
                    response = self.listen_().lower()
                    if 'yes' in response or 'yeah' in response:
                        flag = 1
                        break
                    elif 'no' in response:
                        flag = 0
                        break
                    else:
                        continue
                #end inner loop
                if flag==1:
                    break
                else:
                    continue
                #end outer loop
            self.speak_("Opening ticket no " + ticket_no)
            webbrowser.open("https://jira.int.zone/browse/DE2-"+ticket_no)
        except Exception as e:
            print(e)
            self.speak_("Sorry something went wrong!", 'red')


    def email_(self, input):
        try:
            while True:  # continue iterating if u say no in the inner loop
                self.speak_("What should I send?", 'white')

                while True:
                    text = self.listen_().lower()
                    print(text)
                    if text == 'please say that again.':
                        continue
                    else:
                        break

                self.speak_(text, 'blue', self.custom)  # custom = 'True'
                flag = 0
                while True:  # continue iterating untill u say yes or no
                    self.speak_("\nIs that ok? yes or no.", 'yellow')
                    response = self.listen_().lower()
                    if 'yes' in response:
                        flag = 1
                        break
                    elif 'no' in response:
                        flag = 0
                        break
                    else:
                        continue
                # end inner while

                if flag == 1:
                    break
                else:
                    continue
            # end outer while
            while True:
                self.speak_('Please type gmail password', 'magenta')
                self.password  = pag.password("Password: ") #confirm(), alert(), and prompt()
                if self.password !=None or self.password!='':
                    break
                else:
                    continue
            # self.password = getpass()
            to = 'dasbairagyagopal@gmail.com'
            self.sendEmail(to, text, self.password)
            self.speak_("Email sent!", 'green')

        except Exception as e:
            print(e)
            self.speak_("Sorry, something went wrong!", 'red')


    def list_command_(self):
        self.colored_msg('yellow',"\nCOMMANDS")
        msg = "*" * 9
        self.colored_msg('magenta', msg)
        self.colored_msg('cyan', "[what can you do]")
        self.colored_msg('cyan', "[list commands]")
        self.colored_msg('cyan', "[wikipedia]")
        self.colored_msg('cyan', "[open google]")
        self.colored_msg('cyan', "[open youtube]")
        self.colored_msg('cyan', "[open jira/ticket]")
        self.colored_msg('cyan', "[open terminal]")
        self.colored_msg('cyan', "[play music]")
        self.colored_msg('cyan', "[send email]")
        self.colored_msg('cyan', "[location of ...]")
        self.colored_msg('cyan', "[silent]")
        self.colored_msg('cyan', "[ok bye]")
        msg = "*" * 21
        self.colored_msg('magenta', msg)

    def i_do_(self):
        can =  ['list commands', 'search wikipedia', 'open google', 'open youtube', 'open jira tickets', 'play music', 'send email', 'show location']
        self.speak_('I can,')
        for do in can:
            self.speak_(do)


    '''----------------------------------various command operation methods ends------------------------'''

    def process_cmd(self, input): #3 process the input command

        if 'ok bye' in input or 'bye' in input or 'quit' in input:
            self.exit_()
        elif 'silent' in input or 'chup' in input or 'hold on' in input:
            self.silent_()
            return
        elif 'wikipedia' in input: #search wikipedia
            self.wikipedia_(input)
            return
        elif 'open youtube' in input: #open youtube
            self.youtube_(input)
            return
        elif 'open google' in input or 'search google' in input:
            self.google_()
            return
        elif 'open terminal' in input or 'terminal' in input:
            self.terminal_()
            return
        elif 'play music' in input: #play mp3
            self.music_(input)
            return
        elif 'stop music' in input: #stop currently opend the music
            pass
        elif 'location of' in input:  #show location in the map
            self.location_(input)
            return
        elif 'send email' in input or 'email' in input: #send email
            self.email_(input)
            return
        if 'open jira' in input or 'jira' in input or 'ticket' in input:
            self.jira_(input)
            return
        if 'commands' in input:
            self.speak_('OK', color='green')
            self.list_command_()
            return
        if 'what can you do' in input:
            self.i_do_()
            return
        else:
            self.speak_(input, 'yellow', self.custom)

    def listen_(self): #2 get the input from microphone and return string output
        self.speak_("\nI'm listening..")
        voice_text = ''
        with sr.Microphone() as source:  # device_index=6 for sennheiser microphone with my system

            self.r1.adjust_for_ambient_noise(source)# This filters noise
            self.r1.pause_threshold = 1
            self.r1.energy_threshold = 400
            audio = self.r1.listen(source, phrase_time_limit = 5)
        try:

            voice_text = self.r2.recognize_google(audio)  # convert audio to text
            self.custom = True #for print output with custom color


        except sr.UnknownValueError:
            voice_text = "Please say that again."
            self.custom = None

        except sr.RequestError as e:
            print(e)
            voice_text = "No internet connection." # the API key didn't work
            self.custom = None
            time.sleep(2)

        finally:
                voice_text = voice_text
        # print(voice_text)
        return voice_text

    def execute(self): #1 list avaiable voice commands and process those
        self.list_command_()

        self.wish_message()
        while True:
            input_ = self.listen_().lower()  # retun voice as text
            self.process_cmd(input_) #main function to process voice commands


    def get_microphone_list(self):
        miclist = sr.Microphone.list_microphone_names()

        for index, name in enumerate(miclist):
            print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


    def test(self):
            message = 'Salman Khan (pronounced [səlˈmaːn ˈxaːn]; Hindi: pronunciation ; born Abdul Rashid Salim Salman Khan; 27 December 1965) is an Indian film actor, producer, occasional singer and television personality. In a film career spanning over thirty years, Khan has received numerous awards, including two National Film Awards as a film producer, and two Filmfare Awards for acting.'
            self.speak_(message)


'''Main class to call machine learning class'''
class Main:
    def __init__(self):
        obj = MachineLearning()
        obj.execute()


'''This is a test class to quickly test anything'''
class Test:
    def __init__(self):
        obj = MachineLearning()
        obj.music_('test')
        # obj.get_microphone_list()
        # obj.listen_()


if __name__=='__main__':

    ob = Main()
    # ob = Test()


