class MinStack:
    def __init__(self):
        self.mins: List[int] = []  # indexes of minimal
        # element at the moment of pushing nth element
        self.stack: List[int] = []  # stack

    def push(self, val: int) -> None:
        self.stack.append(val)  # add to stack
        if len(self.mins) == 0:  # if first, mark it the min
            self.mins.append(0)
        else:
            if val < self.stack[self.mins[-1]]:
                self.mins.append(len(self.stack) - 1)
            # if val < min, mark it the min element
            else:
                self.mins.append(self.mins[-1])
            # else keep the previous value as min

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        el = self.stack[-1]
        return el

    def getMin(self) -> int:
        return self.stack[self.mins[-1]]


"""
Done in 15-20 minutes, passed in first try :)
"""
