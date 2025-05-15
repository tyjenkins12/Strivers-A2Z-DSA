class Solution:
    def studentGrade(marks):
        grade = ""
        if marks >= 90:
            grade = "Grade A"
        elif marks >= 70:
            grade = "Grade B"
        elif marks >= 50:
            grade = "Grade C"
        elif marks >= 35:
            grade = "Grade D"
        else:
            grade = "Fail"
        return grade
    marks = 13
    print(studentGrade(marks))