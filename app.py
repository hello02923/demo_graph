# -*- coding: utf-8 -*-
"""
資料架構檔
"""

import strawberry
import typing
from data import (
    get_users, get_drinks
)
from model import (
    User, Drink
)

@strawberry.type
class Query:
    users: User = strawberry.field(resolver=get_users)
    drinks: typing.List[Drink] = strawberry.field(resolver=get_drinks)

schema = strawberry.Schema(Query)

