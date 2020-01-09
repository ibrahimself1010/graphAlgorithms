class stack:
    def __init__(self):
        self.lst = []
    def push(self, a):
        return self.lst.append(a)
    def pop(self):
        return self.lst.pop()
    def isEmpty(self):
        return len(self.lst) == 0
    def peek(self):
        return self.lst[-1]

Graph = {A: {B, C}, B: {D, F}, C: {I, E}, D: {E, G}, E: {H, J}, F: {D, G}, G: {D, F}, H: {I, G}, I: {C, H}}
Visited = set()
Path = []
stac = stack()