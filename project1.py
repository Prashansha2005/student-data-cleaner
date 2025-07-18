with open("projects/datacleaner/data.txt", "r") as f: #opens file in read mode
    content = f.readlines() #reads the file line by line
dict_data = []           #list to store student data
for line in content:      #iterates through each line in the file
    line=line.strip()        # strip remove trailing \n or spaces
    # Check if the line is empty or does not contain a comma
    # If it does not, skip to the next iteration
    if not line or ',' not in line:
        continue
    
    name,marks =line.split(",") #splits the line into name and marks
    name=name.strip()   #strip removes trailing spaces
    marks=marks.strip()  #strip removes trailing spaces
    if not marks.isdigit():   #checks if marks is a digit or empty
        marks="0"           #if empty it gives marks as 0

    if(marks.isdigit()):  #checks if marks is a digit or float
       #if marks is a digit 
     student={
        "name":name,
        "marks":int(marks)
    }
     dict_data.append(student)  #adds student data to the list


print(dict_data) #prints the list of student data
  
total_marks= sum(student["marks"] for student in dict_data)
num_students = len(dict_data)
class_avg= (total_marks/num_students)
print(f"class average: {class_avg}")

sorted_data= sorted(dict_data, key=lambda x: x["marks"])
for student in sorted_data:
    print(f"{student['name']}: {student['marks']}")

highest_marks = max(student["marks"] for student in dict_data)
top_students= [student for student in dict_data if student["marks"] == highest_marks]

print(f"top students: {top_students}")

dict_data2=[]

for student in dict_data:
    if student["marks"] >= 80:
        student["grade"] = "A"
    elif student["marks"] >= 60:
        student["grade"] = "B"
    elif student["marks"] >= 40:
        student["grade"] = "C"
    else:
        student["grade"] = "D"

    

for student in dict_data:
    print(f"{student['name']} - marks:{student['marks']} -grade:{student['grade']}")






    '''Concept	                     What it means in plain English
for student in dict_data	          Go over each student dictionary
if student["marks"] == highest_marks	Check if this student is the topper
[x for x in list if condition]	        Short way to filter things
for line in content:	               Read each line one by one until done — no need to set stop manually
print(dict_data)	                  Show entire list of student dictionaries (raw)
for x in dict_data:                    print(...)	Show each entry, but in a clean format'''



'''for student in dict_data:
    if student["marks"] == highest_marks:
        print(student)



        for variable in iterable:
    # do something
Python doesn't allow you to write a condition (if) directly after the in — unless you're using list comprehension.

So you can't do:

python
Copy code
for x in list if condition:
    ...
BUT you can do:

python
Copy code
[x for x in list if condition]  #  List comprehension
'''