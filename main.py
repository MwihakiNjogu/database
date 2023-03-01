from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "mwihaki.db"))


# creating our first table

class Student(Model):
    stud_name = CharField()
    stud_phone = CharField()
    stud_email = CharField()
    stud_password = CharField()

    class Meta:
        database = db


Student.create_table(fail_silently=True)

class Teacher(Model):
    teacher_name = CharField()
    teacher_email = CharField()
    teacher_password = CharField()

    class Meta:
       database = db

Teacher.create_table(fail_silently=True)

class Product(Model):
      product_price = CharField()
      product_quantity = CharField()
      product_description = CharField()

      class Meta:
         database = db

Product.create_table(fail_silently=True)

class User(Model):
      user_name = CharField()
      user_phone = CharField()
      user_email = CharField()
      user_password = CharField()

      class Meta:
          database = db
User.create_table(fail_silently=True)