class Position():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def key(self):
        return (self.x, self.y)
    
    def __repr__(self):
        return '{} {}'.format(self.x, self.y)