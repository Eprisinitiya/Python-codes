def second_lowest_students():
    students = []
    for _ in range(int(input("Enter number of students: "))):
        name = input("Enter name: ")
        grade = float(input("Enter grade: "))
        students.append([name, grade])
    second_lowest = sorted(list(set(grade for name, grade in students)))[1]
    names = [name for name, grade in students if grade == second_lowest]
    for name in sorted(names):
        print(name)

second_lowest_students()
