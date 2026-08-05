student_name = input("Enter the Student Name: ")
roll_number = input("Enter the Student Roll Number: ")
num_subjects = int(input("Enter the Number of Subjects: "))
subjects = []
subject_marks = {}
for i in range(num_subjects):
    subject = input(f"Enter the Subject {i + 1}: ")
    marks = int(input(f"Enter the Marks Obtained in {subject}: "))
    subjects.append(subject)
    if subject not in subject_marks:
        subject_marks[subject] = marks
unique_subjects = list(set(subjects))
print("-------STUDENT DETAILS------")
print(f"Student Name : {student_name}")
print(f"Roll Number : {roll_number}")
print("---Unique Subjects----")
for subject in unique_subjects:
    print(subject)
print("---- Subject Marks------")
for subject, marks in subject_marks.items():
    print(f"{subject} : {marks}")    

