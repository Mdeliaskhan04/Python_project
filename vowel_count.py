text=input('Enter the string= ')
length=len(text)-1
string='aeiou'
count=0
index=0
while index<length:
    if text[index].lower() in string:
        count+=1
    index+=1
print('The number of vowels are=',count)
