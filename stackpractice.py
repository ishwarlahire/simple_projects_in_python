class Stack:
    def __init__(self):
        self.values = []
    def push(self,element):
        self.values = [element] + self.values
    def pop(self):
        return self.values.pop(0)

S1 = Stack()
S1.push(10)
S1.push(20)
S1.push(30)
S1.push(40)
print(S1.values)
print(S1.pop())