#a stack is a stack lol,its literally a stack whereby you add items on to each other but you cant add in-between them
class Stack :
    def __init__(self):
        self.stack = []

    
    def push (self , item):
        self.stack.append(item)


    def pop(self):
        return self.stack.pop()


    def peek (self):
        last_element = self.stack[len(self.stack)- 1]
        return last_element

stack1 =Stack()
stack1.push (5)
stack1.push(3)
stack1.push(7)

top_element = stack1.peek()
print (top_element)