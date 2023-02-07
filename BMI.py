weight = float(input('Enter your Weight in kg:'))
height = float(input('Enter your Height in meters:'))

height = height / 100
BMI = weight / height ** 2
print('your body mass index is', BMI)
if BMI > 0:

    if BMI <= 16:
        print('Severly Under Weight')
    elif BMI <= 18.5:
        print('Under weight')
    elif BMI <= 25:
        print('healthy weight')
    elif BMI <= 30:
        print('over weight')
    else:
        print('severly over weight')
else:
    print('enter vaild details')

    