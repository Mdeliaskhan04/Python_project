number=float(input('Enter the number= '))
if(number>=80 and number<=100):
    print('The result is A+')
elif(number>=75 and number<80):
    print('The result is A')
elif(number>=70 and number<75):
    print('The result is A-')
elif(number>=65 and number<70):
    print('The result is B+')
elif(number>=60 and number<65):
    print('The result is B')
elif(number>=55 and number<60):
    print('The result is B-')
elif(number>=50 and number<55):
    print('The result is C+')
elif(number>=45 and number<50):
    print('The result is C')
elif(number>=40 and number<45):
    print('The result is D')
else:
    print('Oh! Sorry...He will be fail!!!')