
class Stack:

    def __init__(self ):
         self.a = []

    def push(self, e):
         self.a.append(e)


    def pop(self):
        n = len(self.a)    
        if not n:
             return None

        result = self.a[n-1]
    
        self.a = self.a[:-1]

        return result

