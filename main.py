#!/usr/bin/env python3
from tkinter import Tk, Canvas
from threading import Thread

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
        self.t = Thread(target=self.physics)
        self.closing = False
        self.w.pack()
        self.w.bind('<Button-1>', lambda ev: self.new(ev.x, ev.y))
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
                for e in self.d:
                    e.update()
                    e.render(self.w)
        except:
            if not self.closing:
                raise

if __name__ == '__main__':
    dots = Dots()
    dots.mainloop()
