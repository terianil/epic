import tkinter as tk
import json
import urllib.request
import urllib.parse
from urllib.error import URLError
from random import *

class DataPreparer:
    json_input = {'sender': 'jdog', 'receiver': 'pacman', 'message': 'awesome!', 'value' : 'X'}
    data = None
    mode = 1
    range1 = 5
    range2 = 15

    def __init__(self):
        self.__prepareJsonData()

    def setMode(self, mode, range1, range2):
        self.range1 = float(range1)
        self.range2 = float(range2)
        self.mode = mode
    def __prepareJsonData(self):
        self.data = json.dumps(self.json_input)
        self.data = self.data.encode('utf-8')

    def __generateRandom(self):
        if self.mode== 1:
            return randint(self.range1, self.range2)
        elif self.mode == 2:
            return gauss(self.range1, self.range2)
        else:
            return normalvariate(self.range1, self.range2)
        #return 'asdasd'
    def getData(self):
        self.json_input['value'] = self.__generateRandom()
        self.__prepareJsonData()
        return self.data

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
    normRandomRadio = None
    rangeInputText = None
    url = 'http://localhost:50001/inbound'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = None
    dataPreparer = DataPreparer()
    basicRandomFromInputText = None
    basicRandomToInputText = None
    gaussRandomFromInputText = None
    gaussRandomToInputText = None
    normalRandomFromInputText = None
    normalRandomToInputText = None

    def __init__(self):
        self.frame = tk.Tk()
        self.randomVar = tk.IntVar(self.frame);
        self.label = tk.Label(self.frame , fg="green")
        self.label.pack()
        self.startButton = tk.Button(self.frame, text='Start', width=25, command=self.start)
        self.startButton.pack()
        self.stopButton = tk.Button(self.frame, text='Stop', width=25, command=self.stop)
        self.stopButton.pack()

        # Range
        row = tk.Frame(self.frame)
        label = tk.Label(row, text='Insert delay (ms):')
        self.rangeInputText = tk.Entry(row, width=12)
        self.rangeInputText.insert(self.delay,str(self.delay))
        row.pack()
        label.pack(side=tk.LEFT)
        self.rangeInputText.pack(side=tk.RIGHT, fill=tk.X)

        label = tk.Label(self.frame, text='Choose random type:')
        label.pack()

        # basic random
        row = tk.Frame(self.frame)
        row.pack()
        label = tk.Label(row, text='from:')
        self.basicRandomFromInputText = tk.Entry(row, width=8)
        label2 = tk.Label(row, text='to:')
        self.basicRandomToInputText = tk.Entry(row, width=8)
        self.basicRandomRadio = tk.Radiobutton(row,text="Basic random", variable=self.randomVar, value =1)
        self.basicRandomRadio.pack()
        label.pack(side=tk.LEFT)
        self.basicRandomFromInputText.pack(side=tk.LEFT)
        self.basicRandomToInputText.pack(side=tk.RIGHT)
        label2.pack(side=tk.RIGHT)

        # gauss random
        row = tk.Frame(self.frame)
        row.pack()
        label = tk.Label(row, text='alpha:')
        self.gaussRandomFromInputText = tk.Entry(row, width=8)
        label2 = tk.Label(row, text='beta:')
        self.gaussRandomToInputText = tk.Entry(row, width=8)
        self.gaussRandomRadio = tk.Radiobutton(row,text="Gaussian distribution random", variable=self.randomVar, value =2)
        self.gaussRandomRadio.pack()
        label.pack(side=tk.LEFT)
        self.gaussRandomFromInputText.pack(side=tk.LEFT)
        self.gaussRandomToInputText.pack(side=tk.RIGHT)
        label2.pack(side=tk.RIGHT)

        # norm long random
        row = tk.Frame(self.frame)
        row.pack()
        label = tk.Label(row, text='mu:')
        self.normalRandomFromInputText = tk.Entry(row, width=8)
        label2 = tk.Label(row, text='sigma:')
        self.normalRandomToInputText = tk.Entry(row, width=8)
        self.normRandomRadio = tk.Radiobutton(row,text="Normal distribution random", variable=self.randomVar, value =3)
        self.normRandomRadio.pack()
        label.pack(side=tk.LEFT)
        self.normalRandomFromInputText.pack(side=tk.LEFT)
        self.normalRandomToInputText.pack(side=tk.RIGHT)
        label2.pack(side=tk.RIGHT)

    def randomRadioHandler(self):
        if self.randomVar.get() == 1:
            self.dataPreparer.setMode(self.randomVar.get(), self.basicRandomFromInputText.get(), self.basicRandomToInputText.get())
        elif self.randomVar.get() == 2:
            self.dataPreparer.setMode(self.randomVar.get(), self.gaussRandomFromInputText.get(), self.gaussRandomToInputText.get())
        elif self.randomVar.get() == 3:
            self.dataPreparer.setMode(self.randomVar.get(), self.normalRandomFromInputText.get(), self.normalRandomToInputText.get())

    def prepareJsonData(self):
        self.data = json.dumps(self.json_input)
        self.data = self.data.encode('utf-8')
    def sendRest(self):
        r = urllib.request.Request(self.url, self.dataPreparer.getData(), headers=self.headers, method=self.METHOD)
        try:
            response = urllib.request.urlopen(r)
        except URLError as e:
            print ('Error {0}'.format(e.reason))
    def count(self):
        if self.running == 1 :
            self.counter += 1
            self.label.config(text=str(self.counter))
            self.sendRest()
            self.label.after(self.delay, self.count)

    def start(self):
        self.randomRadioHandler()
        self.running = 1
        self.delay = int(self.rangeInputText.get())
        self.label.after(self.delay, self.count)
    def stop(self):
        self.running = 0
    def runWindow(self):
        self.frame.mainloop()




if __name__ == '__main__':
    main = Generator()
    main.runWindow()