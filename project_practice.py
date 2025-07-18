with open("projects/datacleaner/data.txt", "r") as f:  # opens file in read mode
    content = f.readlines()  
    dict_data=[]
    for line in content:
        line=line.strip()
        if not line or ',' not in line:
            continue
        name,marks= line.split(',')
        name=name.strip()
        marks=marks.strip()

        if not marks.isdigit():
            marks="0"
        
        if marks.isdigit():
            student={
                "name": name,
                "marks":int(marks)

            }
            dict_data.append(student)
print(dict_data)

total_marks=sum(student['marks'] for student in dict_data)
num_students=len(dict_data)
class_avg=(total_marks/num_students)
print(f"class average : {class_avg}")

sorted_marks= sorted(dict_data, key=lambda x:x["marks"])
for student in sorted_marks:
    print(f"{student["name"]}:{student["marks"]}")
highest_marks= max(student["marks"] for student  in dict_data) 
print(f"highest marks: {highest_marks}")

for student in dict_data:
    if student["marks"]>=80:
        student["grade"]="A"
    elif student["marks"]>=60:
        student["grade"]="B"
    elif student["marks"]>=40:
        student["grade"]="C"
    else:
        student["grade"]="D"

print(dict_data)