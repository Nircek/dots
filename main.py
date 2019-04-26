#!/usr/bin/env python3
from tkinter import Tk, Canvas
from threading import Thread

class Dot:
    pass

class Dots(Tk):
    def __init__(self):
        self.w = Canvas(self)
        self.d = []
        self.t = Thread(target=self.physics)
        self.w.pack()
        self.w.bind('<Button-1>', lambda ev: self.new(ev.x, ev.y))
        self.t.start()
    def new(self, x, y):
        pass
    def physics(self):
        while True:
            pass

if __name__ == '__main__':
    dots = Dots()
    dots.mainloop()
