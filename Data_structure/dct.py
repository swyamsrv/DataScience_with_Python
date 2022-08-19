dd = {}
lst = ['A', 'B', 'C', 'D', 'E']
dd = {'A' : {'Maths': 55, 'English': 56, 'CSE' : 50, 'GK': 58, 'Physics': 60}, 
      'B' : {'Maths': 54, 'English': 59, 'CSE' : 60, 'GK': 87, 'Physics': 88}, 
      'C' : {'Maths': 4, 'English': 5, 'CSE' : 6, 'GK': 7, 'Physics': 80}, 
      'D' : {'Maths': 51, 'English': 69, 'CSE' : 61, 'GK': 67, 'Physics': 98}, 
      'E' : {'Maths': 101, 'English': 159, 'CSE' : 560, 'GK': 987, 'Physics': 8888}}

name = input("Enter the name of the Student\n")
if name in dd:
    print(dd[name])
