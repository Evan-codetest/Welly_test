#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json

userIds = ['U01','U02','U03']
orderIds = ['T01','T02','T03','T04']
userOrders = [
    { 'userId': 'U01', 'orderIds': ['T01', 'T02'] },
    { 'userId': 'U02', 'orderIds': [] },
    { 'userId': 'U03', 'orderIds': ['T03'] },
]
userData = { 'U01': 'Tom', 'U02': 'Sam', 'U03': 'John' } 
orderData = {
'T01': { 'name': 'A', 'price': 499 }, 
'T02': { 'name': 'B', 'price': 599 },
'T03': { 'name': 'C', 'price': 699 }, 
'T04': { 'name': 'D', 'price': 799 }
} 

#先將userData與 userIds整合

user_result = []

for i in userData.items():
    user= {}
    #print(i[0],i[1])
    if i[0] in userIds:
        #print(i[0],i[1],2)
        user['id'] = i[0]
        user['name'] = i[1]
        user_result.append(user)

#將userOrders與orderData整合

order_result = []
        
for i in userOrders: #3個userOrders
    if i['userId'] in userIds:  #確認有使用者id
        orders=[]
        for i2 in i['orderIds']: #叫出order id
            order_data = {}
            for o in orderData.items(): #比對data若是有相符id 就將資料統整在order_data後加入orders
                if i2 == o[0]:                
                    order_data['id'] = i2
                    order_data['name'] = o[1]['name']
                    order_data['price'] = o[1]['price']
                    orders.append(order_data)
    #print(orders)
    order_result.append(orders)

total_result = []
for x,x2 in zip(user_result,order_result):
    final = {}
    final['user'] = x
    final['orders'] = x2
    total_result.append(final)
show = json.dumps(re,indent=2)
print(show)

