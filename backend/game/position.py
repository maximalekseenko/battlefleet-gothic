class position:
    ''''''

    def copy(self):
        return position(self.x, self.y)

    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    

    def __str__(self):
        return f'[{self.x};{self.y}]'


    def __getitem__(self, key):
        if key == 0: return self.x
        elif key == 1: return self.y
        else: raise KeyError(f"Wrong key '{key}' for position. Key must be 0 for x or 1 for y.")

    
    def __add__(self, __o):
        try:
            return position(self.x + __o[0], self.y + __o[1])
        except: raise TypeError(f"Cannot add '{__o}' to position")


    def __sub__(self, __o):
        try:
            return position(self.x - __o[0], self.y - __o[1])
        except: raise TypeError(f"Cannot substract '{__o}' to position")


    def __iter__(self):
        self._i = 0
        return self


    def __next__(self):
        self._i += 1
        if self._i == 1: return self.x
        if self._i == 2: return self.y
        else: raise StopIteration


    def __eq__(self, __o: object) -> bool:
        try:
            return self.x == __o[0] and self.y == __o[1]
        except: return False