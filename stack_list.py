#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Stack:
    def __init__(self):
        self.stack = []  #資料存於串列中
        self.sizes = 0

    def push(self, data):  
        self.stack.append(data) 
        self.sizes += 1

    def pop(self):  
        if self.sizes == 0:
            print("Stack is empty.")
        else:
            print(self.stack[-1])
            self.stack.pop()  
            self.sizes -= 1

    def size(self): 
        print(self.sizes)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.size()

