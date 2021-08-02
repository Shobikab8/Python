a=int(input('Enter the first input'))
b=int(input('Enter the second input'))
if 1<=a<=10**10 and 1<=b<=10**10:
    print(a+b)
    print(a-b)
    print(a*b)
else:
	print("Enter valid numbers ie. between 1 and 10^10")