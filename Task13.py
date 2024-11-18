def average_marks():
    n = int(input("Enter number of students: "))
    student_marks = {}
    for _ in range(n):
        data = input("Enter name and marks separated by space: ").split()
        name = data[0]
        marks = list(map(float, data[1:]))
        student_marks[name] = marks
    query_name = input("Enter student name to query: ")
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{average:.2f}")

average_marks()