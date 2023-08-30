#from typing import Union
from fastapi import FastAPI, Request
from pymongo import MongoClient

app = FastAPI()



#connection with
conn = MongoClient("mongodb+srv://user:xnJ1DrKpsxznvk6o@cluster0.wizcknx.mongodb.net")


