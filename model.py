# -*- coding: utf-8 -*-
"""
資料格式設定檔
"""

import strawberry
from datetime import datetime

@strawberry.type
class User:
    UserID: str
    IsLogin: bool
    Created_at: datetime

@strawberry.type
class Drink:
    channel: str
    name: str
    info: str








