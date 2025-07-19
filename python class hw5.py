students = {
    "Alice": [88, 92, 79],
    "Bob": [85, 78, 91],
    "Charlie": [90, 82, 88],
    "Diana": [65, 70, 72],
    "Eve": [95, 89, 93]
}
avg_student_grade = {}
for name, grades in students.items():
    avg = sum(grades) / len(grades)
    avg_student_grade[name] = avg
all_grades = [grade for grades in students.values() for grade in grades]

high=[]
medium = []
low =[]
for name, avg_grade in avg_student_grade.items():
    if avg_grade >= 85 :
        high.append(name)
    elif avg_grade < 85 and avg_grade >= 70 :
        medium.append(name)
    else:
        low.append(name)

sorted_avg_des = dict(sorted(avg_student_grade.items(),key = lambda item:item[1], reverse = True))
student_order = list(sorted_avg_des.keys())
grade_order = list(sorted_avg_des.values())

print("Performance Categories:")
print(f"High: {high}")
print(f"Medium: {medium}")
print(f"Low: {low}")
print(f"Top Student: {student_order[0]} with {grade_order[0]:.2f}%")
print(f"Class avg: {sum(all_grades) / len(all_grades):.1f}"+"%")