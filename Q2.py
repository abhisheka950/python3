N=int(input('Enter the three digit Number:'))
a=N%100
b=a%10
if b%2==0:
    print (N,'is even')
else:
    print(N,'is odd')
