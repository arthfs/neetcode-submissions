class MinStack:

    def __init__(self):
        self.mins = []
        self.ref = []

    def push(self, val: int) -> None:
        if self.ref != []:
            if val < self.mins[-1]:
                self.mins.append(val)
            else:
                self.mins.append(self.mins[-1])
        else:
            self.mins.append(val)
            
        self.ref.append(val)

    def pop(self) -> None:
        removed = self.ref.pop()
        
        self.mins.pop()

    def top(self) -> int:
        return self.ref[-1]

    def getMin(self) -> int:
        return self.mins[-1]
        
