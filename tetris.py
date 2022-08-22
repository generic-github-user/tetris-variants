import time
#import keyboard
from pynput import keyboard

#import curses
#stdscr = curses.initscr()

class vec:
    def __init__(self, items=None):
        if items is None: items = []
        self.items = items
        
    def map(self, f): return vec(map(f, self.items))
    def all(self, p): return all(p(i) for i in self.items)
    def any(self, p): return any(p(i) for i in self.items)
    def none(self, p): return not self.any(p)

    def len(self): return len(self.items)
    def __iter__(self): return self.items.__iter__()
    def append(self, x): return self.items.append(x)
