student_scores = {
  "reshu": 81,
  "siva": 91,
  "ganesh": 55,
  "bhanu": 35
}
student_grades = {}
for student in student_scores:
  score = student_scores[student]
  #print(student)
  #print(student_scores[student])
  if score > 90:
    student_grades[student] = "outstanding"
  elif score > 80:
    student_grades[student] = "Exppections"
  elif score >70:
     student_grades[student] = "Accpetable"
  else:
     student_grades[student] = "Fail"

print(student_grades)