number=float(input('Enter the number= '))
if(number>=80 and number<=100):
    print('The result is A+')
elif (number>=70 and number<80):
    if(number>=70 and number<75):
        print('The result is A-')
    elif(number>=75 and number<80):
        print('The result is A')
else:
    print('He will be fail')