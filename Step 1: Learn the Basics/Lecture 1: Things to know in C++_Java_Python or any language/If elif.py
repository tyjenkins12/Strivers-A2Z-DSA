class Solution:
    def studentGrade(self, marks):
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
s = Solution()
print(s.studentGrade(13))
