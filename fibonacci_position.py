#!/usr/bin/env python
# coding: utf-8

# In[10]:


def fibonacci(position):
    if position < 2:  #不足2個數字
        return position
    n1,n2 = 1,1
    for i in range(2, position): 
        n1, n2 = n2, n1 + n2
    return n2

#使用
fibonacci(5)

