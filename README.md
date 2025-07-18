# student-data-cleaner
a basic student data cleaner using python
# Student Data Cleaner & Analyzer

A beginner-friendly Python project that mimics what real data scientists do!  
This tool cleans and analyzes a CSV file containing student records, helping you get ML-ready skills like data imputation, sorting, filtering, and more.

Machine Learning is 80% data cleaning and understanding.
This project builds real foundational thinking — how to clean, organize, and extract insights from raw data.

---

 Features:

- Loads student data from a `.csv` file
- Cleans the data by:
  - Stripping extra whitespaces
  - Replacing missing marks with `0` (or average)
- Calculates:
  - Average marks of all students
  -  Topper(s) name(s)
  -  List of students who failed (marks < 35)
- Sorts students by their marks (highest → lowest)
- Assigns grades:
  - A: 80+
  - B: 60–79
  - C: 40–59
  - F: < 40
- Counts how many students fall under each grade category

---

 Project Structure

student-data-cleaner-analyzer//
│
├── data/
│ └── students.csv ==Your raw student data
│ └── cleaned_students.csv -- Auto-generated clean version
│
├── main.py -- Your Python script
├── requirements.txt -- Libraries (like pandas)
└── README.md -- This file

 Output:
Printed results like:
1.Average marks
2.Topper(s)
3.Failed students
4.Sorted list
5.Grade-wise count

concepts used:
File handling (open(), .readlines())
Lists & dictionaries
String methods (split(), strip())
Conditional logic (if-else)
Functions
Basic data imputation

Author
Prashansha Rawat
 CS Undergrad- 1st year | Learning Python & ML | Passionate about ai/ml and Real-World Projects
