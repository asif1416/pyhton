# Taking marks as input from user
print("Enter Marks Obtained in 4 Subjects:")
math = int(input("maths: "))
english = int(input("english: "))
science = int(input("science: "))
biology = int(input("biology: "))

# Calculating the total marks
sum = math + english + science + biology
print("Sum of math, english, science, and biology:", sum)

# Calculating the percentage
percentage = (sum / 400) * 100

# Printing the percentage
print("Percentage Mark =", percentage)