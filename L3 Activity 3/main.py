#input a word
text = str(input("Enter a string: "))

#Resverse string
#Using step value as -1 to iterate in reverse 
revText = text[::-1]
text = revText

print("Reverse of Given String is: ")
print(text)