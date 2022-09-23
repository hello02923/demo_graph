# -*- coding: utf-8 -*-
"""
db互動取得資料
"""
from datetime import datetime
from pymongo import MongoClient
from model import (
    User, Drink
)
#%%
client = MongoClient('你的db在哪就連哪～', username='這是帳號要你改', password='這是密碼要你改')
#%%

# 取得用戶資料
async def get_users():
    return User(
        UserID='Mary',
        IsLogin=False,
        Created_at=datetime.now()
    )

# 取得飲料資料
async def get_drinks():
    data = list(
        client['Shop']['Drink'].find(
            {}, {'_id':0, 'channel':1, 'name':1, 'info':1}
        ).limit(3)
    )
    
    return list(Drink(
        channel = item.get('channel'),
        name = item.get('name'),
        info = item.get('info'),
    ) for item in data)
