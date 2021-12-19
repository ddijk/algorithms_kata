from stack import Stack

def reverse(input):
    s =  Stack()
 
    [s.push(e) for e in input]

    result = []
  
    [result.append(s.pop()) for e in input]

    return ''.join(result)
