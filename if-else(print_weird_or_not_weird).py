def start():
    n=int(input("Enter a value : "))
    if n>=1 and n<=100:
        if n%2!=0:
            print('Weird')
        elif n%2==0 and 2<=n<=5:
            print('Not Weird')
        elif n%2==0 and 6<=n<=20:
            print('Weird')
        else:
            print('Not Weird')
    else:
        print('Enter a valid number')
        start()
    return
start()

x=1000
for i in range(x):
    q=input("Want to try again?(ans with yes or no)")
    if q=='yes' or q=='Yes' or q=='YES':
        print("Ok then here we go")
        start()
    else:
        print('Ok then have a nice day!')
        break
