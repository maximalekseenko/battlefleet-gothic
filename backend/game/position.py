class position:
    ''''''

    def copy(self):
        return position(self.x, self.y)

    
    def __init__(self, x:float, y:float) -> None:
        self.x:float = x
        self.y:float = y
    

    def __getitem__(self, key:int) -> int:
        if key == 0: return self.x
        elif key == 1: return self.y
        else: raise KeyError(f"Wrong key '{key}' for position. Key must be 0 for x or 1 for y.")

    
    def __add__(self, __o):
        try:
            return position(self[0] + __o[0], self[1] + __o[1])
        except: raise TypeError(f"Cannot add '{__o}' to position")


    def __sub__(self, __o):
        try:
            return position(self[0] - __o[0], self[1] - __o[1])
        except: raise TypeError(f"Cannot substract '{__o}' to position")

