import os

from flask import Flask
from dotenv import load_dotenv

from peewee import *

load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("APP_SECRET")

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase("file:memory?mode=memory&cache=shared", uri=True)
else:
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306,
    )

print(mydb)

from .models.timelinepost import TimelinePost

mydb.connect()
mydb.create_tables([TimelinePost])

from . import routes
