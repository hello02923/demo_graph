# -*- coding: utf-8 -*-
"""
主程式檔
"""

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app import schema

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")