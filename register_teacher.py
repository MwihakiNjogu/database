from main import Teacher
try:
    teacher_Name = input("Enter Name \n")
    teacher_Email = input("Enter Email \n")
    teacher_Password = input("Enter Password \n")

    Teacher.create( teacher_name = teacher_Name, teacher_email = teacher_Email,  teacher_password = teacher_Password)
    print("Teacher created successfully")

except:
    print("Failed to create teacher")
