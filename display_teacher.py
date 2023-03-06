from main import Teacher

teachers = Teacher.select()
for teacher in teachers:
    print(teacher.teacher_name, teacher.teacher_email, teacher.teacher_password)