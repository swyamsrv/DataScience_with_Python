# score = int(input('Enter the score'))
# GRADE = None
# if score >= 90:
#     GRADE = 'A'
# else:
#     if score >= 80: 
#         GRADE = 'B'
#     else:
#         if score >= 70:
#             GRADE = 'C'
#         else:
#             if score >= 60:
#                 GRADE = 'D'
#             else:
#                 GRADE = 'E'

# print(GRADE)
# __________________________________________

from tkinter.messagebox import NO


score = int(input("Enter the marks ->"))
Grade = None

if score >= 90:
    Grade = 'A'
elif score >= 80:
    Grade = 'B'
elif score >= 70:
    Grade = 'C'
elif score >= 60:
    Grade = 'D'
else:
    Grade = 'FAIL'
    
print(Grade)