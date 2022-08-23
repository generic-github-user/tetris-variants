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
    

class Block:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        return self

class Piece:
    def __init__(self, x, y, board):
        self.x, self.y = x, y
        self.blocks = vec()
        self.board = board

    def move(self, dx, dy):
        #for b in self.blocks: b.move(dx, dy)
        self.x += dx
        self.y += dy
        return self

    def contains(self, x, y):
        return self.blocks.any(lambda b: b.x == x and b.y == y)

    def random(board, n=1):
        r = Piece(board.width // 2, board.height, board)
        r.blocks.append(Block(0, 0))
        deltas = list(itertools.product(*[[-1, 0, 1]]*2))[1::2]
        for i in range(n-1):
            r.blocks.append(Block(*random.choice(deltas)))
        return r

class Board:
    def __init__(self, w, h):
        self.width, self.height = w, h
        self.pieces = vec()

    def render(self):
        B = '-'*(self.width+2)*2
        print(B)
        for y in range(self.height, 0, -1):
            print('| ', end='')
            for x in range(0, self.width):
                matches = self.pieces.any(lambda p: p.contains(x-p.x, y-p.y))
                print(('##' if matches else '..'), end='')
            print(' |')
        print(B)
        return self

    def step(self):
        for p in self.pieces:
            x, y = p.x, p.y
            if p.blocks.none(lambda b: self.contains(b.x+x, b.y+y-1) or b.y+y <= 1):
                p.move(0, -1)

    def contains(self, x, y):
        return self.pieces.any(lambda p: p.contains(x, y))
