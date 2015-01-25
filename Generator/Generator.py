import tkinter as tk
import json
import urllib.request
import urllib.parse
from urllib.error import URLError

class Generator:
    METHOD = 'POST'
    counter = 0
    running = 0
    delay = 500
    randomVar = None
    frame = None
    label = None
    startButton = None
    stopButton = None
    basicRandomRadio = None
    gaussRandomRadio = None
    longNormRandomRadio = None
    rangeInputText = None
    url = 'http://localhost:50001/inbound'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    json_input = {'sender': 'jdog', 'receiver': 'pacman', 'message': 'awesome!'}
    data = None
    def __init__(self):
        self.frame = tk.Tk()
        self.randomVar = tk.IntVar(self.frame);
        self.label = tk.Label(self.frame , fg="green")
        self.label.pack()
        self.startButton = tk.Button(self.frame, text='Start', width=25, command=self.start)
        self.startButton.pack()
        self.stopButton = tk.Button(self.frame, text='Stop', width=25, command=self.stop)
        self.stopButton.pack()
        self.basicRandomRadio = tk.Radiobutton(self.frame,text="basic random", variable=self.randomVar, value =1, command=self.randomRadioHandler)
        self.basicRandomRadio.pack()
        self.gaussRandomRadio = tk.Radiobutton(self.frame,text="Gaussian distribution random", variable=self.randomVar, value =2, command=self.randomRadioHandler)
        self.gaussRandomRadio.pack()
        self.longNormRandomRadio = tk.Radiobutton(self.frame,text="long normal distribution random", variable=self.randomVar, value =3, command=self.randomRadioHandler)
        self.longNormRandomRadio.pack()
        self.rangeInputText = tk.Entry(self.frame, validate = 'key', validatecommand = self.validateNumeric)
        self.rangeInputText.pack()
        self.prepareJsonData()

    def randomRadioHandler(self):
        if self.randomVar.get() == 1:
            print("basic random")
        elif self.randomVar.get() == 2:
            print("Gaussian distribution random")
        else:
            print("long normal distribution random")
    def prepareJsonData(self):
        self.data = json.dumps(self.json_input)
        self.data = self.data.encode('utf-8')
    def sendRest(self):
        r = urllib.request.Request(self.url, self.data, headers=self.headers, method=self.METHOD)
        try:
            response = urllib.request.urlopen(r)
        except URLError as e:
            print ('Error {0}'.format(e.reason))
    def count(self):
        if self.running == 1 :
            self.counter += 1
            self.label.config(text=str(self.counter))
            self.sendRest()
            self.label.after(500, self.count)

    def start(self):
        self.running = 1
        self.label.after(500, self.count)
    def stop(self):
        self.running = 0
    def runWindow(self):
        self.frame.mainloop()

class DataPreparer:
    json_input = {'sender': 'jdog', 'receiver': 'pacman', 'message': 'awesome!'}


if __name__ == '__main__':
    main = Generator()
    main.runWindow()