print("String reversal operation:")
text=input('Enter a string= ')
string=" "
length=len(text)-1
while length>=0:
    string+=text[length]
    length-=1
print(string)