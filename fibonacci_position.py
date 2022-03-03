#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fibonacci(position):
    if position < 2:  #不足2個數字
        return position
    f1,f2 = 1,1
    for i in range(2, position): 
        f1, f2 = f2, f1 + f2
    return f2
fibonacci(1)

