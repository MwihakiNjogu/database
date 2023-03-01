from main import Student
try:
    student_name = input("Enter name \n")
    student_phone = input("Enter phone \n")
    student_email = input("Enter email \n")
    student_password = input("Enter password \n")

    Student.create(stud_name=student_name, stud_phone=student_phone,  stud_email=student_email, stud_password=student_password)
    print("Student created successfully")
except:
      print("Failed to create student")