#!/usr/bin/env python3
from tkinter import Tk, Canvas, ALL, BooleanVar
from threading import Thread
from time import sleep

class Dot:
    def __init__(self, x, y, vx=0, vy=0):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
    def update(self):
        self.x += self.vx
        self.y += self.vy
    def render(self, w):
        (lambda w,x,y,r:w.create_oval(x-r,y-r,x+r,y+r))(w, self.x, self.y, 5)

class Dots(Tk):
    def __init__(self):
        super().__init__()
        self.w = Canvas(self, bg='#aaa')
        self.d = []
        self.t = Thread(target=self.physics, daemon=True)
        self.g = .04
        self.closing = False
        self.start = BooleanVar(self)
        self.w.pack()
        self.w.bind('<Button-1>', lambda ev: self.new(ev.x, ev.y))
        self.bind('<space>', lambda ev: self.start.set(not self.start.get()))
        self.protocol('WM_DELETE_WINDOW', self.on_close)
        self.t.start()
    def on_close(self):
        self.closing = True
        self.destroy()
    def new(self, x, y):
        self.d += [Dot(x, y)]
    def physics(self):
        try:
            while not self.closing:
                if self.d:
                    x = sum([e.x for e in self.d]) / len(self.d)
                    y = sum([e.y for e in self.d]) / len(self.d)
                    self.w.delete(ALL)
                    for e in self.d:
                        if self.start.get():
                            e.vx += self.g*(x - e.x)
                            e.vy += self.g*(y - e.y)
                            e.update()
                        e.render(self.w)
                sleep(1/20)
        except:
            if not self.closing:
                raise

if __name__ == '__main__':
    dots = Dots()
    dots.mainloop()
