from tkinter import *       # gui
from tkinter import ttk     # gui
import webbrowser      # This opem default browser 
import speech_recognition as sr
from pygame import mixer # prompt after clicking voice  search
from selenium.webdriver.common.keys import Keys # google cloud speech API to keep private

class MyVoice(Widget):
    def __init__(self, root):
        '''This Pop-up gui for search bar
        deals all outer side functionality'''

        # master & frame
        self.root = root
        self.frame = ttk.Frame(master=root, width=400, height=400)
        
        # title 
        self.root.title("Universal Seearchbar")

        # image, icon
        self.root.iconbitmap('mic.ico') # title image
        self.photo = PhotoImage(file='microphone.png').subsample(15,15) # title image

        # Style
        self.style = ttk.Style()
        self.style.theme_use('winnative')

        # stringVar()
        self.btn = StringVar()

        # label & entry
        self.label_1 = ttk.Label(self.frame, text='Query') # label 
        self.entry_1 = ttk.Entry(self.frame, width=50) # entry
        
        # Submit Buttons
        self.submitButton_search = ttk.Button(self.frame, text='Search', width=10, command=self.click_searchButton)
        self.submitButton_mic = Button(self.frame, image=self.photo, bd=0,
                activebackground='#c1bfbf',
                 overrelief='groove', relief='sunken',
                command=self.micButton_Call)

        # Radio Button
        self.radioButton_goolge = ttk.Radiobutton(self.frame, text='Google', value='google', variable=self.btn) # google
        self.radioButton_duck = ttk.Radiobutton(self.frame, text='Duck', value='duck', variable=self.btn) # duck
        self.radioCutton_amz = ttk.Radiobutton(self.frame, text='Amz', value='amz', variable=self.btn) # amz
        self.radioCutton_ytb = ttk.Radiobutton(self.frame, text='Ytb', value='ytb', variable=self.btn) # ytb

        # griding
        self.frame.grid(row=0, column=0) # frame

        self.label_1.grid(row=0, column=0) # label
        self.entry_1.grid(row=0, column=1, columnspan=4) # entry
        
        # Radio Buttons griding
        self.radioButton_goolge.grid(row=1, column=1, sticky=W) # google
        self.radioButton_duck.grid(row=1, column=2,sticky=W) # duck
        self.radioCutton_amz.grid(row=1, column=3)           # amz
        self.radioCutton_ytb.grid(row=1, column=4, sticky=E) # ytb

        # Submit Buttons
        self.submitButton_mic.grid(row=0, column=5) # mic
        self.submitButton_search.grid(row=0, column=6) # search

        self.entry_1.bind('<Return>', self.enterKey_bind) # Enter key = binding
        self.entry_1.focus()              # cursor on entry
        self.btn.set('google')      # set radio button on google by default
        self.root.wm_attributes('-topmost', 1)

    def enterKey_bind(self, event):
        '''Only Enter key call this method as Submit Button can't handle event handlers'''

        print('method called: enterKey_bind')
        if (self.btn.get() == 'google') and (self.entry_1.get()):
            webbrowser.open(f'http://google.com/search?q={self.entry_1.get()}')
        
        elif (self.btn.get() == 'duck') and (self.entry_1.get()):
            webbrowser.open(f'http://duckduckgo.com/?q={self.entry_1.get()}')

        elif (self.btn.get() == 'amz') and (self.entry_1.get()):
            webbrowser.open(f'https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords={self.entry_1.get()}')

        elif (self.btn.get() == 'ytb') and (self.entry_1.get()):
            webbrowser.open(f'https://www.youtube.com/results?search_query={self.entry_1.get()}')

        else:pass
    
    def click_searchButton(self):
        '''This called when submit button striked.
        This method is copy of enterKey_bind method as event handlers can;t handle them'''

        print('method called: click_searchButton')
        if self.btn.get() == 'google':
            webbrowser.open(f'http://google.com/search?q={self.entry_1.get()}')
        
        elif self.btn.get() == 'duck':
            webbrowser.open(f'http://duckduckgo.com/?q={self.entry_1.get()}')

        elif (self.btn.get() == 'amz') and (self.entry_1.get()):
            webbrowser.open(f'https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords={self.entry_1.get()}')

        elif (self.btn.get() == 'ytb') and (self.entry_1.get()):
            webbrowser.open(f'https://www.youtube.com/results?search_query={self.entry_1.get()}')

        else:pass

    def micButton_Call(self):
        '''This deals only mic button to recognize voice'''

        print('Method called: micButton_Call')
        mixer.init() # init. mixer
        mixer.music.load('chime1.mp3') # locating mp3
        mixer.music.play() # play loaded mp3
        
        r = sr.Recognizer() # Recognizer instance, deals collection of speech recognition settings, functionality
        r.pause_threshold = 0.7 # minimum length of silence (in seconds) that will register as the end of a phrase
                                # Smaller values result in the recognition completing more quickly, but might result in slower speakers being cut off.
        r.energy_threshold = 400 # threshold is associated with the perceived loudness of the sound.

        with sr.Microphone() as source:         # open the microphone and start recording
                                                # do things here - ``source`` is the Microphone instance created above
                                                # the microphone is automatically released at this point
            try:
                audio = r.listen(source, ) # timeout=5  # Source - r = sr.Microphone() as source
                                                        # The timeout parameter is the maximum number of seconds that this will wait for a phrase
                                                        # to start before giving up and throwing an speech_recognition.WaitTimeoutError exception.
                                                        #  If timeout is None, there will be no wait timeout.
                
                # google_api_key = 'AIzaSyCzyWPbso4cxgGPJYHFT-XOr_3W0cJPSHo'
                print('Speaking...')
                message = str(r.recognize_google(audio))
                print(f'You said; {message}')
                mixer.music.load('chime2.mp3')
                mixer.music.play()
                self.entry_1.focus()
                self.entry_1.delete(0, END)
                self.entry_1.insert(0, message)
                
                # self.enterKey_bind()

            except sr.UnknownValueError:
                print('Google Speech Recognition could not understand audio')

            except sr.RequestError as e:
                print('Could not request results from Google Speech Recognition Service')

            else: pass

root = Tk()
MyVoice(root)
root.mainloop()