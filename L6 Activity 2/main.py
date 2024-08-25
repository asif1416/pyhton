# Comparing numbers
a = 10
b = 12
c = 12

print(a != b)  # Output: True
print(b != c)  # Output: False

# Comparing strings
a = "python"
b = "coding"

if a != b:
    print(a, "and", b, "are different.")  # Output: python and coding are different.

# Comparing expressions
a = 4
b = 5

if (a == 1) != (b == 5):
    print("Hello")  # Output: Hello

# Checking even numbers
a = int(input("Enter a number: "))

if a % 2 != 0:
    print(a, "is not an even number.")