from peewee import *
from os import path
connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join("mwihaki.db"))

#creating our first table

class Student(Model):
    stud_name = CharField()
    stud_phone = CharField()
    stud_email = CharField()
    stud_password = Charfield()

    class Meta:
        database = db

Student.create_table(fail_silently=True)



class Teacher(Model):
    teach_name = CharField()
    teach_email = CharField()
    teach_password = Charfield()
Teacher.create_table(fail_silently=True)


class Product(Model):
    prod_price = CharField()
    prod_quantity = CharField()
    prod_description = Charfield()
    prod_color = Charfield()


Product.create_table(fail_silently=True)

class Users(Model):
    usr_name = CharField()
    usr_phone = CharField()
    usr_email = Charfield()
    usr_password = Charfield()

User.create_table(fail_silently=True)