import tkinter as tk
import json
import urllib.request
import urllib.parse
from urllib.error import URLError

class Generator:
    METHOD = 'POST'
    counter = 0
    running = 0
    range = 500
    think = None
    label = None
    button = None
    button2 = None
    url = 'http://localhost:50001/inbound'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    json_input = {'sender': 'jdog', 'receiver': 'pacman', 'message': 'awesome!'}
    data = None
    def __init__(self):
        self.think = tk.Tk()
        self.label = tk.Label(self.think , fg="green")
        self.label.pack()
        self.button = tk.Button(self.think, text='Start', width=25, command=self.start)
        self.button.pack()
        self.button2 = tk.Button(self.think, text='Stop', width=25, command=self.stop)
        self.button2.pack()
        self.prepareJsonData()
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
        self.think.mainloop()

if __name__ == '__main__':
    main = Generator()
    main.runWindow()