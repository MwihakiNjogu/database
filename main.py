from peewee import *
from os import_path
connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join("mwihaki.db"))

#creating our first table

class Student(Model):
    stud_name = CharField()
    stud_email = CharField()
    stud_password = Charfield()

    class Meta:
        database = db

Student.create_table(fail_silently=True)



